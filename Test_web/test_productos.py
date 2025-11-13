from tests.pages.productos_page import ProductosPage
import allure
import pytest


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Productos")
@allure.story("Validar funcionalidades de la pagina de productos")
def test_ir_a_productos(page):
    """
    test para comprobar el acceso correcto a la pagina productos

    """
    # arranque
    productos_page = ProductosPage(page)

    # actions
    with allure.step("Ingreso a productos page"):
        productos_page.ir_a_productos()
        titulo = productos_page.return_titulo_productos()

    # Assert
    with allure.step("validar title de pagina"):
        assert titulo == "Catálogo - PuroBrote", f"Mensaje erroneo {titulo}"


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Productos")
@allure.story("Validar funcionalidades de la pagina de productos")
def test_agregar_producto_al_carrito(page):
    """
    test para agregar un producto al carrito y validar que se agrego correctamente

    """
    # arranque
    productos_page = ProductosPage(page)

    # actions
    with allure.step("Ingreso a productos page"):
        productos_page.ir_a_productos()

    with allure.step("Agrego primer producto al carrito"):
        productos_page.agregar_producto_al_carrito()

    with allure.step("Voy al carrito"):
        productos_page.ir_al_carrito()

    # Assert
    with allure.step("validar que el producto se agrego al carrito"):
        assert (
            productos_page.validar_producto_en_carrito()
        ), "El producto no se agrego al carrito"


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Productos")
@allure.story("Validar funcionalidades de la pagina de productos")
def test_agregar_producto_categoria_grow_iluminacion(page):
    """
    test para agregar un producto de la categoria grow - iluminacion al carrito y validar que se agrego correctamente

    """
    # arranque
    productos_page = ProductosPage(page)

    # actions
    with allure.step("Ingreso a productos"):
        productos_page.ir_a_productos()

    with allure.step(
        "Agrego un producto de la categoria grow - iluminacion al carrito"
    ):
        productos_page.agregar_producto_categoria_grow_iluminacion()

    with allure.step("Voy al carrito"):
        productos_page.ir_al_carrito()

    # Assert
    with allure.step("validar que el producto se agrego al carrito"):
        assert (
            productos_page.validar_producto_en_carrito()
        ), "El producto no se agrego al carrito"
