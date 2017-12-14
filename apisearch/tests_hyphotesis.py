from hypothesis import given, reject, example
from hypothesis.strategies import integers, text
import unittest
from search import query_api


@given(text())
@example("")
def test_query_hypothesis_with_empty(query):
    print("running test_query_hyphotesis_for_query_api()")
    try:
        assert query_api(query) == ""
    except Exception as e:
        reject()


@given(text())
@example("stars with vmag > 0")
def test_query_hypothesis_with_real_url(query):
    print("running test_query_hyphotesis_for_query_api()")
    try:
        response =  query_api(query)
        if len(response) > 0:
            assert response == 'http://api.skywatch.co/?types=star&vmag=gt0'
        else:
            assert response == ""
    except Exception as e:
        reject()