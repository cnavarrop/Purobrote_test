from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def ir_a(self, url: str):
        self.page.goto(url)

    def obtener_titulo(self):
        return self.page.title()

    def hacer_click(self, selector: str):
        self.page.click(selector)

    def escribir(self, selector: str, texto: str):
        self.page.fill(selector, texto)

    def esta_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
