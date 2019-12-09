from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from db import common
import json
import webbrowser
from socketserver import BaseServer
import time

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    params = parse_qs(environ['QUERY_STRING'])
    name = params.get('name')[0]
    no = params.get('password')[0]
    print("no:%s" % no)
    passwd = common.getPassword('password', 'user', 'name', str(name))
    print("passwd:%s" % passwd)
    if int(no) == int(passwd):
        #dic = {'message':'success','name': str(name)}
        #return json.dumps(dic)

        return "true"

    else:
        return "fail"
        #dic = {'name': name, 'password': no}
        #return json.dumps(dic)

if __name__ == "__main__":
    port = 5000
    httpd = make_server("192.168.3.94", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
    time.sleep(5)
    BaseServer.shutdown()
    httpd.shutdown()