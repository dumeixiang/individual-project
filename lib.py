"""
Main code
"""
import pandas as pd
#import seaborn.objects as so
#from matplotlib import style
#import numpy as np


# Download World Development Indicators
def development(data): 
    data = pd.read_csv("a.csv")
    data.describe()
    return data["a"].describe().loc['mean']

# generate Plot



