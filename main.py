import requests
import json

def main():
    shop = "秋月電子通商"    #今回は秋月電子限定(今後追加実装の可能性アリ)←結局しないやつ
    shop_id = "akizuki"     #akizuki,eleshop,sengoku が選択できる
    model_number = 116108   #秋月電子の販売コード
    model_count = 3         #何個買うのか

    res = get_res(shop_id,model_number)

    if res != "エラー":
        name = get_name(res)
        price = get_price(res)
        url = get_url(res)
        place = get_place(res)

        subtotal = price * model_count
        price_str = "￥"+str(get_price(res))
        subtotal_str = "￥"+str(price * model_count)

        print(model_number)
        print(name)
        print(price_str)
        print(model_count)
        print(subtotal_str)
        print(shop)
        print(url)
        print(place)
    else:
        print("この販売コードの商品は存在しない、もしくはWiFiに接続出来ていません")

def get_res(shop_id,model_number):
    url = f"https://api.partscabi.net/v1/shop/{shop_id}/component/{model_number}/"

    try:
        res = requests.get(url)
        res.raise_for_status()
        return res
    except ConnectionError as ce:
        print(f"WiFi接続エラー: {ce}")
        return "エラー"   #後で直す
    except requests.RequestException as re:
        print(f"リクエストエラー: {re}")
        return "エラー"


def get_name(res):
    name = res.json()["name"]
    return name

def get_price(res):
    price = res.json()["prices"][0]["value"]
    return price

def get_url(res):
    url = res.json()["link"]
    return url

def get_place(res):
    place = res.json()["stores"][0]["place"]
    return place







if __name__ == '__main__':
    main()
