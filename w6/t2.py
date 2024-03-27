"""
    Exercise 2: Error Handling in asyncio

    Task: Enhance the previous script to handle exceptions gracefully using try-except blocks in the download_site function.
        Implement error handling within the download_site function using try-except blocks to catch exceptions raised during the HTTP request.
        Consider handling specific exceptions like aiohttp.ClientError for better error reporting.


"""

import asyncio
import time
import aiohttp


async def download_site(session, url):
    try:
        async with session.get(url) as response:
            print("Read {0} from {1}".format(response.content_length, url))
    except aiohttp.ClientError as e:
        print(f"Error downloading site: {url}, {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


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

