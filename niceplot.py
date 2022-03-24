#!/bin/env python3
""" quick wrapper to generate a 'nice' plot """

import matplotlib.pyplot as plt


def niceplot(xdata, ydata, xlabel='', ylabel='', fromzero=False):
    """ here is the aforementioned 'nice' plot """

    label_fonts = { 'fontsize': 12, 'font': 'Arial'}
    plot_args = {'linewidth': 1, 'color': '#000000'}

    fig = plt.figure(figsize=[4, 4*0.618])
    axs = fig.add_axes([0.15,0.2,0.75,0.75])
    axs.plot(xdata, ydata, 'o-', **plot_args)

    axs.set_xlabel(xlabel, labelpad=4, **label_fonts)
    axs.set_ylabel(ylabel, labelpad=8, **label_fonts)
    if fromzero:
        axs.set_ylim(0, None)
        axs.set_xlim(0, None)
    axs.spines[['right', 'top']].set_visible(False)
    axs.spines[['left', 'bottom']].set_linewidth(1)

    return plt.show()
