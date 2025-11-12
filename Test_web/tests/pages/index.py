from tests.pages.base import BasePage
from utils.config import Config
import os


class IndexPage(BasePage):

    url_index = Config.url_staging
    carrito = "body > header > div > div > a.relative.inline-block"
    producto_ejemplo = ".agregar-btn[data-id='4']"
    btn_seguimiento_pedido = "#btnSeguimiento"
    input_pedido = "#inputPedido"
    btn_buscar_pedido = "#btnBuscar"
    btn_OK_seguimiento_pedido = "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled"
    datos_pedido = "#swal2-html-container"
    contador_carrito = "#contador-carrito"

    def ir_a_index(self):
        self.ir_a(self.url_index)

    def ir_al_carrito(self):
        self.hacer_click(self.carrito)

    def agregar_producto_al_carrito(self):
        self.hacer_click(self.producto_ejemplo)

    # seguimiento de pedido
    def click_btn_seguimiento_pedido(self):
        self.hacer_click(self.btn_seguimiento_pedido)

    def ingresar_numero_pedido(self):
        self.escribir(self.input_pedido, Config.numero_pedido)

    def buscar_pedido(self):
        self.hacer_click(self.btn_buscar_pedido)

    def btn_OK_seguimiento_pedido(self):
        self.hacer_click(self.btn_OK_seguimiento_pedido)

    def obtener_mensaje_seguimiento(self):
        pedido = self.page.text_content(self.datos_pedido)
        return pedido

    def validar_mensaje_seguimiento_pedido(self) -> bool:
        mensaje = self.obtener_mensaje_seguimiento()
        if Config.numero_pedido in mensaje:
            return True
        return False

    # --- fin seguimiento de pedido -------

    def return_titulo_index(self) -> str:
        titulo = self.obtener_titulo()
        return titulo

    def validar_producto_en_carrito(self) -> bool:
        contador = self.page.text_content(self.contador_carrito)
        if contador == "1":
            return True
        return False
