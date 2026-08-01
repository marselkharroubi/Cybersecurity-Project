#Digital signature code

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()
message = b"This is a secure message."
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Message signed successfully.")
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid. The message is authentic and unchanged.")
except Exception:
    print("Signature is invalid. The message may have been altered.")





#How it works:

#The private key is used to create a digital signature for the message
#The public key is used to verify the signature
#If the verification succeeds, the message is authentic and has not been modified. If it fails, the message may have been altered or the signature is not valid.
