import urllib.request

response=urllib.request.urlopen('http://47.103.124.166/museum-admin/index.html#/')
print(response.read().decode('utf-8'))



