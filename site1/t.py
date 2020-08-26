from django.test import TestCase

from django.test import Client

#find_element_by_id
#find_element_by_name
#find_element_by_xpath
#find_element_by_link_text
#find_element_by_partial_link_text
#find_element_by_tag_name
#find_element_by_class_name
#find_element_by_css_selector

import sys, os
#sys.path.append(os.getcwd())
#sys.path += ["whatever"]
#print(sys.path)

pwd = os.getcwd()
#set_path = "export PATH=$PATH:"+pwd
#os.system(set_path)
#os.system("echo $PATH")
#print(sys.path)

os.environ["PATH"] += ":" + pwd
print(os.environ["PATH"])

#from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver

#class MySeleniumTests(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

#    @classmethod
#    def setUpClass(cls):
#        super().setUpClass()
#        cls.selenium = WebDriver()
#        cls.selenium.implicitly_wait(10)

#    @classmethod
#    def tearDownClass(cls):
#        cls.selenium.quit()
#        super().tearDownClass()
#
#    def test_introduction_get(self):
        #self.selenium.get('%s%s' % (self.live_server_url, '/posts/introduction-get/'))
        #send1 = self.selenium.find_element_by_id("send1")
        #print(send1)
        #send1.click()

        #listOfElements = self.selenium.findElements(By.xpath("//div"));
        #username_input = self.selenium.find_element_by_name("username")
        #username_input.send_keys('myuser')
        #password_input = self.selenium.find_element_by_name("password")
        #password_input.send_keys('secret')
        #self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
#        pass


class TestTree(TestCase):

    #modify this
    def test_if_tree_not_empty(self):
        c = Client()
        #response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        #response.status_code
        response = c.get('/tree/')
        print(response.content)
        self.assertEqual(response.status_code, 200)
