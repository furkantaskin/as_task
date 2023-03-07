from playwright.sync_api import sync_playwright, Playwright
from crawler.link_crawler import download_assets
import json


def test_json() -> list:
    with open("chrome_traces/trace.json", "r") as f:
        data = json.load(f)
        f.close()
    urls = []
    for i in data['traceEvents']:
        try:
            if "args" in i.keys() and "data" in i["args"].keys() and "renderBlocking" in i["args"]["data"].keys():
                urls.append(i["args"]["data"]["url"])
        except KeyError:
            print("Error for object: ", i)
    return urls


def run(playwright: Playwright) -> list:
    print("\033[0;35m Running playwright for crawling \033[0m")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    browser.start_tracing(page=page, path="chrome_traces/trace.json", categories=["devtools.timeline"])
    page.goto("https://www.classcentral.com")
    page.wait_for_load_state("load", timeout=0)
    browser.stop_tracing()
    # save_page(page.content())
    context.close()
    browser.close()
    return test_json()


my_urls = None

with sync_playwright() as p:
    my_urls = run(p)

download_assets(my_urls)
