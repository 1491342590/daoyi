import base64
import hashlib

#支持的加密
print(dir(hashlib))

#MD5
md = hashlib.md5()
md.update('admin'.encode('utf-8'))
print(md.hexdigest())
#b方便
md1 = hashlib.md5()
md1.update(b'admin')
print(md1.hexdigest())

#SHA1
sha1 = hashlib.sha1()
sha1.update(b'admin')
print(sha1.hexdigest())

#SHA256
sha256 = hashlib.sha256()
sha256.update(b'admin')
print(sha256.hexdigest())

#Base64
#编码
data = b'admin'
get_base64 = base64.b64encode(data)
print(get_base64.decode())
#解码
data1 = 'YWRtaW4='
get_base64_1 = base64.b64decode(data1)
print(get_base64_1.decode())