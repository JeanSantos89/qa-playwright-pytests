from playwright.sync_api import Page
import pytest

def test_loginUser(page: Page):
    page.goto('http://automationexercise.com')
    page.wait_for_selector('a[href="/login"]').click() # Entre na aba login
    cadastra_login = page.wait_for_selector('input[data-qa="signup-name"]').type("jean") # Adiciona nome 
    cadastra_senha = page.wait_for_selector('input[data-qa="signup-email"]').type("jean@50508080") # Adiciona email existente
    signup_btn = page.wait_for_selector('button[data-qa="signup-button"]').click() # Tenta criar conta

    try:
        erro = page.wait_for_selector('p:has-text("Email Address already exist!")', timeout=3000)
        assert erro.is_visible()
    except TimeoutError:
        pytest.fail("Avança para proxima página mesmo com email existente")
