"""Main module for tests."""
from pytest import raises
from unittest import mock

from scrabbler import scrabble_sentence, fetch_similar_words


def test_scrabble_sentence(mocker):
    """Test that the scrabble_sentence does what it should do."""
    mocker.patch('scrabbler.fetch_similar_words', return_value=['mocked'])
    assert scrabble_sentence('this is a valid sentence') == \
           'mocked mocked mocked mocked mocked'


def test_fetch_similar_words():
    mock_open = mock.mock_open(read_data='test1\ntest2\n')
    with mock.patch('builtins.open', mock_open):
        result = fetch_similar_words('test1')
    assert result == ['test1', 'test2']


def test_empty_sentence():
    """Test that an exception is raised if an empty string is passed in."""
    with raises(ValueError, match='word or sentence is empty of not valid!'):
        scrabble_sentence('')


def test_white_space():
    """Test that an exception is raised if a bunch of spaces is passed in."""
    with raises(ValueError, match='word or sentence is empty of not valid!'):
        scrabble_sentence('   ')
