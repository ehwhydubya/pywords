import os
import pytest
import words

@pytest.fixture(scope='module')
def word():
    return words.Words(os.environ['MASHAPE_TOKEN'])
