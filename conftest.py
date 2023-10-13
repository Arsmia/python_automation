import pytest

import random


@pytest.fixture
def teardown():
    yield
    print("do something")

@pytest.fixture(scope="session")
def browser():
    print("Open browser")
    yield random.randint(0, 100)
    print("Close browser")

