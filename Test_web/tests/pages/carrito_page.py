from tests.pages.base import BasePage
from utils.config import Config
import os


class CarritoPage(BasePage):

    # selectores
    url_carrito = f"{Config.url_staging}/carrito"

    def ingresar_al_carrito(self):
        self.ir_a(self.url_carrito)
