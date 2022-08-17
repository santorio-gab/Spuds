from bs4 import BeautifulSoup
import requests

url = "https://www.tesco.ie/groceries/en-IE/shop/fresh-food/fresh-vegetables/potatoes"

result =  requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

prod_list = soup.find_all('div', {"class":"styles__StyledVerticalTileWrapper-dvv1wj-0 dtCNPH"})
spuds = {}
 
for product in prod_list:
    stock_check = product.find('div', {"class":"product-info-message-list"}).text
    if 'out of' not in  stock_check:
        name = product.find('span', {"class":"styled__Text-sc-1xbujuz-1 ldbwMG beans-link__text"}).text
        price_kg = product.find('p', {"class":"styled__StyledFootnote-sc-119w3hf-7 icrlVF styled__Subtext-sc-8qlq5b-2 bNJmdc beans-price__subtext"}).text[1:-3]
        if '/' not in price_kg:
            price_kg = float(price_kg)
            spuds.update({f'{name}' : f'{price_kg}'})

spuds_sorted = dict(sorted(spuds.items(), key= lambda x:x[1]))

for key, value in spuds_sorted.items():
    print(key + ' - €' + value +'/kg')
