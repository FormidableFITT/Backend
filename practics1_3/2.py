import http.server
import json
import socketserver
import urllib,urllib.request
PORT = 8003
api_key = "1AIzaSyBLLMaRNAmC-GZAv_pJQ8SLEy4SQV1pIf4"
cx = "112f9bb05f7a374333"

class SearchHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            html = '''
                       <html>
                       <body>
                       <form method="POST">
                       <label>Поиск:</label><br>
                       <input type="text" name="query" value=""><br>
                       <input type="submit" value="Submit">
                       </form> 
                       </body>
                       </html>
                   '''
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode('utf-8'))
        query = post_data.get('query')[0]
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
        print(url)
        html = '''
                      <html>
                      <body>
                      <form method="POST">
                      <label>Поиск:</label><br>
                      <input type="text" name="query" value="{}"><br>
                      <input type="submit" value="Submit">
                      </form>
                      {}
                      </body>
                      </html>
                  '''
        res = ''
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            results = json.loads(data)['items']
            if results:
                res += '<ul>'
                for i in results:
                    res += f'<li><a href="{i["link"]}">{i["title"]}</a></li><p>{i["snippet"]}</p>'
                res += '</ul>'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(html.format(query, res), 'utf-8'))


httpd = socketserver.TCPServer(("", PORT), SearchHandler)
httpd.serve_forever()
