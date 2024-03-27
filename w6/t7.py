"""
    Exercise 7: Customizing ThreadPoolExecutor

    Task: Experiment with different values for the max_workers parameter in ThreadPoolExecutor to find the optimal concurrency level.
        Measure the script's performance for each concurrency level to determine the most efficient setting.

"""

import asyncio
import time
import aiohttp
from concurrent.futures import ThreadPoolExecutor

async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")

async def download_all_sites(sites, max_workers):
    async with aiohttp.ClientSession() as session:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            tasks = [loop.run_in_executor(executor, download_site, session, url) for url in sites]
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://github.com/",
        "https://www.bbc.com/"
    ] * 300

    # max_workers_values = [110, 111, 113, 114, 115, 116, 117, 118, 119, 120]

    max_workers_values = [10, 20, 35, 50, 70, 95, 220]

    for max_workers in max_workers_values:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_all_sites(sites, max_workers))
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} sites with max_workers={max_workers} in {duration} seconds")