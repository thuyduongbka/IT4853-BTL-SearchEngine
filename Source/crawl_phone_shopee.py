import requests
import json

dataSolr = []

MAX_PAGE = 50
for page in range(MAX_PAGE):
    print(page)
    URL = "https://shopee.vn/api/v2/search_items/"
    PARAMS = {
        'by': 'sales',
        'limit': '50',
        'match_id': '1979',
        'newest': 50*page,
        'order': 'desc',
        'page_type': 'search',
        'version': '2',
    }
    HEADER = {
        'authority': 'shopee.vn',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'SPC_IA=-1; SPC_EC=-; REC_MD_20=1587914140; SPC_U=-; _gcl_au=1.1.1083950908.1587914141; SPC_F=HLS1oqu0cSc5Axs2tvUFewl4kWaXiK69; REC_T_ID=ca1876c6-87d0-11ea-a6ed-f063f977aeaf; SPC_SI=qpd4af4ih5iwm303b6i5xlxbkw43jv6q; SPC_CT_fadd83b7="1587914139.ZSi8LKdPnZVjcUq6ZZpI1OHglYTTpde/HUKRlj/IJwk="; _fbp=fb.1.1587914141886.357636920; _hjid=7b3acc03-cdcc-4399-a2a4-0b138c4edfbb; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1484201642.1587914143; _gid=GA1.2.198685633.1587914143; _dc_gtm_UA-61914164-6=1; SPC_CT_a6641b98="1587914320.stywd4+yYMmfn3Ha34ihgBidO9TDBizaH3oEG1LPsDIx/mYBVtzz32uATwnbF9dW"; SPC_R_T_ID="gA0jSZhRpRIQz0co/Q5mXoBTpdeyCLWtDdstO3n80s8sYUpNhF+rRfg7GEA2T+UCRvajUv+TxyaOrZdVheSeIBTYHxKssrDE/CrD6UdbXoo="; SPC_T_IV="bszZBreb3pekalXiBN9raQ=="; SPC_R_T_IV="bszZBreb3pekalXiBN9raQ=="; SPC_T_ID="gA0jSZhRpRIQz0co/Q5mXoBTpdeyCLWtDdstO3n80s8sYUpNhF+rRfg7GEA2T+UCRvajUv+TxyaOrZdVheSeIBTYHxKssrDE/CrD6UdbXoo="',
        'if-none-match-': '55b03-b32c62222fb5c1d9159b28be724be96e',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'x-api-source': 'pc',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.get(url=URL, headers=HEADER, params=PARAMS)
    print(response)

    data = response.json()
    items = data['items']

    for i in items:
        URL_ITEM = "https://shopee.vn/api/v2/item/get"
        PARAMS_ITEM = {
            'itemid': i['itemid'],
            'shopid': i['shopid']
        }
        response = requests.get(
            url=URL_ITEM, headers=HEADER, params=PARAMS_ITEM).json()
        item = response['item']

        json_load = {
            'name': item['name'],
            'id': item['itemid'],
            'shopid': item['shopid'],
            'location': item['shop_location'],            
            'rating_star': item['item_rating']['rating_star']
        }        
        dataSolr.append(json_load)       

with open('data.json', 'w') as outfile:
    json.dump(dataSolr, outfile)

# print("Name: ",item['name'])
# # print("Location: ",item['shop_location'])
# # print("Price: ",item['price'])
# # print("Price Max: ",item['price_max'])
# # print("Price Min: ",item['price_min'])
# # print("Brand: ",item['brand'])
# # print("view_count: ", item['view_count'])
# # print("item_rating: ", item['item_rating'])
# # print("description", item['description'])
# # print("liked_count", item['liked_count'])
# # print("historical_sold", item['historical_sold'])
# # print("categories", item['categories'])
# # print("attributes", item['attributes'])
# print()
