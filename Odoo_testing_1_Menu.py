# -*- coding: utf-8 -*-
# from selenium.webdriver.support import
import time
import unittest
from __builtin__ import classmethod

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Odoo_testing_1_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://erp.pre.basetis.com/web/database/selector")
        cls.driver.implicitly_wait(5)

    def test_login(self):
        self.db_var=self.driver.find_element_by_id("db")
        temp_t=''.join(self.db_var.text)
        temp_db_x=temp_t.split()
        Select(self.db_var).select_by_visible_text(temp_db_x[0])
        time.sleep(5)
        self.driver.find_element_by_id("password").send_keys("1Upv0Nkp")
        self.driver.find_element_by_id("login").send_keys("javier.cardaba@basetis.com")
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(5)
        test_wodr = self.driver.find_elements_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[2]/li/a/span")
        # self.assertTrue(test_wodr[0].text)
        if self.assertTrue(test_wodr[0].text):
            self.name = u'Javier C\xe1rdaba Mart\xednez'
            self.assertEqual(self.name, test_wodr[0].text)

    def test_menu(self):
        for i in range(1,14):
            self.driver.find_element_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[1]/li["+str(i)+"]/a/span").click()
            time.sleep(15)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# cls.assertEqual([], cls.verificationErrors)

#    def is_element_present(self, how, what):
#        try: self.driver.find_element(by=how, value=what)
#        except NoSuchElementException as e: return False
#        return True
#
#    def close_alert_and_get_its_text(self):
#        try:
#            alert = self.driver.switch_to_alert()
#            alert_text = alert.text
#            if self.accept_next_alert:
#                alert.accept()
#            else:
#                alert.dismiss()
#            return alert_text
#        finally: self.accept_next_alert = True
#
#    def is_alert_present(self):
#        try: self.driver.switch_to_alert()
#        except NoAlertPresentException as e: return False
#        return True

if __name__ == "__main__":
    unittest.main()
