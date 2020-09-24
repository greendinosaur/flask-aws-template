
from flask_testing import LiveServerTestCase
from selenium import webdriver

from app import create_app, db
from app.models import User

test_user_username = "my_test_user"
test_user_email = "test@test.email"
test_user_password = "test_pwd"


class TestBase(LiveServerTestCase):

    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--window-size=2000,1080')  # need a large display so navbar shows correctly under headless

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.get_server_url())

        db.drop_all()
        db.create_all()

        user = User(username=test_user_username, email=test_user_email)
        user.set_password(test_user_password)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        self.driver.quit()

    def login_user(self):
        self.driver.get(self.get_server_url() + "/auth/login")
        self.driver.find_element_by_id("username").send_keys(test_user_username)
        self.driver.find_element_by_id("password").send_keys(
            test_user_password)
        self.driver.find_element_by_id("submit").click()


class TestLogin(TestBase):

    def test_login_ok(self):
        # Fill in login form
        self.driver.get(self.get_server_url() + "/auth/login")
        self.driver.find_element_by_id("username").send_keys(test_user_username)
        self.driver.find_element_by_id("password").send_keys(
            test_user_password)
        self.driver.find_element_by_id("submit").click()

        # Assert that username is shown
        username_navbar = self.driver.find_element_by_id(
            "navbarDropdownMenuLink").text
        assert test_user_username in username_navbar


class TestContactUs(TestBase):

    def test_contact_us_not_logged_in(self):
        self.driver.find_element_by_id("contact_us_link").click()

        self.driver.find_element_by_id("name").send_keys(
            "Bobby Chariot")
        self.driver.find_element_by_id("email").send_keys(
            "myemail@email.com")
        self.driver.find_element_by_id("message").send_keys(
            "I just wanted to say hello")

        self.driver.find_element_by_id("send_message").click()
        success_message = self.driver.find_element_by_class_name("alert-success").text

        assert "Thank you for sending us a note" in success_message

    def test_contact_us_logged_in(self):
        self.login_user()
        self.driver.find_element_by_id("contact_us_link").click()

        assert test_user_username in self.driver.find_element_by_id("name").get_attribute("value")
        assert test_user_email in self.driver.find_element_by_id("email").get_attribute("value")

        self.driver.find_element_by_id("message").send_keys(
            "I just wanted to say hello")

        self.driver.find_element_by_id("send_message").click()
        success_message = self.driver.find_element_by_class_name("alert-success").text
        assert "Thank you for sending us a note" in success_message

    def test_contact_us_invalid_data(self):
        self.driver.find_element_by_id("contact_us_link").click()
        self.driver.find_element_by_id("send_message").click()

        error_message = self.driver.find_element_by_class_name("text-muted").text
        assert "This field is required" in error_message
