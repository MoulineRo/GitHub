# def parse(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


from http import cookies

def parse_cookie(str):
    key1=[]
    value1=[]
    dictionary={}
    value=cookies.BaseCookie(str).values()
    for values in value:
        key1.append(values.key)
        value1.append(values.value)
        dictionary=dict(zip(key1,value1))
    return dictionary

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User=;age=28;') == {'name': 'Dima=User=', 'age': '28'}
    assert parse_cookie('name=Dima=User=Notuser;age=28;') == {'name': 'Dima=User=Notuser', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;surname=Popov') == {'name': 'Dima=User', 'age': '28','surname':'Popov'}
    assert parse_cookie('name=Dima=User;age=28;surname=') == {'name': 'Dima=User', 'age': '28', 'surname':''}
    assert parse_cookie('name=Dima;age=') == {'name': 'Dima', 'age':''}
    assert parse_cookie('name=') == {'name': ''}

