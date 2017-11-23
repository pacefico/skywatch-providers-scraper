
import requests
from bs4 import BeautifulSoup

url_page = 'https://www.skywatch.co/datasets'
page = requests.get(url_page)
soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find('div', attrs={'class': 'main-content'} )

my_data_set = {}
for div in content.find_all('div'):
    if 'id' in div.attrs:
        data_block = div.find('div', attrs={'data-block-type': '44'})

        if data_block:
            data_set_name = data_block.find('h2').text

            if data_set_name and data_set_name not in my_data_set:
                print(data_set_name)
                if data_set_name and len(data_set_name) > 0:
                    data_set_provider = ""
                    data_set_info = div.find('div', attrs={'data-block-type': '2'})
                    for item in data_set_info.find_all('p'):
                        if 'provider' in item.text.lower():
                            data_set_provider = item.text
                            break
                    my_data_set[data_set_name] = data_set_provider

response = {
    "datasets": my_data_set,
    "total": len(my_data_set)
}

print(response)



