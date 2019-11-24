from django.test import SimpleTestCase
from django.shortcuts import reverse


class FibonacciTest(SimpleTestCase):

    def test_url_valid(self):
        response = self.client.get("/fib/5")
        self.assertEqual(response.status_code, 200)

    def test_url_reverse_valid(self):
        response = self.client.get(reverse("fibonacci:index_value", kwargs={"index": 5}))
        self.assertEqual(response.status_code, 200)

    def test_proper_response(self):
        """
        Cleaner way of providing test parameters is in pytest.mark.parametrize decorator. I used default test tool
        builded in Django.
        """
        correct_input_response_values = {
            0: b'0',
            1: b'1',
            2: b'1',
            3: b'2',
            4: b'3',
            5: b'5',
            6: b'8',
            7: b'13',
            8: b'21',
            9: b'34',
            10: b'55',
        }
        for index, response in correct_input_response_values.items():
            current_response = self.client.get(reverse("fibonacci:index_value", kwargs={"index": index}))
            self.assertEqual(current_response.status_code, 200)
            self.assertEqual(current_response.content, response)

    def test_invalid_input_data(self):
        invalid_index = ['-1', '-10', 'ss']
        for index in invalid_index:
            current_response = self.client.get('fib/' + index)
            self.assertEqual(current_response.status_code, 404)
