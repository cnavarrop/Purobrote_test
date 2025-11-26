import pytest
from playwright.sync_api import sync_playwright
from tests.pages.index_page import IndexPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args
        # "storage_state": "auth.json",  # Opcional: para persistir sesión
    }


@pytest.fixture
def shared_page(page):
    # Usar la misma página entre tests
    yield page


@pytest.fixture
def carrito_con_item(page):
    index_page = IndexPage(page)
    index_page.ir_a_index()
    index_page.agregar_producto_al_carrito()
    yield page
