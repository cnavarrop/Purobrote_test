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
    btn_restablecer_contrasena = "#reset-password-btn"
    mensaje_ventana_restablecer_contrasena = "#swal2-title"
    textbox_restablecer_contrasena = "#swal2-input"
    btn_accion_restablecer_contrasena = "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled"
    btn_cancelar_restablecer_contrasena = "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-cancel.swal2-styled"
    mensaje_confirmacion_cambio_contrasena = "#swal2-title"

    def Ir_a_login(self):
        self.ir_a(self.url_login)

    def return_titulo_login(self) -> str:
        titulo = self.obtener_titulo()
        return titulo

    def ingresar_cliente_login(self):
        try:
            self.escribir(self.correo, Config.correo_cliente)
            self.escribir(self.password, Config.pass_cliente)
            self.hacer_click(self.btn_ingresar)
        except Exception as e:
            raise e

    def restablecer_contrasena(self):
        self.hacer_click(self.btn_restablecer_contrasena)
        self.escribir(self.textbox_restablecer_contrasena, Config.correo_cliente)
        self.hacer_click(self.btn_accion_restablecer_contrasena)

    def mensaje_confirmacion_restablecer_contasena(self):
        return self.obtener_mensaje(self.mensaje_confirmacion_cambio_contrasena)

    def return_titulo_restablecer_contrasena(self):
        return self.obtener_mensaje(self.mensaje_ventana_restablecer_contrasena)
