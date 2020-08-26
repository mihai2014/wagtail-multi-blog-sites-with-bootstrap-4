from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests
from django.test import Client

from site1.models import Site1Index

class TestTree(WagtailPageTests):

    #modify this
#    def test_if_tree_not_empty(self):
        #c = Client()
        #response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        #response.status_code
        #response = c.get('/')
        #print(response.content)
        #self.assertEqual(response.status_code, 200)

#    def test_subpage(self):
        #response = self.client.get('tree')
        #print(response.content)
        #self.assertEqual(response.status_code, 200,
        #             'Request the open positions page')        

    def test_tree(self):
        Posts = Site1Index.objects.all()[0]       
        print(Posts)
        pass
