'''
4-3 ループ, 4-4 リスト内包表記, 4-5 その他の内包表記
'''
from decimal import Decimal

def calc_zeikomi(value):
    return value * Decimal('1.08')

price_list = [100, 200, 300, 400, 500]

print('------------------------')
print('内包表記を使用しない記述')
print('------------------------')
zeikomi_list_01 = []
for price in price_list:
    zeikomi_list_01.append(calc_zeikomi(price))
print(zeikomi_list_01)

print('------------------------')
print('内包表記で記述（List）')
print('------------------------')
zeikomi_list_02 = [calc_zeikomi(price) for price in price_list]
print(zeikomi_list_02)

print('------------------------')
print('内包表記で記述（Dict）')
print('------------------------')
zeikomi_dict = {price: calc_zeikomi(price) for price in price_list}
print(zeikomi_dict)
