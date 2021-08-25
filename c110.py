import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as pgo
import plotly.figure_factory as pff
import random as rd
import statistics as stats

df = pd.read_csv("csv files\c110-1.csv")
data = df["average"].tolist()

popMean = stats.mean(data)
popSD = stats.stdev(data)

def randMean(counter):
    ds = []
    for i in range(0,counter):
        rdin = rd.randint(0,len(data)-1)
        val = data[rdin]
        ds.append(val)
    mean = stats.mean(ds)
    return mean

def showFig(meanL):
    df = meanL
    mean = stats.mean(df)
    figure = pff.create_distplot([df],["temp"],show_hist = False)
    figure.add_trace(pgo.Scatter(x = [mean,mean],y = [0,1],mode = "lines"))
    figure.show()

def setup():
    meanL = []
    for i in range(0,1000):
        setM = randMean(100)
        meanL.append(setM)
    showFig(meanL)
    print(setM)

setup()

def standDev():
    meanL = []
    for i in range(0,1000):
        setM = randMean(100)
        meanL.append(setM)
    sd = stats.stdev(meanL)
    print(sd)

standDev()
