'''
5-4 可変長引数
'''
def spam(arg1, *args, **kwargs):
    print(f'arg1 : {arg1}')
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
    print(type(args))
    print(type(kwargs))

spam(
    'value1',
    2,
    0.3,
    {'key': 4},
    arg5=50,
    arg6=[0, 1, 2]
)
