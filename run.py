#import junit_xml
import HTMLTestRunner
import unittest

from Odoo_testing_0_Login import Odoo_testing_0_Login
from Odoo_testing_1_Menu import Odoo_testing_1_Menu
from Odoo_testing_2_Personas import Odoo_testing_2_Personas

odoo_test_0 = unittest.TestLoader().loadTestsFromTestCase(Odoo_testing_0_Login)
odoo_test_1 = unittest.TestLoader().loadTestsFromTestCase(Odoo_testing_1_Menu)
odoo_test_2 = unittest.TestLoader().loadTestsFromTestCase(Odoo_testing_2_Personas)

final_tests = unittest.TestSuite([odoo_test_0, odoo_test_1, odoo_test_2])

#unittest.TextTestRunner().run(final_tests)


outfile = open("OdooTestReport.html", "w")
#configure HTMLTestRunner options

runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title="Tests Report", description="Tests")
runner.run(final_tests)


