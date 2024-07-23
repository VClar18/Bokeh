#Making a basic Bokeh line graph with pandas

#importing Bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#Prepare some data
df=pandas.read_csv("bachelors.csv")
x=df["Year"]
y=df["Engineering"]

#prepare the output file
output_file("Exercise2_Plotting_Education.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

#write the plot in the figure
show(f)
