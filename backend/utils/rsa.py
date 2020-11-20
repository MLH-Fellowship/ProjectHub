from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def gen_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()

    return private_key, public_key


def read_private_key(pk):
    return pk.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )


def read_public_key(pk):
    return pk.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


def create_and_save_key_pair(pair_name: str):
    (private, public) = gen_key_pair()
    
    pem = read_private_key(private)
    pub = read_public_key(public)

    with open(f'{pair_name}.pem', 'wb') as f:
        f.write(pem)

    with open(f'{pair_name}.pub', 'wb') as f:
        f.write(pub)


def load_public_key(filename: str):
    if not filename.endswith(".pub"):
        raise ValueError("Error: npublic key must end with .pub")

    with open(filename, 'rb') as f:
        return load_pem_public_key(f.read(), None)


def load_private_key(filename: str):
    if not filename.endswith(".pem"):
        raise ValueError("Error: private key must end with .pem")

    with open(filename, 'rb') as f:
        return load_pem_private_key(f.read(), None, default_backend())


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Useage: python rsa.py <key-name>')
        exit(1)
    create_and_save_key_pair(sys.argv[1])
