#Making a basic Bokeh line graph

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#Prepare some data
x=[1,2,3,4,5]
y=[6,7,8,9,10] #note that these two pairs need to have the same number of pairs or there will be an error

#prepare the output file
output_file("Basic_Graph.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

#write the plot in the figure
show(f)
