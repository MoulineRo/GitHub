import unittest
from main import parse_cookie

class TestParse(unittest.TestCase):

    def testparse1(self):
        assert parse_cookie('name=Dima;') == {'name': 'Dima'}

    def testparse2(self):
        assert parse_cookie('') == {}

    def testparse3(self):
        assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}

    def testparse4(self):
        assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    def testparse5(self):
        assert parse_cookie('name=Dima=User=;age=28;') == {'name': 'Dima=User=', 'age': '28'}

    def testparse6(self):
        assert parse_cookie('name=Dima=User=Notuser;age=28;') == {'name': 'Dima=User=Notuser', 'age': '28'}

    def testparse7(self):
        assert parse_cookie('name=Dima=User;age=28;surname=Popov') == {'name': 'Dima=User', 'age': '28','surname': 'Popov'}

    def testparse8(self):
        assert parse_cookie('name=Dima=User;age=28;surname=') == {'name': 'Dima=User', 'age': '28', 'surname': ''}

    def testparse9(self):
        assert parse_cookie('name=Dima;age=') == {'name': 'Dima', 'age': ''}

    def testparse10(self):
        assert parse_cookie('name=') == {'name': ''}

