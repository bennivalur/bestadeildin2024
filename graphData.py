import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from configs import team_pic_mapper
import statistics


def getImage(path): 
    return OffsetImage(plt.imread(path), zoom=.5)


def graphData(data, xAxis,yAxis,invertXAxis,perGame):
    logos = os.listdir(os.getcwd() + '/logos')
    #print(logos)
    logo_paths = []
    x = []
    y = []
    for i in data:
        logo_paths.append(os.getcwd() + '/logos/' + team_pic_mapper[i['team']]+'.png')
        if perGame:
            x.append(i[xAxis]/i['games'])
            y.append(i[yAxis]/i['games'])
        else:
            x.append(i[xAxis])
            y.append(i[yAxis])
    fig, ax = plt.subplots()

    #Make a scatter plot first to get the points to place logos
    ax.scatter(x, y, s=.001)
    if invertXAxis:
        ax.invert_xaxis()

    #Adding logos to the chart
    for x0, y0, path in zip(x, y, logo_paths):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False, fontsize=4)
        ax.add_artist(ab)

    #Adding labels and text
    perGameString = ''
    if perGame:
        perGameString = '/game'
    ax.set_xlabel(xAxis + perGameString, fontsize=16)
    ax.set_ylabel(yAxis + perGameString, fontsize=16)

    #Add a grid
    ax.grid(zorder=0,alpha=.4)
    ax.set_axisbelow(True)

    #ax.invert_xaxis()

    ax.set_title('Data provided by @bestadeildin', fontsize=7)
    plt.suptitle('Bestadeildin 2024 ' + xAxis + ' Vs. ' + yAxis, fontsize=18)
    plt.figtext(.66, .02, 'Data: @bestadeildin | Graph: @bennivaluR_', fontsize=7)

    plt.plot([statistics.mean(x),statistics.mean(x)],[max(y),min(y)], 
            color='darkorange', linestyle='--')
    plt.plot([max(x),min(x)],[statistics.mean(y),statistics.mean(y)], 
            color='darkorange', linestyle='--')

    #Create directory if it does not exist
    try: 
        os.makedirs('graphs')
    except OSError:
        if not os.path.isdir('graphs'):
            raise

    #Save the figure as a png
    plt.savefig('graphs/besta' + xAxis + 'vs' + yAxis + 'A.png', dpi=400)

def graphLinear(data):
    # Define X and Y variable data
    
    for d in data:
        x = np.array([i for i in range(d['games']+1)])
        y = np.array(d['accxGDiff'])
        print(x,y)
        plt.plot(x, y)
    
    
    plt.xlabel("Games")  # add X-axis label
    plt.ylabel("accumulated net xG")  # add Y-axis label
    plt.title("Any suitable title")  # add title
    plt.savefig('graphs/bestaAccXG.png', dpi=400)

    print(graphData)