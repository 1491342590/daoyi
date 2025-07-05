import requests
import socket
import socks

socks.set_default_proxy(socks.HTTP,'127.0.0.1',7897)
socket.socket = socks.socksocket

res = requests.get('https://www.google.com',timeout=3).content
print(res)