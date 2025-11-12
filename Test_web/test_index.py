import pytest
from tests.pages.index import IndexPage
from utils.config import Config
import allure


def test_ir_a_index(page):
    """
    test para comprobar el acceso correcto a la pagina index

    """
    # arranque
    index_page = IndexPage(page)

    # actions
    with allure.step("Ingreso a index page"):
        index_page.ir_a_index()
        titulo = index_page.return_titulo_index()

    # Assert
    with allure.step("validar title de pagina"):
        assert titulo == "Inicio", f"Mensaje erroneo {titulo}"


def test_agregar_producto_al_carrito(page):
    """
    test para comprobar que se agrega un producto al carrito desde la pagina index

    """
    # arranque
    index_page = IndexPage(page)

    # actions
    with allure.step("Ingreso a index page"):
        index_page.ir_a_index()
    with allure.step("Agregar producto al carrito"):
        index_page.agregar_producto_al_carrito()

    # Assert
    with allure.step("validar que el carrito tenga 1 producto"):
        assert (
            index_page.validar_producto_en_carrito()
        ), "No se agrego el producto al carrito"


def test_seguimiento_pedido(page):
    """
    test para comprobar el seguimiento de un pedido desde la pagina index

    """
    # arranque
    index_page = IndexPage(page)

    # actions
    with allure.step("Ingreso a index page"):
        index_page.ir_a_index()
    with allure.step("Click en boton seguimiento de pedido"):
        index_page.click_btn_seguimiento_pedido()
    with allure.step("Ingresar numero de pedido"):
        index_page.ingresar_numero_pedido()
    with allure.step("Buscar pedido"):
        index_page.buscar_pedido()

    # Assert
    with allure.step("validar mensaje de seguimiento de pedido"):
        assert (
            index_page.validar_mensaje_seguimiento_pedido()
        ), "El mensaje de seguimiento no es correcto"
