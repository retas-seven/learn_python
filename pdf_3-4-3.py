'''
3-4-3 リスト
'''
id_list = [1, 2, 3.0, 'a', 'b', 'c']

print('------------------------')
print('インデックスアクセス')
print('------------------------')
print(id_list[0], id_list[1], id_list[2], id_list[3], id_list[4], id_list[5], sep=', ')

print('------------------------')
print('イテレーション')
print('------------------------')
for id in id_list:
    print(id)

print('------------------------')
print('リストの更新')
print('------------------------')
id_list.append('spam')
id_list.append('eggs')
print(id_list)
id_list.remove('spam')
print(id_list)