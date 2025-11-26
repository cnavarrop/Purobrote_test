from tests.pages.base import BasePage
from tests.pages.checkout_page import CheckoutPage
import allure
from tests.conftest import carrito_con_item
from utils.config import Config
import pytest


@pytest.mark.skip("momentaneo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Checkout")
@allure.story("Validar funcionalidades de la pagina de checkout")
def test_ir_a_checkout(carrito_con_item):
    """
    test para comprobar el acceso correcto a la pagina checkout

    """
    titulo_pagina = "Finalizar Compra - Puro Brote"
    # arranque
    checkout_page = CheckoutPage(carrito_con_item)

    # actions
    with allure.step("Ingreso a checkout page"):
        checkout_page.ir_a_checkout()
        titulo = checkout_page.return_titulo_checkout()

    # Assert
    with allure.step("validar title de pagina"):
        assert titulo == titulo_pagina, f"Mensaje erroneo {titulo}"


@pytest.mark.skip("momentaneo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Checkout")
@allure.story("Validar funcionalidades de la pagina de checkout")
def test_completar_formulario_checkout(carrito_con_item):
    """
    test para completar el formulario de checkout

    """
    # arranque
    checkout_page = CheckoutPage(carrito_con_item)

    # actions
    with allure.step("Ingreso a checkout page"):
        checkout_page.ir_a_checkout()

    with allure.step("Completo el formulario de checkout"):
        checkout_page.completar_formulario_checkout()

    with allure.step("Seleccionar Flow como metodo de pago"):
        checkout_page.seleccionar_flow()

    # Assert
    with allure.step("validar completitud de formulario"):
        assert (
            checkout_page.validar_generacion_qr() is True
        ), "No se genero el QR de Flow"


def test_cancelar_flow_checkout(carrito_con_item):
    """
    test para cancelar el flow de pago

    """
    # arranque
    checkout_page = CheckoutPage(carrito_con_item)

    # actions
    with allure.step("Ingreso a checkout page"):
        checkout_page.ir_a_checkout()

    with allure.step("Completo el formulario de checkout"):
        checkout_page.completar_formulario_checkout()

    # with allure.step("Seleccionar Flow como metodo de pago"):
    #    checkout_page.seleccionar_flow()

    with allure.step("Cancelar flow de pago"):
        checkout_page.cancelar_flow()

    # Assert
    with allure.step("validar cancelacion de flow"):
        assert (
            checkout_page.Mensaje_confirmacion() == "¿Deseas cancelar el pedido?"
        ), "No se visualiza el mensaje de confirmacion de cancelacion"

    with allure.step("confirmacion de cancelacion de pedido"):
        checkout_page.confirmar_cancelacion()

    with allure.step("validar mensaje de confirmacion de cancelacion"):
        assert (
            checkout_page.mensaje_confirmacion_cancelacion() == "Pedido cancelado"
        ), "No se redirigio correctamente"
