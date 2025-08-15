from playwright.sync_api import sync_playwright
import time

class DictaBrowser:
    def __init__(self, url="https://dicta-il-dictalm2-0-instruct-demo.hf.space", headless=True):
        self.url = url
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()
        self.page.goto(self.url)
        self.page.wait_for_selector('#component-10 textarea[data-testid="textbox"]', timeout=60000)

    def send_prompt(self, prompt):
        input_box = self.page.locator('#component-10 textarea[data-testid="textbox"]')
        input_box.fill(prompt)
        self.page.locator('#component-11').click()
        self.page.wait_for_selector('.message-wrap .bot', timeout=120000)
        time.sleep(5)
        last_bot_message = self.page.locator('.message-wrap .bot').inner_text()
        return last_bot_message.strip()

    def close(self):
        self.browser.close()
        self.playwright.stop()
