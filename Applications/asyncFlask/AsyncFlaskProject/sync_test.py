import requests
from timeit import default_timer

#urls = ['http://127.0.0.1:4000/crud/' for _ in range(1000)]
urls = ['http://example.com' for _ in range(1000)]

start_time = default_timer()

for url in urls:
    response=requests.get(url)

total_elapsed_time = default_timer() - start_time
print(total_elapsed_time)
