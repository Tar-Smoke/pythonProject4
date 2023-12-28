import requests
from bs4 import BeautifulSoup


list_ua = [("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 "
          "Chrome/87.0.4280.144 Safari/537.36 Dooble/2023.07.15 Dooble/2023.11.30"), "Mozilla/5.0 (Linux; U; X11; en-US; Valve Steam GameOverlay/1544834093; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15 Epiphany/605.1.15"]
num_run = 1
num_ua = num_run % 3 - 1
headers = {"User-Agent": list_ua[num_ua]}

URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="

list_url = []
for i in range(20):
    x = i+1
    list_url.append(URL + str(x))

def get_soup(url, headers):
    global num_run
    num_run += 1
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        print(num_run)
    else:
        print("ERROR!!! code is not 200")
        soup = None

    return soup
def our_data(list_url, headers):
    computer_names = []
    comp_prices = []
    comp_descriptions = []
    all_data = []
    for url in list_url:
        comp_name = get_soup(url, headers).find_all("a", class_="title")
        for c_name in comp_name:
            computer_names.append(c_name.text)
        comp_price = get_soup(url, headers).find_all("h4", class_="float-end price card-title pull-right")
        for c_price in comp_price:
            comp_prices.append(c_price.text)
        comp_descr = get_soup(url, headers).find_all("p", class_="description card-text")
        for c_descr in comp_descr:
            comp_descriptions.append(c_descr.text)
    for i in range(0, len(computer_names)):
        a_data = []
        a_data.append(f"name {computer_names[i]}")
        a_data.append(f"price {comp_prices[i]}")
        a_data.append(f"description {comp_descriptions[i]}")
        all_data.append(a_data)


    return all_data

new_all_data = our_data(list_url, headers)
nf = open("computers.txt", "w")
for j in range(0, len(new_all_data)):
    nf.write("--------------- \n")
    for nd in  new_all_data[j]:
        nf.write(f"{nd}\n")

nf.close()
