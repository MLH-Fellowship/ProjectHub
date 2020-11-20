import json
from jwcrypto import jwk, jwe
from jwcrypto.common import json_decode, json_encode
from github_auth import GitHub
from settings import PRIV_KEY_PATH, PUB_KEY_PATH
import base64


from typing import Optional
from fastapi.security.http import (
    HTTPBase,
    HTTPBearerModel,
    get_authorization_scheme_param,
    HTTPAuthorizationCredentials,
    Request,
    HTTPException,
    HTTP_403_FORBIDDEN
)
from pydantic import BaseModel


class HTTPAuthorizationJWT(BaseModel):
    scheme: str
    credentials: str
    github_id: int
    github_at: str


class HTTPBearerJWEScheme(HTTPBase):
    def __init__(
        self,
        *,
        bearerFormat: Optional[str] = None,
        scheme_name: Optional[str] = None,
        auto_error: bool = True,
    ):
        self.model = HTTPBearerModel(bearerFormat=bearerFormat)
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        authorization: str = request.headers.get('Authorization')
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail='Not authenticated'
                )
            else:
                return None
        if scheme.lower() != 'bearer':
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN,
                    detail='Invalid authentication credentials',
                )
            else:
                return None

        context = decode(credentials)
        if not context:
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN,
                    detail='Authentication credentials expired',
                )
            else:
                return None

        return HTTPAuthorizationJWT(
            scheme=scheme,
            credentials=credentials,
            github_id=context['id'],
            github_at=context['at']
        )

    
with open(PRIV_KEY_PATH, 'rb') as priv, open(PUB_KEY_PATH, 'rb') as pub:
    public_key = jwk.JWK.from_pem(pub.read())
    private_key = jwk.JWK.from_pem(priv.read())

protected_header = {
    'alg': 'RSA-OAEP-256',
    'enc': 'A256CBC-HS512',
    'typ': 'JWE',
    'kid': public_key.thumbprint(),
}


def encode(uid, at):    
    payload = json_encode({'at': at, 'id': uid})

    token = jwe.JWE(payload.encode('utf-8'),
                       recipient=public_key,
                       protected=protected_header)
    encrypted = token.serialize()

    return base64.encodebytes(encrypted.encode('utf-8')).decode('ascii')


def decode(encrypted):
    try:
        decoded = base64.decodebytes(encrypted.encode('utf-8'))
        token = jwe.JWE()
        token.deserialize(decoded, key=private_key)
        return json_decode(token.payload)
    except Exception as e:
        print(e)
        return None
    