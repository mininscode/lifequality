import bcrypt


# Hashing password service
def hash_password(password: str) -> bytes:
    bytePassword = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytePassword, salt)
    return hashed_password
