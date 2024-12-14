import requests
import json

def main():
    print("Hello world")
    shop_id = "akizuki"     #akizuki,eleshop,sengoku が選択できる
    model_number = 114961

    get(shop_id,model_number)

def get(shop_id,model_number):
    url = f"https://api.partscabi.net/v1/shop/{shop_id}/component/{model_number}/"
    res = requests.get(url)
    name = res.json()["prices"][0]["value"]
    print(name)
    








if __name__ == '__main__':
    main()
