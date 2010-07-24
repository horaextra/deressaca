#coding:utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse

class TestCounterView(TestCase):

    def test_counter_redirects_to_counter_template(self):
        response = self.client.get(reverse('counter'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_counter_is_zero_when_there_is_no_hangover(self):
        response = self.client.get(reverse('counter'))
        self.assertEquals(response.context['hangovers'], 0)

