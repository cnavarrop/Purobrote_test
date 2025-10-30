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
        titulo = login_page.return_titulo_login()

    # Assert
    with allure.step("validar title de pagina"):
        assert titulo == "Admin Login", f"Mensaje erroneo {titulo}"


def test_ingresar_usuario(page):
    # arranque

    login_page = LoginPage(page)
    dashboard = DashboardPage(page)

    # action
    with allure.step("Ingreso a login page"):
        login_page.Ir_a_login()
    with allure.step("ingreso a dashboard"):
        login_page.ingresar_cliente_login()
        titulo = dashboard.return_titulo_bienvenida()
    # Assert
    with allure.step("validacion de mensaje de bienvenida"):
        assert titulo == Config.bienvenida_cliente, f"Mensaje erroneo {titulo}"
