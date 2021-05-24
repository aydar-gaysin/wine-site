import datetime
import pandas

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pprint

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

years_running = int(datetime.datetime.now().year) - 1920
excel_data = pandas.read_excel('wine.xlsx')
wine_bottles = []
for index in range(6):
    wine_bottles.append(
        {
            'title': excel_data.to_dict()['Название'][index],
            'price': f'{excel_data.to_dict()["Цена"][index]} руб.',
            'sort': excel_data.to_dict()['Сорт'][index],
            'image': f'images/{excel_data.to_dict()["Картинка"][index]}'
        }
    )

render_page = template.render(
    years_running=years_running,
    wine_bottles=wine_bottles,
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
