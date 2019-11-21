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
DESCRIPTION = 'deterministic_mut'
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
plt.savefig(figdir + f'{filename}.{FORMAT}', bbox_inches='tight',
            dpi=300)
