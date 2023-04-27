import http.server
import socketserver
import csv

PORT = 8002
FILENAME = 'data.csv'

class WriteHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            html = """
            <html>
            <head>
                <title>Форма</title>
            </head>
            <body>
                <form method="post" action="/submit">
                    <label for="name">Имя:</label>
                    <input type="text" id="name" name="name"><br>
                    <label for="email">Почта:</label>
                    <input type="email" id="email" name="email"><br>
                    <label for="text">Текс:</label>
                    <input type="text" id="text" name="text"><br> 
                    <input type="submit" value="Submit">
                </form>
            """
            try:
                csvfile = open(FILENAME, newline='')
                r = csv.reader(csvfile)
                html += '<table>'
                for row in r:
                    html += '<tr>'
                    for item in row:
                        html += f'<td>{item}</td>'
                    html += '</tr>'
                html += '</table>'
            except FileNotFoundError:
                pass
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        fields = post_data.decode('utf-8').split('&')
        values = [f.split('=')[1] for f in fields]
        csvfile = open(FILENAME,'a', newline='')
        w = csv.writer(csvfile)
        w.writerow(values)
        self.send_response(301)
        self.send_header('Location', '/')
        self.end_headers()

httpd = socketserver.TCPServer(("", PORT), WriteHandler)
httpd.serve_forever()
