"""
Test goes here

"""

import pandas as pd
from main import development
from lib import development
from lib import plot

def test_data():
    # Test with dataset
    data= pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
    result = development(data)
    assert result == 47.790116494845364

def test_plot(data):
    data= pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
    my_chart = (so.Plot(data, x="Mortality rate, infant (per 1,000 live births)", y="GDP per capita (constant 2010 US$)")
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and infat Mortality")
    .theme({**style.library["seaborn-whitegrid"]}))
    my_chart.show()
    

if __name__ == "__main__":
    test_data()
    test_plot()
