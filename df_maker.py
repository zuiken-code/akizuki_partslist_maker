from get import get_all
import pandas as pd


def main():
    numbers = [114659,129604,109848]
    pieces = [1,2,3]
    df = df_maker(numbers,pieces)
    print(df)

def df_maker(numbers,pieces):
    if len(numbers) == len(pieces):
        df = make_df(numbers,pieces)
        return df
    else:
        print("エラー: 入力された販売コードと個数の数が一致しません")

def make_df(numbers,pieces):
    df = pd.DataFrame(columns=["名前","単価","個数","小計","購入店舗","URL","場所"],index=numbers)
    shop = "秋月電子通商"    #今回は秋月電子限定(今後追加実装の可能性アリ)←結局しないやつ
    for i in range(len(numbers)):
        number = numbers[i]
        count = pieces[i]
        name,price,count,url,place = get_all(number,count)
        subtotal = price * count
        df.loc[number,:] = [name,price,count,subtotal,shop,url,place]
    return df



if __name__ == '__main__':
    main()