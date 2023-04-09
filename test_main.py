import unittest
from main import parse

class TestParse(unittest.TestCase):

    def test_parse1(self):
        assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret','color': 'purple'}
    def test_parse2(self):
        assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret','color': 'purple'}
    def test_parse3(self):
        assert parse('https://example.com/path/to/page?name=ferret&color=purple&style') == {'name': 'ferret', 'color': 'purple','style': ''}
    def test_parse4(self):
        assert parse('https://example.com/path/to/page?name=ferret&color=purple&style=') == {'name': 'ferret','color': 'purple','style': ''}
    def test_parse5(self):
        assert parse('https://example.com/path/to/page?name=ferret&color=purple&style=gold') == {'name': 'ferret','color': 'purple','style': 'gold'}
    def test_parse6(self):
        assert parse('https://example.com/path/to/page?') == {}
    def test_parse7(self):
        assert parse('http://example.com/') == {}
    def test_parse8(self):
        assert parse('http://example.com/?') == {}
    def test_parse9(self):
        assert parse('https://example.com/path/to/page?name') == {'name': ''}
    def test_parse10(self):
        assert parse('https://example.com/path/to/page?name=') == {'name': ''}
    def test_parse11(self):
        assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}