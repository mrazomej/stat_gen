#!/usr/bin/env python
# coding: utf-8

# Deterministic selection

# (c) 2019 Manuel Razo. This work is licensed under a [Creative Commons
# Attribution License CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
# All code contained herein is licensed under an [MIT
# license](https://opensource.org/licenses/MIT)

#%%
# Import our numerical workhorse
import numpy as np
import pandas as pd

# Import matplotlib stuff for plotting
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import seaborn as sns
import statgen

#%%
# Set plotting style
statgen.viz.pboc_style_mpl()

# Define chapter name
CHAPTER = 'deterministic_evo'
# Define file description (will be attached to file name)
DESCRIPTION = 'deterministic_select'
# Define format for figure
FORMAT = 'png'

# Read list of figures for this chapter
figs = pd.read_excel('../../fig/fig_names.xlsx',
                     sheet_name=CHAPTER)

# Compose figure name given current numbering of files
chapter = int(figs[figs.fig_name == DESCRIPTION].chapter)
section = int(figs[figs.fig_name == DESCRIPTION].section)
number = int(figs[figs.fig_name == DESCRIPTION].number)
# Define plot file name
filename = f'{chapter:02d}_{section:02d}_{number:02d}_{DESCRIPTION}'

# Define output fig folder
figdir = f'../../fig/{CHAPTER}/'

#%%
# Define function to compute allele frequency
def x_select(t, x_init, s_select):
    '''
    Computes the allele frequency x for the regime of deterministic
    selection acting on a one-locus two-allele system
    '''
    return x_init * np.exp(s_select * t) / \
        (1 + x_init * (np.exp(s_select * t) - 1))

# Define time array
time = np.linspace(0, 1000, 500)

# Define ranges of selection to chose
s_select = [-0.01, -0.005, 0, 0.005, 0.01]

# Define initial frequency
x_init = 0.1

# Initialize figure
fig = plt.figure()

# Define colors for plot
colors = sns.color_palette('Blues', n_colors=len(s_select) + 1)[1::]

# Loop through selection coefficients
for i, s in enumerate(s_select):
    # Compute allele frequency
    x_s = x_select(time, x_init, s)

    # Plot allele time vs allele frequency
    plt.plot(time, x_s, label=s, color=colors[i])

 # Label axis
plt.xlabel('time (a.u.)')
plt.ylabel('allele frequency')

 # Add legend
plt.legend(title='$s$', fontsize=6)

# Save figure
plt.savefig(figdir + f'{filename}.{FORMAT}', bbox_inches='tight',
            dpi=300)
