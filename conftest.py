import pytest
from typing import Generator
from playwright.sync_api import Page, Browser, sync_playwright


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as playwright:
        browser_instance = playwright.chromium.launch(headless=True)
        yield browser_instance
        browser_instance.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  # type: ignore[arg-type]
        locale="ru-RU"
    )
    page_instance = context.new_page()
    yield page_instance
    context.close()

