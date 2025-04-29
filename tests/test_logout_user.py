from playwright.sync_api import Page
import pytest

def test_loginUser(page: Page):
    page.goto('http://automationexercise.com')
    login_btn = page.wait_for_selector('a[href="/login"]').click() # Entre na aba login
    adiciona_login = page.wait_for_selector('input[type="email"]').type("jean@50508080") # Adiciona login
    adiciona_senha = page.wait_for_selector('input[type="password"]').type("jean@50508080") # Adiciona Senha
    botao_login = page.wait_for_selector('button[type="submit"]').click() # Verifica login
    logout_btn = page.wait_for_selector('a[href="/logout"]').click()

    try:
        login_btn = page.wait_for_selector('a[href="/login"]', timeout=3000)
        assert login_btn.is_visible(), "Botão de login visível"
    except:
        pytest.fail("Logout não foi bem-sucedido - botão de logout encontrado.")
