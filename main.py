import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

years_running = int(datetime.datetime.now().year)-1920
wine_bottles = [
    {
        'title': 'Изабелла',
        'price': '350 руб.',
        'sort': 'Изабелла',
        'image': 'images/izabella.png'
    },    {
        'title': 'Изабелла',
        'price': '350 руб.',
        'sort': 'Изабелла',
        'image': 'images/izabella.png'
    },    {
        'title': 'Изабелла',
        'price': '350 руб.',
        'sort': 'Изабелла',
        'image': 'images/izabella.png'
    },    {
        'title': 'Изабелла',
        'price': '350 руб.',
        'sort': 'Изабелла',
        'image': 'images/izabella.png'
    },    {
        'title': 'Изабелла',
        'price': '350 руб.',
        'sort': 'Изабелла',
        'image': 'images/izabella.png'
    },    {
        'title': 'Изабелла',
        'price': '350 руб.',
        'sort': 'Изабелла',
        'image': 'images/izabella.png'
    },
]
render_page = template.render(

    wine_bottles=wine_bottles,
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

