def is_float(x):
    try:
        x = float(x)
        return True
    except TypeError:
        pass

    return False
