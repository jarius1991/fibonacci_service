from django.test import SimpleTestCase
from django.shortcuts import reverse


# Create your tests here.


class FibonacciTest(SimpleTestCase):

    def test_fibbonaci_url_valid(self):
        response = self.client.get("/fib/5")
        self.assertEqual(response.status_code, 200)

    def test_fibonacci_url_reverse_valid(self):
        response = self.client.get(reverse("fibonacci:index_value", kwargs={"index": 5}))
        self.assertEqual(response.status_code, 200)
