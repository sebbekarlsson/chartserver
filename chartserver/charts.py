import numpy as np
import matplotlib.pyplot as plt
import io


FORMAT = 'png'
DPI_DIV = 3200


def write_image_buffer_and_save(plt, buf, filename, dpi):
    plt.draw()
    plt.savefig(buf, format=FORMAT, dpi=dpi)

    buf.seek(0)
    plt.savefig(filename, format=FORMAT, dpi=dpi)

    return buf


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
    dpi = (width * height) / DPI_DIV
    plt.rcParams["figure.figsize"] = [width / dpi, height / dpi]
    y_pos = np.arange(len(xpoints))

    plt.bar(y_pos, ypoints, color=color)

    plt.xticks(y_pos, xpoints)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    buf = io.BytesIO()

    return write_image_buffer_and_save(plt, buf, filename, dpi=dpi)


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
    dpi = (width * height) / DPI_DIV
    plt.rcParams["figure.figsize"] = [width / dpi, height / dpi]

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=shadow, startangle=90, colors=color)

    ax1.axis('equal')

    plt.tight_layout()

    buf = io.BytesIO()

    return write_image_buffer_and_save(plt, buf, filename, dpi=dpi)


def create_line_chart(
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
    dpi = (width * height) / DPI_DIV
    plt.rcParams["figure.figsize"] = [width / dpi, height / dpi]

    plt.plot(xpoints, ypoints, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.tight_layout()

    buf = io.BytesIO()

    return write_image_buffer_and_save(plt, buf, filename, dpi=dpi)
