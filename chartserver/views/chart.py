from flask import Blueprint, send_file, send_from_directory, request
from chartserver.charts import create_bar_chart, create_pie_chart
from chartserver.type_utils import is_float
import base64
import os


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/chart'
)


@bp.route('/bar/<xpoints>/<ypoints>')
def bar(xpoints, ypoints):
    width = request.args.get('w')
    height = request.args.get('h')
    color = request.args.get('c')
    title = request.args.get('title')
    xlabel = request.args.get('xlabel')
    ylabel = request.args.get('ylabel')
    cached = True if not request.args.get('no_cache') else False

    directory = '/tmp/'
    filename = base64.b64encode(
        xpoints + ypoints + str(width) + str(height) + str(color) + str(title)
        + str(xlabel) + str(ylabel)
    ) + '.png'
    fullpath = directory + filename

    kwargs = dict(mimetype='image/png', attachment_filename=filename)

    if os.path.isfile(fullpath) and cached:
        return send_from_directory(directory, filename, **kwargs)

    xpoints = [float(x) if x.isdigit() else x for x in xpoints.split(',')]
    ypoints = [float(y) if y.isdigit() else y for y in ypoints.split(',')]

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

    directory = '/tmp/'
    filename = base64.b64encode(
        str(width) + str(height) + str(color) + str(labels) + str(sizes)
        + str(explode) + str(shadow)
    ) + '.png'
    fullpath = directory + filename

    kwargs = dict(mimetype='image/png', attachment_filename=filename)

    if os.path.isfile(fullpath) and cached:
        return send_from_directory(directory, filename, **kwargs)

    labels = [float(x) if x.isdigit() else x for x in labels.split(',')]
    sizes = [float(y) if y.isdigit() else y for y in sizes.split(',')]
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
