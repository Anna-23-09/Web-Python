import pytest
from module import Site
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture
def add_post_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture
def add_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture
def add_description():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span'


@pytest.fixture
def add_content():
    return '//*[@id="create-item"]/div/div/div[3]/div/label'


@pytest.fixture
def save_post():
    return '//*[@id="create-item"]/div/div/div[7]/div/button/div'


@pytest.fixture
def check_title():
    return '//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2'
    # return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture
def title_name():
    return f"{testdata['title']}"


@pytest.fixture
def email_input():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture
def password_input():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture
def error():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture
def submit():
    return 'button'


@pytest.fixture
def error_result():
    return "401"


@pytest.fixture
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.close()
