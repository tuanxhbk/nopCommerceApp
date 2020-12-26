from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class TestLoginDDT002:
    baseUrl = ReadConfig.get_application_url()
    path = ".//TestData//LoginData.xlsx"
    sheet = 'Sheet1'

    logger = LogGen.log_gen()

    def test_login_ddt(self, setup):
        self.logger.info("******** TestLoginDDT002 ********")
        self.logger.info("******** Verifying Login DDT test ********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)

        self.row = XLUtils.get_row_count(self.path, self.sheet)
        print("Number of Rows in an Excel: ", self.row)

        lst_status = []

        for r in range(2, self.row+1):
            self.username = XLUtils.read_data(file=self.path, sheet_name=self.sheet, row_no=r, column_no=1)
            self.password = XLUtils.read_data(file=self.path, sheet_name=self.sheet, row_no=r, column_no=2)
            self.exp = XLUtils.read_data(file=self.path, sheet_name=self.sheet, row_no=r, column_no=3)

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("******** Login test is passed ********")
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("******** Login test is failed ********")
                    self.lp.click_logout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("******** Login test is failed ********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******** Login test is passed ********")
                    lst_status.append("Pass")
        self.driver.close()

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed....")
            assert True
        else:
            self.logger.info("Login DDT test failed....")
            assert False

        self.logger.info("******** TestLoginDDT002 ********")
        self.logger.info("******** Finished Login DDT test ********")