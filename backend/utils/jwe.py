import jwt
from . import rsa
from github_auth import GitHub
from settings import PRIV_KEY_PATH, PUB_KEY_PATH


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
        authorization: str = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )
            else:
                return None
        if scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN,
                    detail="Invalid authentication credentials",
                )
            else:
                return None

        context = decode(credentials)
        if not context:
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN,
                    detail="Authentication credentials expired",
                )
            else:
                return None

        return HTTPAuthorizationJWT(
            scheme=scheme,
            credentials=credentials,
            github_id=context['id'],
            github_at=context['access_token']
        )



def encode(at, private_key_path=PRIV_KEY_PATH):
    private_key = rsa.load_private_key(private_key_path)
    auth = GitHub(at=at)
    gh_user_id = auth.id()

    payload = {"access_token": at, "id": gh_user_id}
    encoded = jwt.encode(payload=payload, key=private_key, algorithm="RS256")

    return encoded


def decode(data, public_key_path=PUB_KEY_PATH):
    public_key = rsa.load_public_key(public_key_path)
    try:
        decoded = jwt.decode(jwt=data, key=public_key, algorithms="RS256")
    except Exception:
        # We want to reject the token and require the user to sign in again
        return None
    return decoded
