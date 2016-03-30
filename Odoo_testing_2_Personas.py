# -*- coding: utf-8 -*-
# from selenium.webdriver.support import
import time
import unittest
from __builtin__ import classmethod

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Odoo_testing_2_Personas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://erp.pre.basetis.com/web/database/selector")
        cls.driver.implicitly_wait(30)
        cls.driver.implicitly_wait(5)

    def test_0_login(self):
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
        time.sleep(15)

    def test_1_add_person(self):
        self.driver.find_element_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[1]/li[9]/a/span").click()
        time.sleep(15)
        self.driver.find_element_by_css_selector("button.oe_kanban_button_new.oe_highlight").click()
        time.sleep(5)

        self.driver.find_element_by_id("oe-field-input-4").send_keys("Test_First_Name")
        self.driver.find_element_by_id("oe-field-input-5").send_keys("Test_Last_Name")
        self.driver.find_element_by_xpath(".//*[@id='notebook_page_11']/table[1]/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[2]/span/div/span[2]/img").click()
        time.sleep(2)
        self.driver.find_element_by_id("ui-id-26").click()
        self.driver.find_element_by_xpath(".//*[@id='notebook_page_11']/table[1]/tbody/tr[1]/td[2]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/span/div/span[2]/img").click()
        time.sleep(2)
        #self.driver.find_element_by_id("oe-field-input-24").click()
        #self.driver.find_element_by_id("oe-field-input-24").send_keys("Plan evaluación proyectos BaseTIS")
        self.driver.find_element_by_id("ui-id-30").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td[1]/div/div[2]/span[2]/button").click()

        #Verificaciones del User Data
        self.test_user_name=self.test_user=self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[4]/div/div[4]/div/div/div[1]/div/div[1]/span[1]/span")
        self.assertEqual("Test_First_Name",self.test_user_name.text)
        time.sleep(15)

    def test_2_del_person(self):
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td[2]/div/div/div/div[3]/button").click()
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td[2]/div/div/div/div[3]/ul/li[4]/a").click()
        time.sleep(1)
        alert=self.driver.switch_to_alert()
        alert_text=alert.text
        #self.assertEqual("Do you really want to delete this record?",alert_text)
        time.sleep(2)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
