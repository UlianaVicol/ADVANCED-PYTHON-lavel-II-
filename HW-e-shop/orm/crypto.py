import hashlib 

secret_key = 'hfhfjmnmhhjhjghghgh'
password = '123456' + secret_key

hasher = hashlib.sha3_384(password.encode())

password_hash = hasher.hexdigest()

print(password_hash)
print(len(password_hash))