import matplotlib.pyplot as plt
import numpy as np
import paths

# Generate some data
rng = np.random.default_rng()
random_numbers = rng.random((100, 10))

# Plot and save
fig = plt.figure(figsize=(7, 6))
plt.plot(random_numbers)
plt.xlabel("x")
plt.ylabel("y")
fig.savefig(paths.figures / "random_numbers.pdf", bbox_inches="tight", dpi=300)
