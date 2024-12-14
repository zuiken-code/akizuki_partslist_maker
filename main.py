import requests
import json

def main():
    shop_id = "akizuki"     #akizuki,eleshop,sengoku が選択できる
    model_number = 116108   #秋月電子の販売コード

    res = get_res(shop_id,model_number)
    price = str(get_price(res))+"円"
    name = get_name(res)
    print(name)
    print(price)

def get_res(shop_id,model_number):
    url = f"https://api.partscabi.net/v1/shop/{shop_id}/component/{model_number}/"
    res = requests.get(url)
    print(res.json())
    return res

def get_name(res):
    name = res.json()["name"]
    return name

def get_price(res):
    price = res.json()["prices"][0]["value"]
    return price








if __name__ == '__main__':
    main()
