import unittest
from search import query_api, is_url_valid

class QueryTestCase(unittest.TestCase):

    def setUp(self):
        print("==> Setting up the env for tests!")

    def tearDown(self):
        print("==> Tearing down after tests!")

    def test_physical_with_criteria(self):
        assert query_api("stars with vmag > 0") == \
               'http://api.skywatch.co/?types=star&vmag=gt0'

    def test_only_physical(self):
        assert query_api(
            "stars, galaxies and interstellar matter") == \
               'http://api.skywatch.co/?types=star+galaxy+interstellar_matter'

    def test_physical_with_multiple_criteria(self):
        assert query_api("galaxies with redshift > 0.001, plx < 1 and mes = jpl+flux_v") == \
               'http://api.skywatch.co/?types=galaxy&redshift=gt0.001&plx=lt1&mes=jpl+flux_v'

    def test_only_criteria(self):
        assert query_api("redshift > 0.001, plx < 1 and mes = jpl+flux_v") == \
               'http://api.skywatch.co/?redshift=gt0.001&plx=lt1&mes=jpl+flux_v'

    def test_physical_criteria_unordered(self):
        assert query_api("stars, redshift > 0.001, galaxies") == \
               'http://api.skywatch.co/?types=star+galaxy&redshift=gt0.001'

    def test_mult_physical_with_mult_criteria(self):
        assert query_api("stars, galaxies with mes = jpl+flux_v, redshift <= 0.01 and plx >= 2") == \
               'http://api.skywatch.co/?types=star+galaxy&mes=jpl+flux_v&redshift=lte0.01&plx=gte2'

    def test_url_valid(self):
        url_ok = 'http://api.skywatch.co/?types=star+galaxy+interstellar_matter'
        url_from_query = query_api("stars, galaxies and interstellar matter")
        assert url_from_query == url_ok
        assert is_url_valid(url_from_query)
        assert is_url_valid(url_ok)

    def test_url_not_valid(self):
        url_not_ok = 'http://api.skywatch.cotypes=star+galaxy+interstellar_matter'
        assert not is_url_valid(url_not_ok)


if __name__ == '__main__':
    unittest.main()


