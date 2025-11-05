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

    # action
    with allure.step("Ingreso a login page"):
        login_page.Ir_a_login()
    with allure.step("ingreso a cliente/dashboard"):
        login_page.ingresar_cliente_login()
    # Assert
    with allure.step("validacion de ingreso a dashboard"):
        login_page.validar_ingreso_cliente_a_dashboard(
            "cliente/dashboard"
        ), "No se pudo ingresar al dashboard del cliente"


@pytest.mark.skip("momentaneo")
def test_restablecer_contrasena_cliente(page):
    # arranque
    login_page = LoginPage(page)
    # action
    with allure.step("Ingreso a pantalla login"):
        login_page.Ir_a_login()
    with allure.step("accion de restablecimiento de contraseña para un cliente"):
        login_page.restablecer_contrasena()
    # Assert
    with allure.step("validacion de mensaje de confirmacion"):
        assert (
            login_page.mensaje_confirmacion_restablecer_contasena()
            == "Contraseña restablecida"
        ), "No se pudo realizar el cambio de contraseña"


def test_volver_a_la_tienda_desde_login(page):
    # arranque
    login_page = LoginPage(page)
    # action
    with allure.step("Ingreso a pantalla login"):
        login_page.Ir_a_login()
    with allure.step("volver a la tienda desde login"):
        login_page.seguir_comprando()
    # Assert
    with allure.step("validacion de redireccion a la tienda"):
        assert page.url == Config.url_staging, "No se pudo volver a la tienda"


def test_cancelar_restablecer_contrasena(page):
    # arranque
    login_page = LoginPage(page)
    # action
    with allure.step("Ingreso a pantalla login"):
        login_page.Ir_a_login()
    with allure.step("abrir y cancelar restablecimiento de contraseña"):
        login_page.ir_a_restablecer_contrasena()
    # asert
    with allure.step("validacion de apertura de ventana de restablecimiento"):
        assert (
            login_page.ventana_restablecer_contrasena_visible()
        ), "No se pudo abrir la ventana de restablecimiento"
        login_page.cancelar_restablecer_contrasena()
    # accion
    with allure.step("cerrar ventana de restablecimiento de contraseña"):
        login_page.cancelar_restablecer_contrasena()
    # asert
    with allure.step("validacion de cierre de ventana de restablecimiento"):
        assert (
            login_page.ventana_restablecer_contrasena_no_visible()
        ), "No se pudo cerrar la ventana de restablecimiento"
