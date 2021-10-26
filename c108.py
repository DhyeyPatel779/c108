import plotly.figure_factory as pf
import csv
import pandas as pd

df=pd.read_csv("data.csv")
graph=pf.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)

graph.show()