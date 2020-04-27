from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import keyword
from IPython.display import set_matplotlib_formats
from pprint import pprint

def mushroom_plot(series, clazz, title=None, legend_map=None):
    title = series.name if title is None else title
    svs = series.unique() #series values
    cvs = clazz.unique() #class values
    legend_map = {k: k for k in cvs} if legend_map is None else legend_map
    cvs = sorted(cvs, key=lambda c: np.count_nonzero(clazz==c))
    #print(np.count_nonzero(series=='r'))
    data = {k:
        {
            'total': np.count_nonzero(series==k),
            **{
                c: np.count_nonzero((series==k) & (clazz==c))
                for c in cvs
            }
        }
        for k in svs
    }
    data = sorted(list(data.items()), key=lambda x: -x[1]['total'])
    #pprint(data)
    #finding the left edge
    left = np.array([0] + list(np.cumsum(list(map(lambda x: x[1]['total'], data)))))
    
    plt.figure(figsize=(20,6))
     
    for i,(color, pe) in enumerate(data):
        #figure out bottom edge
        percent = [pe[c]/pe['total'] for c in cvs]
        bottom = [0] + list(np.cumsum(percent))
        for ic, (bot, b, p) in enumerate(zip(cvs, bottom, percent)):
            plt.bar(left[i], p, color='C{0}'.format(ic), width=pe['total'], align='edge', bottom=b)
    midpoints = (left[1:] + left[:-1])/2
    labels = list(map(lambda x: x[0], data))
    plt.xticks(midpoints, labels)
    plt.xlim(0,left[-1])
    plt.ylim(0,1)
    for l in left:
        plt.axvline(l, ls='dashed', color='gray')
    plt.title(title)
    from matplotlib.patches import Patch
    patches = [Patch(color='C{0}'.format(i)) for i, k in enumerate(cvs)]
    labels = [legend_map.get(k, k) for k in cvs]
    plt.legend(patches, labels)
    return data