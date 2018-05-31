from chartserver.app import app
from chartserver.config import config


STATIC_DIR = 'chartserver/static'


def run():
    app.run(
        debug=config['debug'] if 'debug' in config else False,
        threaded=config['threaded'] if 'threaded' in config else False
    )


if __name__ == '__main__':
    run()
