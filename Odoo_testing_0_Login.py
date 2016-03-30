# -*- coding: utf-8 -*-
# from selenium.webdriver.support import
import time
import unittest
from __builtin__ import classmethod

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Odoo_testing_0_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://erp.pre.basetis.com/web/database/selector")
        cls.driver.implicitly_wait(5)

    def test_login(self):
        self.db_var=self.driver.find_element_by_id("db")
        temp_t=''.join(self.db_var.text)
        temp_db_x=temp_t.split()
        Select(self.db_var).select_by_visible_text(temp_db_x[1])
        time.sleep(5)
        self.driver.find_element_by_id("password").send_keys("1Upv0Nkp")
        self.driver.find_element_by_id("login").send_keys("javier.cardaba@basetis.com")
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(5)
        test_wodr = self.driver.find_elements_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[2]/li/a/span")
        if self.assertTrue(test_wodr[0].text):
            self.name = u'Javier C\xe1rdaba Mart\xednez'
            self.assertEqual(self.name, test_wodr[0].text)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
