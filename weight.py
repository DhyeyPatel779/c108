import plotly.figure_factory as pf
import csv
import pandas as pd

df=pd.read_csv("data.csv")
graph=pf.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)

graph.show()