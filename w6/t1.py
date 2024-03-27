"""
    Exercise 1: Basic Parallelism with asyncio

    Task: Write a script to asynchronously download 5 websites using the asyncio module.
        Use the asyncio module to define asynchronous functions for downloading websites (download_site) and downloading all sites concurrently (download_all_sites).
        Execute the script using asyncio.run() or by creating an event loop with asyncio.get_event_loop().run_until_complete().

"""

import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://www.arstechnica.com",
        "https://www.brainpickings.org",
        "https://www.theguardian.com/long-reads",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


