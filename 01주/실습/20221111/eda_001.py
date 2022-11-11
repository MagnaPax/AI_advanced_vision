import sweetviz as sv
import pandas as pd

my_dataframe = pd.read_csv("data/train.csv")
my_report = sv.analyze(my_dataframe)
# my_report.show_html("data/sweetviz_example.html")
my_report.show_html()
