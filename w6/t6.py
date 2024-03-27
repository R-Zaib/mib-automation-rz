"""
    Exercise 6: Combining asyncio and ThreadPoolExecutor

    Task: Integrate asyncio with ThreadPoolExecutor to combine the advantages of asynchronous I/O and thread-based parallelism.
        Use asyncio.to_thread() function to execute blocking I/O operations within a separate thread.

"""

import asyncio
import time
import aiohttp
from concurrent.futures import ThreadPoolExecutor

async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_site(session, url)) for url in sites]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://github.com/"
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")