'''
5-9 高階関数とlambda式
'''
def task01():
    print('task01 end')

def task02():
    print('task02 end')

def task03():
    print('task03 end')

def execute(*tasks):
    for task in tasks:
        task()

execute(
    task01,
    task02,
    task03,
    lambda: print('task04 end'),
    lambda: print('task05 end'),
)
