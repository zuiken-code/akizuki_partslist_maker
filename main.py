import requests
import json

def main():
    shop_id = "akizuki"     #akizuki,eleshop,sengoku が選択できる
    model_number = 116108   #秋月電子の販売コード
    model_count = 3         #何個買うのか

    res = get_res(shop_id,model_number)

    name = get_name(res)
    price = get_price(res)
    subtotal = price * model_count
    price_str = "￥"+str(get_price(res))
    subtotal_str = "￥"+str(price * model_count)
    
    print(name)
    print(price_str)
    print(subtotal_str)

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
