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
        self.assertEquals(response.context['hangovers'], '0000')

    def test_post_inc_counter_when_is_hungover(self):
        response = self.client.post(
            reverse('counter'),
            {'new_hangover':1}
        )
        hangovers = Hangover.objects.count()
        self.assertEquals(hangovers, 1)

    def test_post_inc_counter_when_more_than_one_hungover(self):
        response = self.client.post(
            reverse('counter'),
            {'new_hangover':1}
        )
        response = self.client.post(
            reverse('counter'),
            {'new_hangover':1}
        )
        hangovers = Hangover.objects.count()
        self.assertEquals(hangovers, 2)

    def _test_get_counter_is_one_after_one_new_hangover(self):
        response = self.client.post(
            reverse('counter'),
            {'new_hangover':1}
        )
        response = self.client.get(reverse('counter'))
        self.assertEquals(response.context['hangovers'], '0001')

    def test_redirect_when_post_new_hangover(self):
        twitter_url = 'http://twitter.com/?status=Eu%20tamb%C3%A9m%20estou%20#deressaca!'
        response = self.client.post(
            reverse('counter'),
            {'new_hangover':1}
        )
        self.assertRedirects(response, twitter_url)

    def test_redirects_to_counter_page_when_post_is_malformed(self):
        response = self.client.post(
            reverse('counter'),
            {'wrong':1}
        )
        self.assertRedirects(response, reverse('counter'))

