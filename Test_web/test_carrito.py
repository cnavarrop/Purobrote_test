import allure
import pytest
import os
from tests.pages.carrito_page import CarritoPage
from tests.conftest import carrito_con_item


def test_ir_al_carrito(carrito_con_item):
    # arranque
    carrito = CarritoPage(carrito_con_item)
    # actions
    carrito.ingresar_al_carrito()
    titulo = carrito.obtener_titulo()
    # assert
    assert titulo == "Carrito - Puro Brote"
