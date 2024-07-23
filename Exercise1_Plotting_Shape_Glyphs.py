#This is plotting different shape glyphs

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#Prepare some data
x=[3,7.5,10]
y=[3,6,9] 

#prepare the output file
output_file("Circle_Glyphs.html")

#create a figure object
f=figure()

#create circle glyphs
f.circle(x,y)

#write the plot in the figure
show(f)


#prepare the output file
output_file("Triangle_Glyphs.html")

#create a figure object
f=figure()

#create triangle glyphs
f.triangle(x,y)

#write the plot in the figure
show(f)