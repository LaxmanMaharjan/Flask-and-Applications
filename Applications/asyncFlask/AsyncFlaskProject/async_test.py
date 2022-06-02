import asyncio
from aiohttp import ClientSession
from timeit import default_timer

async def fetch_response(session, url):
    """Fetch the specified response using the aiohttp session specified."""
    response = await session.get(url)
    return response


#urls = ['http://127.0.0.1:4000/crud/' for _ in range(1000)]
urls = ['http://example.com' for _ in range(1)]

async def async_get():
    """Asynchronously retrieve the list of URLs using the new async/await support in Flask 2.0."""

    # Retrieve all the URLs asynchronously using aiohttp
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_response(session, url))
            tasks.append(task)
        sites = await asyncio.gather(*tasks)
        print(sites[0].url)

start_time = default_timer()
asyncio.run(async_get())
total_elapsed_time = default_timer() - start_time
print(total_elapsed_time)
