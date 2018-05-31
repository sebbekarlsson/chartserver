import numpy as np
import matplotlib.pyplot as plt
import io


def create_bar_chart(filename, xpoints, ypoints):
    # Make a fake dataset:
    # ypoints = [3, 12, 5, 18, 45]
    # bxars = ('A', 'B', 'C', 'D', 'E')
    y_pos = np.arange(len(xpoints))

    plt.bar(y_pos, ypoints)

    plt.xticks(y_pos, xpoints)

    buf = io.BytesIO()

    plt.draw()
    plt.savefig(buf, format='png')

    buf.seek(0)

    plt.savefig(filename)

    return buf
