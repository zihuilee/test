import time


def application(environ, start_response):
    start_response('200 ok',[('Content-Type', 'text/html')])
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()