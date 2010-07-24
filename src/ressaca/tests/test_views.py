#coding:utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse

from ressaca.models import Hangover

class TestCounterView(TestCase):

    def test_counter_redirects_to_counter_template(self):
        response = self.client.get(reverse('counter'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_counter_is_zero_when_there_is_no_hangover(self):
        response = self.client.get(reverse('counter'))
        self.assertEquals(response.context['hangovers'], 0)

    def test_post_inc_counter_when_is_hungover(self):
        response = self.client.post(
            reverse('counter'),
            {'new_hangover':1}
        )
        hangover = Hangover.objects.all()
        self.assertTrue(hangover)
        self.assertEquals(hangover[0].counter, 1)

