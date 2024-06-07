from test_contr import *

@pytest.mark.smoke
def test_login(page: Page, login):
    login()

@pytest.mark.smoke
def test_logout(page: Page, logout):
    logout()
