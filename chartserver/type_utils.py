def is_float(x):
    try:
        x = float(x)
        return True
    except Exception:
        pass

    return False
