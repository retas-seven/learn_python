'''
6-1 クラスの定義 〜
'''

class User:
    '''
    ユーザ情報クラス
    '''

    def __init__(self, name, email):
        '''
        ユーザ情報クラス
        '''
        self.name = name
        self.email = email

    def show(self):
        '''
        ユーザ情報を表示します
        '''
        print(f'{self.name} : {self.email}')

user_list = [
    User('iwasaki', 'iwasaki@test.com'),
    User('saito', 'saito@test.com'),
    User('suzuki', 'suzuki@test.com'),
]

for user in user_list:
    user.show()
