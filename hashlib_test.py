import hashlib

md5 = hashlib.md5(b'c8b388b4459e13f978d7c846f4')
md5.update('1234'.encode('utf-8'))
print(md5.hexdigest())
