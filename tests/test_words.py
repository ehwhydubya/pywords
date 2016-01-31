import pytest

def test_setprettyprint_invalid_option(word):
    with pytest.raises(ValueError) as excinfo:
        word.setPrettyPrint('nope')
    assert 'Please enter a valid input' in str(excinfo.value)

def test_results_in_word(word):
    key = 'results'
    response = word.word('soliloquy')
    assert key in response

def test_invalid_entries_on_get(word):
    with pytest.raises(ValueError) as excinfo:
        response = word._get(12345, 'definitions')
    assert 'You must enter a valid string' in str(excinfo.value)

def test_query_in_search_single_param(word):
    key = 'query'
    response = word.search(letters=6)
    assert key in response

def test_query_in_search_multiple_params(word):
    key = 'query'
    response = word.search(letters=7, partOfSpeech='verb')
    assert key in response
