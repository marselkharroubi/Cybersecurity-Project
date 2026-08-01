symmetric code

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
message = "Hello, World!"
encrypted_message = cipher.encrypt(message.encode())
decrypted_message = cipher.decrypt(encrypted_message)
print("Shared Key:", key.decode())
print("Original Message:", message)
print("Encrypted Message:", encrypted_message.decode())
print("Decrypted Message:", decrypted_message.decode())

#output

#Shared Key: <generated key>
#Original Message: Hello, World!
#Encrypted Message: gAAAAAB...
#Decrypted Message: Hello, World!
