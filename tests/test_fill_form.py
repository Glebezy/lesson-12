import allure
import pytest
from models.users import User
from pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page():
    return RegistrationPage()


@pytest.fixture
def user():
    return User("John", "Doe", "gte@mail.com", "Male", "1234567890",
                "7 August,2023", ["English", "Math"], ["Sports", "Music"],
                "pic.jpeg", "123 Main St, Haryana Karnal")


@allure.title("Проверка регистрации студента")
@allure.description("Заполнение всех полей в форме регистрации")
@allure.tag("UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Gleb T")
@allure.link("https://demoqa.com/", name="Website")
@allure.issue("ISSUE-123")
@allure.testcase("TMS-457")
def test_success_fill_form(setup_browser, registration_page):
    with allure.step("Open browser"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.register(user)
    with allure.step("Check registration"):
        registration_page.should_have_registered(user)