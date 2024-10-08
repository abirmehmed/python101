import ecdsa
from ecdsa import SigningKey, SECP256k1
import hashlib

# Generate a new key pair
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

def encrypt_message(message, private_key):
    # Hash the message
    hashed_message = hashlib.sha256(message.encode('utf-8')).digest()
    # Encrypt the message (signing)
    signature = private_key.sign(hashed_message)
    return signature

def decrypt_message(signature, public_key, original_message):
    try:
        # Hash the original message
        hashed_message = hashlib.sha256(original_message.encode('utf-8')).digest()
        # Verify the signature (decrypt the message)
        public_key.verify(signature, hashed_message)
        return "The message is verified"
    except ecdsa.BadSignatureError:
        return "The message could not be verified"

# Main program
if __name__ == "__main__":
    user_input = input("Enter a message to encrypt: ")
    encrypted_message = encrypt_message(user_input, private_key)
    print("Encrypted message:", encrypted_message)
    
    verification_result = decrypt_message(encrypted_message, public_key, user_input)
    print("Decryption result:", verification_result)
  
#It will Give Output Like This,
#Enter a message to encrypt: Hello World
#Encrypted message: b'\xb5\xa8\xb3\xca\xccX\x92\x81\xe4\xfe\xcd\x87\x96\x1f\xe0\xe0\xf1\xd2\x92`K\xfc\x85\x9c\xd0\xee\x9a`\x00_\xb4C9\xd9\x80,)\xf0\xa5\xae\xd5\x16\xcf\xb4\xc9\xb1\xbd\xf1`Z"\xc5hnd\xf4\xccl\x05\x11\xaabj#'
#Decryption result: The message is verified
#
