import collections
import datetime
import os

import pandas

from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

load_dotenv()
IMPORT_CATALOGUE = os.getenv('CATALOGUE_PATH')
YEAR_OF_FOUNDATION = 1920

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

age_of_the_winery = datetime.datetime.now().year - YEAR_OF_FOUNDATION
products_from_file = pandas.read_excel(
    IMPORT_CATALOGUE, na_values=['Nan', 'nan'], keep_default_na=False
)

wines_grouped_by_category = collections.defaultdict(list)
for product in products_from_file.to_dict(orient='records'):
    category = product['Категория']
    wines_grouped_by_category[category].append(product)

render_page = template.render(
    age_of_the_winery=age_of_the_winery,
    wines_grouped=wines_grouped_by_category,
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
