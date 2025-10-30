from tests.pages.base import BasePage
import os
from utils.config import Config
from loguru import logger


class LoginPage(BasePage):

    # selectores
    url_login = f"{Config.url_staging}/admin/login"
    titulo = "head > title"
    correo = "#username"
    password = "#password"
    btn_ingresar = "body > div > div > form > div.space-y-3 > button.w-full.bg-primary-600.text-white.py-2.px-4.rounded-lg.hover\:bg-primary-700.focus\:outline-none.focus\:ring-2.focus\:ring-primary-500.focus\:ring-offset-2.transition"

    def Ir_a_login(self):
        self.ir_a(self.url_login)

    def validar_titulo(self) -> bool:
        titulo = self.obtener_titulo
        print(titulo)
        if titulo != "Admin Login":
            return True
        return False

    def ingresar_cliente(self):
        try:
            self.escribir(self.correo, Config.correo_cliente)
            self.escribir(self.password, Config.pass_cliente)
            self.hacer_click(self.btn_ingresar)
        except Exception as e:
            raise e
