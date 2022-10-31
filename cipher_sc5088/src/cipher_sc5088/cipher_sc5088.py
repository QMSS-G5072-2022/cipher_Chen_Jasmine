def cipher(text, shift, encrypt=True):
    """
    The cipher fuction can help to decrypt and encrypt text.

    Parameters
    ----------
    text : enter the text you want to cipher
    shift: enter the number of shift you want your text to be cipher based on
    encrypt: This is a boolean parameter that you can use to decide if you want to decrypt
    or encrypt the text you enter

    Examples
    --------
    >>> from cipher_sc5088 import cipher_sc5088 as ci
    >>> ci.cipher('jasmine',10,encrypt=False)
    'ZQicYdU'
    >>> ci.cipher('ZQicYdU',10,encrypt=True)
    'jasmine'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
