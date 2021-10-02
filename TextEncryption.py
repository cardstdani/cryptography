from cryptography.fernet import Fernet
import base64

message = "Hello world!"
print(message, message.encode())

key = Fernet.generate_key()
print(key)

key = base64.b64encode(("a"*32).encode())
print(key)

token = Fernet(key).encrypt(message.encode())
print("Encrypted: " + str(token))

print("Decrypted: " + str(Fernet(key).decrypt(token)))
