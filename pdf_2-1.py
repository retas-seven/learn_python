'''
2-1 Pythonの基本 〜
'''

def main():
    '''
    サンプルプログラムのメイン関数
    '''
    for i in range(1, 6): # 1, 2, 3, 4, 5 の数値を生成
        if i % 2 == 0:
            print(f'{i}は偶数です。')
        else:
            print(f'{i}は奇数です。')

if __name__ == '__main__':
    main()
