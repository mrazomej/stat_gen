#!/usr/bin/env python
# coding: utf-8

#%% [markdown]
# ## Random walker

# (c) 2019 Manuel Razo. This work is licensed under a [Creative Commons
# Attribution License CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
# All code contained herein is licensed under an [MIT
# license](https://opensource.org/licenses/MIT)

#%%
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
figdir = '../../fig/drift_langevin/'
#%% [markdown]

# ## Langevin equation
# Our task for this script is to simulate a random walker in 1D that follows
# the dynamics of the form
# $$
# {dx \over dt} = -\gamma x(t) + \xi(t),
# $$
# where $\gamma$ is the restoration force, and $\xi(t)$ is white noise with
# properties
# $$
# \left\langle \xi(t) \right\rangle = 0,
# $$
# and
# $$
# \left\langle \xi(t) \xi(t') \right\rangle = 2D \delta(t-t').
# $$
# where $D$ is the diffusion coefficient. We have shown already that the
# average position of the random walker is given by
# $$
# \left\langle x(t) \right\rangle = x_o e^{-\gamma t}.
# $$
# We also showed that the variance of the position $\sigma^2(x(t))$ is given by
# $$
# \sigma^2(x(t)) = {D \over \gamma} \left( 1 - e^{-2 \gamma t} \right).
# $$
# So our task now is to simulate a random walker that follows this stochastic
# differential equation and compare the statistics of the trajectories to our
# analytical results.
#%% [markdown]
# ### Numerical implementation of a Langevin equation
# Let's now discuss how we are going to numerically simulate these stochastic
# dynamics.

#%%
