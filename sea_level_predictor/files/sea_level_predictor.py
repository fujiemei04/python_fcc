import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"].to_numpy()
    y = df["CSIRO Adjusted Sea Level"].to_numpy()
    # Create scatter plot
    plt.scatter(x,y)

    # Create first line of best fit
    result = linregress(x,y)
    
   
    maxyear=x.max()
    for i in range(maxyear + 1, 2051):
        x=np.append(x,i)
    plt.plot(x,result.intercept+x*result.slope)

    # Create second line of best fit
    x_altern = df[df["Year"] >= 2000]
    y_altern = x_altern["CSIRO Adjusted Sea Level"].to_numpy()
    

    x_altern = x_altern["Year"].to_numpy()
    result2 = linregress(x_altern,y_altern)
    for i in range(maxyear + 1, 2051):
        x_altern=np.append(x_altern,i)
    plt.plot(x_altern,result2.intercept+x_altern*result2.slope)
     # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")
    
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()