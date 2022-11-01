from cipher_sc5088 import cipher_sc5088

def test_cipher_negative_shift():
    shift_eg1 = -8
    text_eg1= 'Python is so fun'
    assert cipher_sc5088.cipher(text_eg1,shift_eg1)=='HqlZgf ak kg Xmf', 'shift can be negative'


