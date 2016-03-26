# -*- coding: utf-8 -*-
import calendar
import psycopg2
import time
import unittest
from __builtin__ import classmethod
from  datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date,timedelta

class Odoo_testing_3_horas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #cls.driver.get("https://erp.pre.basetis.com/web/database/selector")
        cls.driver.get("http://127.0.0.1:8069/web/database/selector")
        cls.driver.implicitly_wait(5)

    def test_0_login(self):
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

    def db_names(self):
        conn = None
        db_name_real = []
        db_names_res = ['template0', 'template', 'template1', 'postgres']
        try:
            conn = psycopg2.connect("dbname='postgres' user='odoo' password='Cnjnhb103'")
        except:
            print "Cant connect to database  1"

        cur = conn.cursor()
        cur.execute("""SELECT datname from pg_database""")

        for row in cur:
            if row[0] not in db_names_res:
                db_name_real.append(row[0])
        conn.close()
        return db_name_real

    def days_total(self):
        month = datetime.now().month
        year = datetime.now().year
        days_in_month = calendar.monthrange(year, month)[1]
        conn = None
        days_f = []
        month_f = []
        days_fest = []
        days_of_work = []
        days_total = []
        db_name=self.db_names()[1]

        try:
            conn = psycopg2.connect("dbname='%s' user='odoo' host='localhost' password='odoo'" % str(db_name))
        except:
            print "Failed to connect to database  2 - "
        cur = conn.cursor()
        cur.execute("""SELECT date FROM hr_holidays_public WHERE employee_category_id = 4 ORDER BY 1""")

        for i in cur:
            days_f.append(i[0])
        for j in range(0,len(days_f)):
            if days_f[j].month == month:
                 month_f.append(days_f[j])
        for i in range(0, len(month_f)):
            days_fest.append(month_f[i].day)
        conn.close()


        fromdate = date(year,month, 1)
        todate = date(year,month,days_in_month)
        daygenerator = (fromdate + timedelta(x)
        for x in range((todate - fromdate).days + 1))
        for day in daygenerator:
            if day.weekday() < 5:
                days_of_work.append(day.day)
        for i in days_of_work:
            if i not in days_fest:
                days_total.append(i)
        return days_total

    def test_1_horas(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[1]/li[9]/a/span").click()
        #for i in range(0,14):
        #    self.text_of=self.driver.find_element_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[1]/li["+str(i)+"]/a/span")
        #    temp_n=''.join(self.text_of.text)
        #    if temp_n == "Personas":
        #        print temp_n
        #        self.text_of.click()
        time.sleep(5)
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[1]/div/div[1]/div/div/div[9]/ul[3]/li[1]/a/span").click()
        time.sleep(5)
        self.t_word=self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr[1]/td[1]/label")
        time.sleep(5)
        self.assertEqual("Periodo del parte de horas", self.t_word.text )
        time.sleep(10)

    def test_2_partes_de_horas(self):
        days_of_work = self.days_total()




        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/div[2]/div[1]/button").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/table[2]/tbody/tr[2]/td/span/div/input").send_keys("erp")
        time.sleep(10)
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/ul[4]/li[1]/a").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/table[2]/tbody/tr[2]/td/div/button").click()
        time.sleep(10)

        for i in days_of_work:
            self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/table[2]/tbody/tr[2]/td["+str(i+2)+"]/input").click()
            self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/table[2]/tbody/tr[2]/td["+str(i+2)+"]/input").clear()
            self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/table[2]/tbody/tr[2]/td["+str(i+2)+"]/input").send_keys(8)
            time.sleep(10)
        #self.assertEqual("88:00", self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/table[2]/tbody/tr[2]/td[34]").text)
        self.driver.find_element_by_xpath("html/body/div[1]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td[1]/div/div/span[2]/button").click()
        time.sleep(15)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
