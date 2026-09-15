import http.server
import socketserver
import socket
import os
import qrcode
import io

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable PWA headers and prevent stale caching of dynamic files
        if self.path.endswith('.html') or self.path.endswith('.js') or self.path.endswith('sw.js'):
            self.send_header('Cache-Control', 'no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def main():
    local_ip = get_local_ip()
    url = f"http://{local_ip}:{PORT}/index.html"

    print("=" * 60)
    print("  CHIIKAWA: GTA 5 RP | TUELVO - MOBILE SERVER")
    print("=" * 60)
    print(f"\n[1] URL to open on your phone (same Wi-Fi network):")
    print(f"    --> {url} <--")
    print(f"    --> http://localhost:{PORT}/index.html <--")
    print("-" * 60)

    try:
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(os.path.join(DIRECTORY, "mobile_qr.png"))
        print("[2] QR code image generated: mobile_qr.png")
    except Exception as e:
        print("QR generation notice:", e)

    print("-" * 60)
    print("Mobile server active on port 8080. Press Ctrl+C to stop.\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен.")

if __name__ == "__main__":
    main()
