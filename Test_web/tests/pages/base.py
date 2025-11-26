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

    def obtener_mensaje(self, selector: str) -> str:
        return self.page.locator(selector).inner_text().strip()

    def esperar_elemento(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def obtener_sweetAlert(self):
        sweetalert = self.page.locator(".swal2-popup")
        return sweetalert

    def obtener_heading_sweetAlert(self):
        sweetalert = self.obtener_sweetAlert()
        heading = sweetalert.get_by_role("heading").inner_text().strip()
        return heading
