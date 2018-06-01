from chartserver.utils import create_base64_filename
from base64 import b64encode


def test_create_base64_filename():
    assert create_base64_filename(['hello', 'world', '!', '!']) ==\
        b64encode('hello') +\
        b64encode('world') +\
        b64encode('!') +\
        b64encode('!') + '.png'

    assert '.png' in create_base64_filename(['hello', 'this', 'is', 'me'])
    assert '.jpg' in create_base64_filename(
        ['hello', 'this', 'is', 'me'], extension='.jpg')
