from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin001:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    def test_home_page_title(self, setup):
        self.logger.info("******** TestLogin001 ********")
        self.logger.info("******** Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login1":
            self.logger.info("******** Home Page Title test is passed ********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******** Home Page Title test is failed ********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("******** TestLogin001 ********")
        self.logger.info("******** Verifying Login test ********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("******** Login test is passed ********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******** Login test is failed ********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
