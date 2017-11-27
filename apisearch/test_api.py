import unittest
import json
import api


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        print("\n==> Setting up the env for tests!")
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        print("==> Tearing down after tests!")

    def test_search_OK(self):
        print("Running: test_search OK")
        resp = self.app.get('/search', data=dict(
            search="stars with vmag > 0",
        ))
        assert "200 OK" == resp.status
        assert "url" in json.loads(resp.data)

    def test_search_empty_NOOK(self):
        print("Running: test_search NOOK")
        resp = self.app.get('/search', data=dict(
            search="",
        ))
        assert "400 BAD REQUEST" == resp.status

    def test_search_wrong_value_NOOK(self):
        print("Running: test_search NOOK")
        resp = self.app.get('/search', data=dict(
            search="adflkadjflkajfka adfa",
        ))
        assert "400 BAD REQUEST" == resp.status

    def test_url_request_OK(self):
        print("Running: test_url OK")
        resp = self.app.get('/search', data=dict(
            search="stars with vmag > 0"
        ))
        my_url = json.loads(resp.data)['url']
        my_url = my_url.split("?")[1]

        new_resp = self.app.get('/url?{}'.format(my_url))
        assert "200 OK" == new_resp.status

    def test_url_request_multi_OK(self):
        print("Running: test_url_multi OK")
        resp = self.app.get('/search', data=dict(
            search="stars, galaxies with mes = jpl+flux_v, redshift <= 0.01 and plx >= 2"
        ))
        my_url = json.loads(resp.data)['url']
        my_url = my_url.split("?")[1]

        new_resp = self.app.get('/url?{}'.format(my_url))
        assert "200 OK" == new_resp.status


if __name__ == '__main__':
    unittest.main()