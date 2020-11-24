# %%
# Import relevant libraries
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
# %%

# Define array to evaluate Gaussian
x = np.linspace(0, 1, 200)

# Evaluate Gaussian
px_1 = norm.pdf(x, 0.4, 0.12)
px_2 = norm.pdf(x, 0.55, 0.15)

# Plot pdf
plt.plot(x, px_1, linewidth=2)
plt.plot(x, px_2, linewidth=2)

# Define places to evaluate forces
x_force = np.linspace(1E-3, 1 - 1E-3, 10)

# Evaluate selection
selection = x_force * (1 - x_force) * 0.3 

# Plot arrows
for i, pos in enumerate(x_force):
    plt.arrow(
        pos,
        4.5,
        selection[i],
        0,
        length_includes_head=True,
        shape='full',
        head_width=.1,
        head_length=0.01,
    )

# Define places to evaluate forces
x_mutation = np.linspace(0, 1, 9)

# Evaluate selection
mutation = 1E-1 * (1 - x_mutation) - 0.5E-1 * x_mutation

# Plot arrows
for i, pos in enumerate(x_mutation):
    plt.arrow(
        pos,
        4,
        mutation[i],
        0,
        length_includes_head=True,
        shape='full',
        head_width=.1,
        head_length=0.01,
    )

# Define places to evaluate forces
x_drift = np.linspace(0.1, 0.9, 10)

# Evaluate selection
drift = (1 - x_drift) * x_drift * 0.3

# Plot arrows
for i, pos in enumerate(x_drift):
    # Plot forward arrow
    plt.arrow(
        pos,
        3.5,
        drift[i],
        0,
        length_includes_head=True,
        shape='full',
        head_width=.1,
        head_length=0.01,
    )
    # Plot reverse arrow
    plt.arrow(
        pos + drift[i],
        3.5,
        - drift[i],
        0,
        length_includes_head=True,
        shape='full',
        head_width=.1,
        head_length=0.01,
    )

# Save image as SVG
plt.savefig("../../fig/spread_the_butter/diffusion_theory_schematic.svg")
# %%
