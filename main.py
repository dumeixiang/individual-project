"""
Main code
"""
import pandas as pd
#import numpy as np
import seaborn.objects as so
from matplotlib import style


# Download World Development Indicators
def development(data): 
    data = pd.read_csv("a.csv")
    data.describe()
    return data["a"].describe().loc['mean']

# generate Plot


def plot(data):
    my_chart = (so.Plot(data, x="a"), y="GDP per capita (constant 2010 US$)")
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and infat Mortality")
    .theme({**style.library["seaborn-whitegrid"]}))
    my_chart.show()
