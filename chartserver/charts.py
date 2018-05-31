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
    print(dpi)
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
