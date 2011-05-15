from django.test import TestCase

class indexURLTest(TestCase):
    def test_sucess_when_get_index(self):
    	response = self.client.get('/')	
    	self.assertEquals(200, response.status_code)
    	self.assertTemplateUsed(response, 'index.html')
