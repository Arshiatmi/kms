import hashlib
import base64

#Returns MD5 Hashed String
def MD5_hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

#Returns sha256 Hashed String
def sha256_hash(string):
    m = hashlib.sha256()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

#Returns Something That Encoded In OpenSSL Algorithm
def openssl_alg(string):
    h = hashlib.new("ripemd160")
    h.update(string)
    h.hexdigest()

def base64_encode(string):
    return base64.b64encode(string)

def base64_decode(string):
    return base64.b64decode(string)

def base32_encode(string):
    return base64.b32encode(string)

def base32_decode(string):
    return base64.b32decode(string)

def base16_encode(string):
    return base64.b16encode(string)

def base16_decode(string):
    return base64.b16decode(string)
