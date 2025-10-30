from utils.config import Config
import os
from tests.pages.base import BasePage


class DashboardPage(BasePage):

    # Selectores
    titulo_bienvenida = (
        "body > main > div > div > div.bg-white.shadow.rounded-lg.p-6 > h2"
    )

    def validar_mensaje_bienvenida_cliente(self) -> bool:

        texto_bienvenida = (
            self.page.locator(self.titulo_bienvenida).inner_text().strip()
        )
        if texto_bienvenida == Config.bienvenida_cliente:
            return True
        return False

    def return_titulo_bienvenida(self) -> str:
        return self.page.locator(self.titulo_bienvenida).inner_text().strip()
