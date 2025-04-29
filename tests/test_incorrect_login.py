from playwright.sync_api import Page
import pytest

def test_loginUser(page: Page):
    page.goto('http://automationexercise.com')
    page.wait_for_selector('a[href="/login"]').click() # Entre na aba login
    adiciona_login = page.wait_for_selector('input[type="email"]').type("jean@50508080") # Adiciona login
    adiciona_senha = page.wait_for_selector('input[type="password"]').type("jean@50508080") # Adiciona Senha
    botao_login = page.wait_for_selector('button[type="submit"]').click() # Verifica login

    try:
        erro = page.wait_for_selector('p:has-text("Your email or password is incorrect!")', timeout=3000)
        assert erro.is_visible()
    except TimeoutError:
        pytest.fail("Mensagem de erro de login não foi apresentada")

    