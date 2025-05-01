from playwright.sync_api import Page
import pytest

def test_loginUser(page: Page):
    page.goto('http://automationexercise.com')
    page.wait_for_selector('a[href="/login"]').click() # Entre na aba login
    adiciona_login = page.wait_for_selector('input[type="email"]').type("jean@50508080") # Adiciona login
    adiciona_senha = page.wait_for_selector('input[type="password"]').type("jean@50508080") # Adiciona Senha
    botao_login = page.wait_for_selector('button[type="submit"]').click() # Verifica login

        # Verifica se o login foi bem-sucedido procurando o botão de logout
    try:
        logout_btn = page.wait_for_selector('a[href="/logout"]', timeout=5000)
        assert logout_btn.is_visible(), "Botão de logout não visível -  login pode ter falhado."
    except:
        pytest.fail("Login não foi bem-sucedido - botão de logout não encontrado.")
