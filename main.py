from playwright.sync_api import sync_playwright, Playwright
import json


def test_json():
    with open("chrome_traces/trace.json", "r") as f:
        data = json.load(f)
    urls = []
    for i in data['traceEvents']:
        try:
            if "args" in i.keys() and "data" in i["args"].keys() and "renderBlocking" in i["args"]["data"].keys():
                print(i["args"]["data"]["url"])
                urls.append(i["args"]["data"]["url"])
        except KeyError:
            print("Error for object: ", i)


def run(playwright: Playwright) -> None:
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
    test_json()


with sync_playwright() as p:
    run(p)
