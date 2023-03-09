from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=50)
    context = browser.new_context()
    context.tracing.start(sources=True, screenshots=True, snapshots=True)
    page = context.new_page()
    page.goto("https://www.classcentral.com")
    my_list = page.locator("xpath=//html/body/*[not(self::script or self::link or self::noscript or self::style)]").all()
    for i in my_list:
        print(i.inner_text())
    context.tracing.stop(path="../log/trace.zip")
    input("Deneme")


with sync_playwright() as p:
    run(p)
