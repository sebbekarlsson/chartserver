from base64 import b64encode


def create_base64_filename(nodes=[], extension='.png'):
    return ''.join([b64encode(str(node)) for node in nodes]) + extension
