import numpy as np
import matplotlib.pyplot as plt
import io


def create_bar_chart(
    filename,
    xpoints,
    ypoints,
    width=640,
    height=480,
    color=None,
    title='',
    xlabel='',
    ylabel=''
):
    dpi = (width * height) / 3200
    plt.rcParams["figure.figsize"] = [width / dpi, height / dpi]
    y_pos = np.arange(len(xpoints))

    plt.bar(y_pos, ypoints, color=color)

    plt.xticks(y_pos, xpoints)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    buf = io.BytesIO()

    kwargs = dict(format='png', dpi=dpi)

    plt.draw()
    plt.savefig(buf, **kwargs)

    buf.seek(0)
    plt.savefig(filename, **kwargs)

    return buf


def create_pie_chart(
    filename,
    labels,
    sizes,
    explode=None,
    shadow=False,
    width=640,
    height=480,
    color=None
):
    dpi = (width * height) / 3200
    plt.rcParams["figure.figsize"] = [width / dpi, height / dpi]

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=shadow, startangle=90, colors=color)

    ax1.axis('equal')

    plt.tight_layout()

    buf = io.BytesIO()

    kwargs = dict(format='png', dpi=dpi)

    plt.draw()
    plt.savefig(buf, **kwargs)

    buf.seek(0)
    plt.savefig(filename, **kwargs)

    return buf
