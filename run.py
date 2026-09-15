#!/usr/bin/env python3
"""
GTA 5 RP "ТУЛЕВО ЗА РОНАЛДУ" - LOCAL WEBSERVER LAUNCHER
Runs high-performance HTTP server and opens browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/index.html"
            print("=" * 65)
            print(f"  GTA 5 RP: ТУЛЕВО ЗА РОНАЛДУ (ROCKFORD & REDWOOD DM)")
            print(f"  Сервер запущен: {url}")
            print(f"  Нажмите Ctrl+C для остановки")
            print("=" * 65)
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError:
        # Fallback to port 8081 if 8080 is in use
        alt_port = 8085
        with socketserver.TCPServer(("", alt_port), Handler) as httpd:
            url = f"http://localhost:{alt_port}/index.html"
            print(f"  Сервер запущен на альтернативном порту: {url}")
            webbrowser.open(url)
            httpd.serve_forever()

if __name__ == '__main__':
    main()
