from chartserver.type_utils import is_float


def test_is_float():
    not_a_float = 'hello world'

    assert is_float(not_a_float) is False

    a_float = '5.66'

    assert is_float(a_float) is True

    real_float = 2.5

    assert is_float(real_float) is True
