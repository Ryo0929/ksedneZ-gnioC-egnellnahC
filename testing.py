import unittest
import pandas as pd
from model import *
from unittest import mock

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.text = json_data
            self.status_code = status_code

    if args[0] == 'https://zccryo.zendesk.com/api/v2/tickets.json':
        return MockResponse('{"tickets":[{"key1": "value1"}]}', 200)
    if args[0] == 'https://others.zendesk.com/api/v2/tickets.json':
        return MockResponse('{"not_tickets":[{"key1": "value1"}]}', 200)

    return MockResponse(None, 404)

@mock.patch('requests.get', side_effect=mocked_requests_get)
class TestModel(unittest.TestCase):
    def test_fetch_data_success(self, mock_get):
        correct_url='zccryo'
        result=get_data(correct_url,"acc","pwd")
        self.assertTrue(isinstance(result, pd.DataFrame))

    def test_fetch_data_fail(self, mock_get):
        incorrect_url="heeeee"
        result=get_data(incorrect_url,"acc","pwd")
        self.assertTrue(result is None)

    def test_fetch_data_invalid(self, mock_get):
        different_api_call="others"
        result=get_data(different_api_call,"acc","pwd")
        self.assertTrue(result is None)

if __name__ == '__main__':
    unittest.main()