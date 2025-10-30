import pytest
from playwright.sync_api import sync_playwright


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
