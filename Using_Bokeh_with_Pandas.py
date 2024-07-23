#Making a basic Bokeh line graph with pandas

#importing Bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#Prepare some data
df=pandas.read_csv("data.csv")
x=df["x"]
y=df["y"]

#prepare the output file
output_file("Basic_Graph_with_pandas.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

#write the plot in the figure
show(f)
