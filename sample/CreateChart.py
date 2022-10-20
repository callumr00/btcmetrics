import os

import matplotlib.pyplot as plt

def CreateChart(chart_type,
                x,
                y,
                x2=None,
                y2=None,
                average=None,
                title=None,
                xlabel=None,
                xformat=None,
                xticks=None,
                xlim=None,
                xscale=None,
                ylabel=None,
                yformat=None,
                yticks=None,
                ylim=None,
                yscale=None,
                hline=None,
                vline=None
                ):
    '''
    Create chart using function Args and kwArgs
    
    Uses function arguments and keyword arguments to create a matplotlib visualization
    of data. Arguments are used in combination with pre-determined variables and
    style attributes to provide uniformity in layout while having tailored results
    specific to what is required to best present the data.
    '''

    # Set colours
    axcol = 'orange'
    axcol2 = 'black'

    # Create chart
    fig, ax = plt.subplots()
    
    # Set the type of chart desired and plot the data
    if chart_type == 'scatter':
        plt.scatter(x, y, color=axcol, s=1, alpha=0.2)
    elif chart_type == 'line':
        ax.plot(x, y, color=axcol)

    # Hide chart spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set attributes for chart grid 
    plt.grid(True, which='major', axis='both', alpha=0.4)

    # Plot a second data set, keeping the same y values
    if x2 is not None:
        if chart_type == 'scatter':
            plt.scatter(x2, y, color=axcol2, s=1, alpha=0.2)
        elif chart_type == 'line':
            ax.plot(x2, y, color=axcol2, alpha=0.4)

    # Plot a second data set, keeping the same x values
    if y2 is not None:
        if chart_type == 'scatter':
            ax2.scatter(x, y2, color=axcol2, s=1, alpha=0.2)
        elif chart_type == 'line':
            ax2.plot(x, y2, color=axcol2)

    # Plot a rolling mean line
    if average is not None:
        plt.plot(average, color='k', alpha=0.6, linewidth=1)

    # Set chart title
    if title is not None:
        plt.title(title, pad=30)

    # Set x axis label
    if xlabel is not None:
        ax.set_xlabel(xlabel, labelpad=20)

    # Format the x axis tick values
    if xformat is not None:
        ax.xaxis.set_major_formatter(xformat)

    # Set the x axis tick values
    if xticks is not None:
        plt.xticks(xticks)

    # Set the range of x values shown
    if xlim is not None:
        plt.xlim(xlim)

    # Set the scale in which x values are shown
    if xscale is not None:
        plt.xscale(xscale)

    # Set y axis label
    if ylabel is not None:
        ax.set_ylabel(ylabel, labelpad=20)

    # Format the y axis tick values
    if yformat is not None:
        ax.yaxis.set_major_formatter(yformat)

    # Set the y axis tick values
    if yticks is not None:
        plt.yticks(yticks)

    # Set the range of y values shown
    if ylim is not None:
        plt.ylim(ylim)

    # Set the scale in which y values are shown
    if yscale is not None:
        plt.yscale(yscale)

    # Plot a horizontal line
    if hline is not None:
        plt.axhline(y = hline, color = axcol2, linestyle='--')

    # Plot a vertical line
    if vline is not None:
        plt.axvline(x = vline, color = axcol2, linestyle='--')

    # Show chart
    plt.show()