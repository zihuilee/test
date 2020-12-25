import re
import select, time, socket, sys, os
import multiprocessing


class WSGIServer(object):
    """
    定义一个WSGI服务器类
    """
    def __init__(self, port, document_root, app):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))
        self.server_socket.listen(128)

        self.document_root = document_root
        self.app = app

    def run_forever(self, client_socket):
        while True:
            new_socket, new_addr = self.server_socket.accept()
            new_socket.settimeout(3)
            new_process = multiprocessing.Process(target=self.deal_with_request, args=(new_socket,))
            new_process.start()
            new_socket.close()

    def deal_with_request(self, client_socket):
        while True:
            try:
                request = client_socket.recv(1024).decode('utf-8')
            except Exception as e:
                print('=======>%s', e)
                client_socket.close()
                return

            if not request:
                client_socket.close()
                return
            request_lines = request.splitlines()
            for i, line in enumerate(request_lines):
                print(i, line)

            ret = re.match(r'([^/]*)([^ ])', request_lines[0])
            if ret:
                pass
