import pytest
from tests.pages.login_page import LoginPage
from tests.pages.dashboard import DashboardPage
from utils.config import Config
import allure


def test_ir_al_login(page):
    """
    test para comprobar el acceso correcto a la pagina de login

    """
    # arranque
    login_page = LoginPage(page)

    # actions
    with allure.step("Ingreso a login page"):
        login_page.Ir_a_login()

    # Assert
    with allure.step("validar title de pagina"):
        assert login_page.validar_titulo()


def test_ingresar_usuario(page):
    # arranque

    login_page = LoginPage(page)
    dashboard = DashboardPage(page)

    # action
    with allure.step("Ingreso a login page"):
        login_page.Ir_a_login()
    with allure.step("ingreso a dashboard"):
        login_page.ingresar_cliente()
        titulo = dashboard.return_titulo_bienvenida()
    # Assert
    with allure.step("validacion de mensaje de bienvenida"):
        assert (
            dashboard.validar_mensaje_bienvenida_cliente() is True
        ), f"Mensaje erroneo {titulo}"
