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

## Define time array
time = np.linspace(0, 200)

# Define function to compute allele frequency
def x_mut(t, x_init, mu_Aa, mu_aA):
    '''
    Computes the allele frequency x for the regime of deterministic
    mutation acting on a one-locus two-allele system
    '''
    mu = mu_aA + mu_Aa
    return mu_aA / mu - \
        (mu_aA - mu * x_init) * np.exp(- mu * t) / mu

# Define ranges of mutations to chose
mu_Aa = 0.01
mu_aA = [mu_Aa * 0.2 / (1 - 0.2), 0.01, mu_Aa * 0.8 / (1 - 0.8)]

# Define initial frequency
x_init = 0.1

# Initialize figure
fig = plt.figure()

# Define colors for plot
colors = sns.color_palette('Blues', n_colors=len(mu_aA) + 1)[1::]

# Loop through selection coefficients
for i, mu in enumerate(mu_aA):
    # Compute allele frequency
    x_m = x_mut(time, x_init, mu_Aa, mu)

    # Plot allele time vs allele frequency
    plt.plot(time, x_m, label=np.round(mu / (mu_Aa + mu), 2),
             color=colors[i])

 # Label axis
plt.xlabel('time (a.u.)')
plt.ylabel('allele frequency')

# Set axis limits
plt.ylim([0, 1.15])

 # Add legend
plt.legend(title=r'$\frac{\mu_{aA}}{\mu_{Aa} + \mu_{aA}}$', fontsize=6)

# Save figure
plt.savefig(figdir + '01_02_deterministic_mut.png', bbox_inches='tight',
            dpi=300)
