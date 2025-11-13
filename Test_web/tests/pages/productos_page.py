import os
from utils.config import Config
import allure
from tests.pages.base import BasePage


class ProductosPage(BasePage):

    url_productos = f"{Config.url_staging}/productos"
    primer_producto = "#contenedor-productos > div:nth-child(1)"
    agregar_al_carrito_btn = "button[data-id='1868']"
    carrito_icono = "body > header > div > div > a.relative.inline-block"
    contador_carrito = "#contador-carrito"
    categoria_grow = "xpath=//button[contains(text(), 'Grow')]"
    grow_iluminacion = "xpath=//a[contains(text(), '• Iluminación')]"
    producto_iluminacion = "button[data-id='299']"

    def ir_a_productos(self):
        self.ir_a(self.url_productos)

    def agregar_producto_al_carrito(self):
        self.hacer_click(self.agregar_al_carrito_btn)

    def ir_al_carrito(self):
        self.hacer_click(self.carrito_icono)

    def validar_producto_en_carrito(self) -> bool:
        contador = self.page.text_content(self.contador_carrito)
        if contador and int(contador) > 0:
            return True
        return False

    def return_titulo_productos(self) -> str:
        titulo = self.obtener_titulo()
        return titulo

    def agregar_producto_categoria_grow_iluminacion(self):
        self.hacer_click("text=Grow")
        self.hacer_click(self.grow_iluminacion)
        self.hacer_click(self.producto_iluminacion)
