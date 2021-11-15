import asyncio
from arsenic import get_session, browsers, services
from webdriver_manager.chrome import ChromeDriverManager


def run(urls, scraper):
    asyncio.run(launch(urls, scraper))


async def launch(urls, scraper):
    tasks = []
    for chunk_urls in chunks(urls, 10):
        for url in chunk_urls:
            tasks.append(
                asyncio.create_task(get_content(url, scraper))
            )

    return await asyncio.gather(*tasks)


async def get_content(url, scraper):
    service = services.Chromedriver(binary=ChromeDriverManager().install())
    browser = browsers.Chrome()
    # hide options
    browser.capabilities = {
        "goog:chromeOptions": {"args": ["--headless", "--disable-gpu"]}
    }
    async with get_session(service, browser) as session:
        await asyncio.wait_for(session.get(url), timeout=60)
        html = await session.get_page_source()
        scraper(html)


def chunks(lst, n=10):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
