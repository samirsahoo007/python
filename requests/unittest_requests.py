import requests
import requests_mock
import unittest2

class MyTestSuite(unittest2.TestCase):
  def test_my_api(self):
    session = requests.Session()
    with requests_mock.mock() as m:
        m.get('http://test.com/test', text='data')
        response = session.request('http://test.com/test')
    self.assertEqual(response.body, 'data')

