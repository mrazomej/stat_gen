# %%
# Import relevant libraries
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
# %%

# Define array to evaluate Gaussian
x_1 = np.linspace(-3.5, 3.5, 200)
x_2 = np.linspace(-2.5, 6.5, 200)
# Evaluate Gaussian
px_1 = norm.pdf(x_1, 0, 1)
px_2 = norm.pdf(x_2, 2, 1.5)

# Plot pdf
plt.plot(x_1, px_1, linewidth=2)
plt.plot(x_2, px_2, linewidth=2)

# Save image as SVG
plt.savefig("../../fig/spread_the_butter/gaussian_pdf.svg")
# %%
