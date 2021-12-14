import asyncio
import aiohttp


async def get_resource(session, url):
    """Coroutine that request to a specific url
    """
    async with session.get(url) as response:
        return await response.json()


async def get(urls):
    """Coroutine that run get_resource concurrently and return the results
    """
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_resource(session, url))
                 for url in urls]
        return await asyncio.gather(*tasks)
