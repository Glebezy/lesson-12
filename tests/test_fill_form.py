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
class TestFillForm:
    def test_success_fill_form(self):
        steps = Steps()
        steps.open_form()
        steps.fill_form()
        steps.check_registration()


class Steps:
    @allure.step("Open Repo link")
    def open_form(self, registration_page):
        registration_page.open()

    @allure.step("Fill form")
    def fill_form(self, registration_page, user):
        registration_page.register(user)

    @allure.step("Check success registration")
    def check_registration(self, registration_page, user):
        registration_page.should_have_registered(user)