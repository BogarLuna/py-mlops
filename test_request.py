from request_hello import get_web_data

def test_request_hello():
    assert get_web_data('https://openlibrary.org/search.json')!=None