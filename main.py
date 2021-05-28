import collections
import datetime

import pandas

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

YEAR_STARTED = 1920
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

years_running = int(datetime.datetime.now().year) - YEAR_STARTED

excel_data = pandas.read_excel('wine3.xlsx', na_values=['Nan', 'nan'],
                               keep_default_na=False)

sorted_wines = collections.defaultdict(list)
for product in excel_data.to_dict(orient='records'):
    category = product['Категория']
    sorted_wines[category].append(product)

render_page = template.render(
    years_running=years_running,
    sorted_wines=sorted_wines,
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
