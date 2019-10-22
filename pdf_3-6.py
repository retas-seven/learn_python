'''
3-6 辞書型（Dictionaries）
'''
d = {
    'key1': 'Value1',
    'key2': 'Value2',
    'key3': 'Value3',
}

print('------------------------')
print('インデックスアクセス')
print('------------------------')
print(d['key1'], d.get('key2'), d.get('keyX'), d.get('keyX', 'defaultValue!'), sep=', ')

print('------------------------')
print('イテレーション key-1')
print('------------------------')
for key in d:
    print(key)

print('------------------------')
print('イテレーション key-2')
print('------------------------')
for key in d.keys():
    print(key)

print('------------------------')
print('イテレーション value')
print('------------------------')
for value in d.values():
    print(value)

print('------------------------')
print('イテレーション key + value')
print('------------------------')
for key, value in d.items():
    print(key, value, sep=', ')

print('------------------------')
print('辞書の更新')
print('------------------------')
d['key1'] = 'NewValue1'  # key1の値を上書き
d['newKey'] = 'NewValue!!'  # 新しいキーと値を追加
print(d)

del d['newKey']
pop_value = d.pop('key2')
print(pop_value)
print(d)

