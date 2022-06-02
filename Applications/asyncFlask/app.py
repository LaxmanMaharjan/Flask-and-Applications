from flask import Flask
import asyncio
from aiohttp import ClientSession
from timeit import default_timer
from AsyncFlaskProject import timer

import requests


# Create the Flask application
app = Flask(__name__)


#urls = ['http://127.0.0.1:4000/crud/']
urls = ['http://example.com' for _ in range(1000)]

async def fetch_url(session, url):
    """Fetch the specified URL using the aiohttp session specified."""
    response = await session.get(url)
    return {'url': response.url, 'status': response.status}

@app.route('/')
def index():
    return 'Examples of using the new asynchronous features of Flask 2.0!'


@app.route('/async')
async def async_get():
    """Asynchronously retrieve the list of URLs using the new async/await support in Flask 2.0."""
    start_time = default_timer()

    # Retrieve all the URLs asynchronously using aiohttp
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        sites = await asyncio.gather(*tasks)

    # Generate the HTML response
    response = '<h1>URLs:</h1>'
    for site in sites:
        response += f"<p>URL: {site['url']} --- Status Code: {site['status']}</p>"
    total_elapsed_time = default_timer() - start_time
    response += f'<h3>Elapsed time: {total_elapsed_time}</h3>'

    return response


@app.route('/sync')
@timer
def sync_get():
    """Synchronously retrieve the list of URLs (works in Flask 1.x and 2.0)."""
    sites = []
    for url in urls:
        response = requests.get(url)
        sites.append({'url': response.url, 'status': response.status_code})

    # Generate the HTML response
    response = '<h1>URLs:</h1>'
    for site in sites:
        response += f"<p>URL: {site['url']} --- Status Code: {site['status']}</p>"
    return response

