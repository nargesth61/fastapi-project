from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')

'''
To save the password in hashed form and decode the password hash for verify
'''

class Hash:
    @staticmethod
    def bcrypt(password):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)


