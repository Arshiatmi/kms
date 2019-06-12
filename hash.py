import hashlib

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
