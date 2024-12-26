from get import get_all

def main():
    shop = "秋月電子通商"    #今回は秋月電子限定(今後追加実装の可能性アリ)←結局しないやつ
    number = 116108
    count = 3
    name,price,count,url,place = get_all(number,count)
    subtotal = price * count
    print(name)
    print(price)
    print(count)
    print(subtotal)
    print(shop)
    print(url)
    print(place)



if __name__ == '__main__':
    main()