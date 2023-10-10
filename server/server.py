import json
import http.server
import socketserver
 
PORT = 8080
 
class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # try to create HTML page form results.json
        # If scraping has not finished yet, serve blank html insted
        try:    
            createHTML()
        except FileNotFoundError:
            print("scraping has not finished yet")

        self.path = "scraped_sreality.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def createHTML(fileName="/data/results.json"):
    f = open(fileName)
    data = json.load(f)

    f.close()

    # Create an HTML page
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sreality Scraping</title>
    </head>
    <body>
        <ul>
            {}
        </ul>
    </body>
    </html>
    """
    
    # Create HTML list items from JSON data
    items = ""
    for item in data:
        name = item["name"]
        img_tags = "".join(f'<img src="{img}" alt="{name}">' for img in item["imgs"])
        items += f"<li>{name}{img_tags}</li>"
    
    # Insert the list items into the HTML template
    html = html.format(items)
    

    with open("scraped_sreality.html", "w") as f:
        f.write(html) 

def makeBlankHTML():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sreality Scraping</title>
    </head>
    <body>
        <h1> Scraping has not finished yet </h1>
    </body>
    </html>
    """

    with open("scraped_sreality.html", "w") as f:
        f.write(html) 
    

 
def main():
    Handler = HttpRequestHandler
     
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print("Http Server Serving at port", PORT)
        httpd.serve_forever()

if __name__ == "__main__":
    makeBlankHTML()
    main()
