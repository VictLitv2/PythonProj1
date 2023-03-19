
import requests
from bs4 import BeautifulSoup


def retrieve_input_from_inet():
    try:
        response = requests.get('https://www.laughteronlineuniversity.com/three-word-quotes/')
        soup = None
        try:
            soup = BeautifulSoup( str(response.content, "UTF-8"), features="lxml")
        except:
            pass
        items = soup.select(".post-content  li  li ")
        result = []
        for item in items:
            item_text = f'{item.getText()}'
            result.append(item_text)
        return  result
    except Exception as exc:
        print(exc)
        return ['Mission is Impossible', 'It is hard to start', 'Yes We can']
