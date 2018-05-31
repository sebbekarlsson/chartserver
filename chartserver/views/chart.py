from flask import Blueprint, send_file, send_from_directory, request
import os
from chartserver.charts import create_bar_chart, create_pie_chart
from chartserver.type_utils import is_float
from chartserver.utils import create_base64_filename


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/chart'
)

DIRECTORY = '/tmp/'
MIMETYPE = 'image/png'


@bp.route('/bar/<xpoints>/<ypoints>')
def bar(xpoints, ypoints):
    width = request.args.get('w')
    height = request.args.get('h')
    color = request.args.get('c')
    title = request.args.get('title')
    xlabel = request.args.get('xlabel')
    ylabel = request.args.get('ylabel')
    cached = True if not request.args.get('no_cache') else False

    filename = create_base64_filename([
        width, height, color, title, xlabel, ylabel])

    fullpath = DIRECTORY + filename

    kwargs = dict(mimetype=MIMETYPE, attachment_filename=filename)

    if os.path.isfile(fullpath) and cached:
        return send_from_directory(DIRECTORY, filename, **kwargs)

    xpoints = [float(x) if is_float(x) else x for x in xpoints.split(',')]
    ypoints = [float(y) if is_float(y) else y for y in ypoints.split(',')]

    chart_io = create_bar_chart(
        fullpath,
        xpoints,
        ypoints,
        width=int(width) if width else 640,
        height=int(height) if height else 480,
        color=color.split(',') if color else None,
        title=title if title else '',
        xlabel=xlabel if xlabel else '',
        ylabel=ylabel if ylabel else ''
    )

    return send_file(chart_io, **kwargs)


@bp.route('/pie/<labels>/<sizes>')
def pie(labels, sizes):
    width = request.args.get('w')
    height = request.args.get('h')
    color = request.args.get('c')
    explode = request.args.get('explode')
    shadow = True if request.args.get('shadow') else False
    cached = True if not request.args.get('no_cache') else False

    filename = create_base64_filename([
        width, height, color, labels, sizes, explode, shadow])

    fullpath = DIRECTORY + filename

    kwargs = dict(mimetype=MIMETYPE, attachment_filename=filename)

    if os.path.isfile(fullpath) and cached:
        return send_from_directory(DIRECTORY, filename, **kwargs)

    labels = [float(x) if is_float(x) else x for x in labels.split(',')]
    sizes = [float(y) if is_float(y) else y for y in sizes.split(',')]
    explode = [float(e) if is_float(e) else 0.0 for e in explode.split(',')]\
        if explode else None

    chart_io = create_pie_chart(
        fullpath,
        labels,
        sizes,
        explode=explode,
        shadow=shadow,
        width=int(width) if width else 640,
        height=int(height) if height else 480,
        color=color.split(',') if color else None
    )

    return send_file(chart_io, **kwargs)
