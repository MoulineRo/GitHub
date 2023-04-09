from urllib.parse import urlsplit
def parse(str):
    keys=[]
    value=[]
    dictonary={}
    skip=''
    url = urlsplit(str).query.replace('&',' ').split(' ')
    for urls in url:
        if len(urls)>0:
            urlss=urls.split('=')
            keys.append(urlss[0])
            if len(urlss)==1:
                value.append(skip)
                dictonary = dict(zip(keys, value))
            if len(urlss)==2:
                value.append(urlss[1])
                dictonary = dict(zip(keys, value))
    return dictonary

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&style') == {'name': 'ferret', 'color': 'purple', 'style': ''}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&style=') == {'name': 'ferret', 'color': 'purple', 'style': ''}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&style=gold') == {'name': 'ferret', 'color': 'purple', 'style': 'gold'}
    assert parse('https://example.com/path/to/page?') == {}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('https://example.com/path/to/page?name') == {'name': ''}
    assert parse('https://example.com/path/to/page?name=') == {'name': ''}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}



  # def parse_cookie(query: str) -> dict:
  #     return {}
  #    if __name__ == '__main__':
  #    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
  #    assert parse_cookie('') == {}
  #    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
  #    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}