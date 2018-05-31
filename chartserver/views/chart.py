from flask import Blueprint, send_file, send_from_directory
from chartserver.charts import create_bar_chart
import base64
import os


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/chart'
)


@bp.route('/bar/<xpoints>/<ypoints>')
def show(xpoints, ypoints):
    directory = '/tmp/'
    filename = base64.b64encode(xpoints + ypoints) + '.png'
    fullpath = directory + filename

    kwargs = dict(mimetype='image/png', attachment_filename=filename)

    if os.path.isfile(fullpath):
        return send_from_directory(directory, filename, **kwargs)

    xpoints = [float(x) if x.isdigit() else x for x in xpoints.split(',')]
    ypoints = [float(y) if y.isdigit() else y for y in ypoints.split(',')]

    chart_io = create_bar_chart(
        fullpath,
        xpoints,
        ypoints
    )

    return send_file(chart_io, **kwargs)
