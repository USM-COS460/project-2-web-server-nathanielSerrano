# Nathaniel Serrano
# COS 460
# Project 2
# A simple web server that serves static files and handles basic HTTP requests.

import socket
import os
import threading
import mimetypes
import sys 
from datetime import date, datetime, timezone


HOST, PORT = 'localhost', 8080
DOCUMENT_ROOT = './www'

def handle_request(client_socket, doc_root):
    try:
        request = client_socket.recv(1024).decode('utf-8')
        lines = request.split('\r\n')
        if len(lines) > 0:
            request_line = lines[0]
            method, path, _ = request_line.split()
            if method == 'GET':
                serve_file(client_socket, path, doc_root)
            else:
                send_405(client_socket)
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        client_socket.close()

def serve_file(client_socket, path, doc_root=DOCUMENT_ROOT):
    if path.endswith('/'):
        path += 'index.html'
    file_path = os.path.join(doc_root, path.lstrip('/'))
    if os.path.exists(file_path) and os.path.isfile(file_path):
        mimetype, _ = mimetypes.guess_type(file_path)
        with open(file_path, 'rb') as f:
            content = f.read()
        response = (
            f"HTTP/1.1 200 OK\r\n"
            f"Date: {datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}\r\n"
            f"Server: Server del Serrano\r\n"
            f"Content-Type: {mimetype or 'application/octet-stream'}\r\n"
            f"Content-Length: {len(content)}\r\n"
            f"\r\n"
        ).encode('utf-8') + content
        client_socket.sendall(response)
    else:
        send_404(client_socket)

def send_404(client_socket):
    response = (
        "HTTP/1.1 404 Not Found\r\n"
        f"Date: {datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}\r\n"
        f"Server: Server del Serrano\r\n"
        "Content-Type: text/html\r\n"
        "Content-Length: 48\r\n"
        "\r\n"
        "<html><body><h1>404 Not Found</h1></body></html>"
    ).encode('utf-8')
    client_socket.sendall(response)

def send_405(client_socket):
    response = (
        "HTTP/1.1 405 Method Not Allowed\r\n"
        f"Date: {datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}\r\n"
        f"Server: Server del Serrano\r\n"
        "Content-Type: text/html\r\n"
        "Content-Length: 58\r\n"
        "\r\n"
        "<html><body><h1>405 Method Not Allowed</h1></body></html>"
    ).encode('utf-8')
    client_socket.sendall(response)

def start_server(host, port, doc_root):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Serving HTTP on {host}:{port} ...")
    try:
        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=handle_request, args=(client_socket,doc_root,)).start()
    except KeyboardInterrupt:
        print("\nShutting down server.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    if len(sys.argv) != 4 and len(sys.argv) != 1:
        print("Usage: python web_server.py <host> <port> <document_root>")
        sys.exit(1)
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT
    doc_root = sys.argv[3] if len(sys.argv) > 3 else DOCUMENT_ROOT

    start_server(host, port, doc_root)