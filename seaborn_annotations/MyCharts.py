import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def boxplot(
    df, x, y,
    title='My title', subtitle='My subtitle',
    highlights=[], annotations=[]
):
    plt.style.use('fivethirtyeight')
    sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'})
    sns.set_style('whitegrid')

    fig, ax = plt.subplots(figsize=(20,10))
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    plt.title(title, loc='left', fontsize=36, pad=50, weight='semibold')
    fig.text(
        0.08, .9, subtitle,
        horizontalalignment='left', size='medium', color='gray', weight='semibold',fontsize=28
    )

    plt.tick_params(labelsize=18)
    plt.yticks(fontweight="bold")
    plt.xlabel("", fontsize=0)
    plt.ylabel("", fontsize=0)

    sorted_nb = df.groupby([x])[y].median().sort_values(ascending=False)

    sns.set_context("talk", font_scale=1.4)

    custom_palette = {}
    for genre in list(sorted_nb.index):
        if genre in highlights:
            custom_palette[genre] = '#72b6a1'
        else:
            custom_palette[genre] = '#cccccc'

    splot = sns.boxplot(
        y=df[x],
        x=df[y],
        order=list(sorted_nb.index),
        palette=custom_palette,
        orient="h",
        linewidth=3.5,
        width=.7
    )
    
    for annotation in annotations:
        ax.annotate(annotation['text'],
                    xy=annotation['xy'], xycoords='data',
                    xytext=annotation['xytext'], textcoords='data',
                    arrowprops=dict(arrowstyle="->", fc='k', ec='k', connectionstyle="arc3,rad=.2", linewidth=2),
                    fontsize=18,
                    bbox=dict(boxstyle="round", facecolor="orange", edgecolor="orange", pad=0.4, alpha=0.4))

    return plt
