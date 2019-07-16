#!/usr/bin/env python
# coding: utf-8

# Deterministic selection

# (c) 2019 Manuel Razo. This work is licensed under a [Creative Commons
# Attribution License CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
# All code contained herein is licensed under an [MIT
# license](https://opensource.org/licenses/MIT)

# Import our numerical workhorse
import numpy as np

# Our main plotting package (must have explicit import of submodules)
import bokeh.io
import bokeh.plotting
import bokeh.layouts
from bokeh.themes import Theme
from bokeh.models import CustomJS, WidgetBox, ColumnDataSource
from bokeh.models.widgets import Slider, RadioButtonGroup
from bokeh.resources import CDN
from bokeh.embed import autoload_static

# Import the project utils
import sys
sys.path.insert(0, '../../')
import statgen

# Define output fig folder
figdir = '../../fig/deterministic_evo/'

# Define plot file name
filename = '01_01_deterministic_select'

# The first thing we need to define for the plot are the sliders that we will
# be able to manipulate. We will need two:
# 1. $s$ for the selection coefficient
# 2. $x_o$ for the initial frequency of the mutant.

# Define initial values of the parameters
x_i = 0.1
s_i = 0.01

# Define the interactions
s_select = Slider(title='s', start=-0.03, end=0.03, step=.0001, value=s_i,
                  format="0[.]0000")
x_init = Slider(title='x\u2092', start=0, end=1, step=0.01, value=x_i)

# Now we are ready to prepare the data for the plot. Fro the very simple plot
# we want to generate all the data we need is a range of $t$ time values. We
# will generate a `data source` for `bokeh`. This is the equivalent to a
# `pandas` dataframe where we could put different sources of data. This `data
# source` will include a precomputed allele frequency such that when the plot
# is first rendered it is not empty. So we will define a `python` function to
# compute this initial allele frequency. In the next step we will re-define the
# function in `javascript` such that the plot can be updated without the need
# of a `python` kernel.

# Define time array
time = np.linspace(0, 1000, 500)

# Define function to compute allele frequency
def x_select(t, x_init, s_select):
    '''
    Computes the allele frequency x for the regime of deterministic
    selection acting on a one-locus two-allele system
    '''
    return x_init * np.exp(s_select * t) / \
        (1 + x_init * (np.exp(s_select * t) - 1))

# Generate bokeh data source
source = ColumnDataSource({'time': time,
                           'x_allele': x_select(time, x_i, s_i)})

# Now we need to define the `JavaScript` callback function. We will define it
# using `JavaScript` such that the function can exists as its own standing HTML
# object without the need for a `python` kernel to render it. Since our
# function is very simple we can compute this very easily

# Define JavaScript callback function
cb_script = """
// Variable definition
var data = source.data; 
var s_select = sSlider.value;
var x_init = xoSlider.value;

// Function definition
function x_select(t, x_init, s_select){
    var updated_val =  x_init * Math.exp(s_select * t) / 
    (1 + x_init * (Math.exp(s_select * t) - 1));
    return updated_val;
}

// Update values using a for loop (since I don't know how to do 
// vectorized oprations)
var updated_allele = []; // temporary variable to update values
for (var i = 0; i < data['time'].length; i++){
    updated_allele[i] = x_select(data['time'][i], x_init, s_select);
}
// update x_allele column entry in source
data['x_allele'] = updated_allele

// Emit data source for plot to be updated
source.change.emit();
"""

# Done! Not too bad. Now let's define the arguments for the callback function

# Define arguments for JavaScript callback function
cb_args = {'source': source, 'sSlider': s_select, 'xoSlider': x_init}
# Asign arguments to function
cb = CustomJS(args=cb_args, code=cb_script)

# Now we must assign this callback function to each of the sliders. What this means is that we must indicate that every time the slider value is changed, the `JavaScript` callback function must be executed.

# Assign callback function to widgets
x_init.callback = cb
s_select.callback = cb
x_init.js_on_change('value', cb)
s_select.js_on_change('value', cb)

# Alright. Now everything is setup for our interactive plot! Now we just need to define the bokeh plot.

# Define bokeh axis
x_allele_ax = bokeh.plotting.figure(width=300, height=275,
                                    x_axis_label='time (a.u.)',
                                    y_axis_label='allele frequency',
                                    y_range=[-0.05, 1.05])

# Populate the plot with our line coming from the Data Source
x_allele_ax.line(x='time', y='x_allele', line_width=2, source=source)

# Define the theme to be the dictionary we generated
theme = Theme(json=statgen.viz.pboc_style_bokeh())
# Asign the teme to the bokeh plot
bokeh.io.curdoc().theme = theme

# Generate figure
fig = bokeh.layouts.column(x_init, s_select, x_allele_ax)

# Generate script and div to include in HTML website
js, tag = autoload_static(fig, CDN, figdir + filename + '.js')

# Open file to save script and div
f_js= open(figdir + filename + '.js', 'w+')
f_tag = open(figdir + filename + '_div.html', 'w+')

# Write script and div into files
f_js.write(js)
f_js.close()

f_tag.write(tag)
f_tag.close()

# Define output file
bokeh.plotting.output_file(figdir + filename + '.html')

# Save stand-alone HTML figure
bokeh.io.save(fig)