import pytest, random

@pytest.fixture
def get_admin(browser, teardown):
    return random.randint(0, 100)

def simple_test(get_admin, browser):
    #assert get_admin == 5, "admin id expected 5"
    #assert browser == "Chrome"
    print(browser)
