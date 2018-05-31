from chartserver.utils import create_base64_filename


def test_create_base64_filename():
    assert len(create_base64_filename(['hello', 'world', '!', '!'])) > 8

    assert '.png' in create_base64_filename(['hello', 'this', 'is', 'me'])
    assert '.jpg' in create_base64_filename(
        ['hello', 'this', 'is', 'me'], extension='.jpg')
