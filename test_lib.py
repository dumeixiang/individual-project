"""
Test goes here

"""

import pandas as pd
from lib import development
#from lib import plot

def test_data():
    # Test with dataset
    data= pd.read_csv("a.csv")
    result = development(data)
    assert result == 47.790116494845364

if __name__ == "__main__":
    test_data()
   # test_plot("./a.csv")
