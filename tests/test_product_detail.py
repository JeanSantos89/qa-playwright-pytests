from playwright.sync_api import Page
import pytest

def test_ProductDetail(page: Page):
    page.goto('http://automationexercise.com')
    products_btn = page.wait_for_selector('a[href="/products"]').click() # Entre na aba produtos
    primeiro_produto = page.wait_for_selector('a[href="/product_details/1"]').click() # Entra no primeiro produto disponível

    try: # Verifica a presença das informações necessárias
        availability = page.wait_for_selector('b:has-text("Availability")')
        condition = page.wait_for_selector('b:has-text("Condition")')
        brand = page.wait_for_selector('b:has-text("Brand")', timeout = 3000)
        assert availability.is_visible()
        assert condition.is_visible()
        assert brand.is_visible()
    except TimeoutError:
        pytest.fail("Não possui as informações no produto")