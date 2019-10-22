'''
3-3-8 Decimalモジュール
'''
from decimal import Decimal

ng_test_01 = 0.1 + 0.1 + 0.1
ng_test_02 = 0.1 * 0.1 * 0.1
print('NG TEST:', ng_test_01, ng_test_02, sep=', ')

ok_test_01 = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
ok_test_02 = Decimal('0.1') * Decimal('0.1') * Decimal('0.1')
print('OK TEST:', ok_test_01, ok_test_02, sep=', ')

int_test_01 = 10 + 10 + 10
int_test_02 = 10 * 10 * 10
print('INT TEST:', int_test_01, int_test_02, sep=', ')
