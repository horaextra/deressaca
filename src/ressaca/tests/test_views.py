from django.test import TestCase
from django.core.urlresolvers import reverse

class TestCounterView(TestCase):

    def test_counter_redirects_to_counter_template(self):
        response = self.client.get(reverse('counter'))
        print 'hey'
