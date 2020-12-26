import time
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer page
    lnk_customers_menu_xpath = "//a[@href='#']/span[.='Customers']"
    lnk_customers_menu_item_xpath = "//span[@class='menu-item-title'][.='Customers']"
    btn_add_new_xpath = "//a[@class='btn bg-blue']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_customer_roles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lst_item_administrators_xpath = "//li[contains(text(),'Administrators')]"
    lst_item_registered_xpath = "//li[contains(text(),'Registered')]"
    lst_item_guests_xpath = "//li[contains(text(),'Guests')]"
    lst_item_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_mgr_of_vendor_xpath = "//*[@id='VendorId']"
    rd_male_gender_id = "Gender_Male"
    rd_female_gender_id = "Gender_Female"
    txt_first_name_xpath = "//input[@id='FirstName']"
    txt_last_name_xpath = "//input[@id='LastName']"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    txt_admin_content_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customers_menu(self):
        self.driver.find_element_by_xpath(self.lnk_customers_menu_xpath).click()

    def click_on_customers_menu_item(self):
        self.driver.find_element_by_xpath(self.lnk_customers_menu_item_xpath).click()

    def click_on_add_new(self):
        self.driver.find_element_by_xpath(self.btn_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def set_customer_roles(self, role):
        self.driver.find_element_by_xpath(self.txt_customer_roles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.list_item = self.driver.find_element_by_xpath(self.lst_item_registered_xpath)
        elif role == 'Administrators':
            self.list_item = self.driver.find_element_by_xpath(self.lst_item_administrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_item = self.driver.find_element_by_xpath(self.lst_item_guests_xpath)
        elif role == 'Vendors':
            self.list_item = self.driver.find_element_by_xpath(self.lst_item_vendors_xpath)
        else:
            self.list_item = self.driver.find_element_by_xpath(self.lst_item_guests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drp_mgr_of_vendor_xpath))
        drp.select_by_visible_text(value)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rd_male_gender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rd_female_gender_id).click()
        else:
            self.driver.find_element_by_id(self.rd_male_gender_id).click()

    def set_first_name(self, fname):
        self.driver.find_element_by_xpath(self.txt_first_name_xpath).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element_by_xpath(self.txt_last_name_xpath).send_keys(lname)

    def set_dob(self, dob):
        self.driver.find_element_by_xpath(self.txt_dob_xpath).send_keys(dob)

    def set_company_name(self, comname):
        self.driver.find_element_by_xpath(self.txt_company_name_xpath).send_keys(comname)

    def set_admin_content(self, content):
        self.driver.find_element_by_xpath(self.txt_admin_content_xpath).send_keys(content)

    def click_on_save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
