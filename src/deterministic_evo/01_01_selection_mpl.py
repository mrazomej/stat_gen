#!/usr/bin/env python
# coding: utf-8

# Deterministic selection

# (c) 2019 Manuel Razo. This work is licensed under a [Creative Commons
# Attribution License CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
# All code contained herein is licensed under an [MIT
# license](https://opensource.org/licenses/MIT)

# Import our numerical workhorse
import numpy as np

# Import matplotlib stuff for plotting
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

# Seaborn, useful for graphics
import seaborn as sns

# Import the project utils
import sys
sys.path.insert(0, '../../')
import statgen

# Set plotting style
statgen.viz.pboc_style_mpl()

# Define output fig folder
figdir = '../../fig/deterministic_evo/'

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
plt.savefig(figdir + '01_01_deterministic_select.png', bbox_inches='tight',
            dpi=300)
