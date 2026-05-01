import numpy as np
import matplotlib.pyplot as plt

# Categories
labels = [
    "Functional Suitability",
    "Performance Efficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# App ratings
whatsapp = [5, 5, 5, 4, 5, 5, 5, 5]
imo = [4, 3.5, 3, 4, 3.5, 3, 3.5, 3]

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the loop
whatsapp += whatsapp[:1]
imo += imo[:1]
angles += angles[:1]

# Create plot
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

ax.plot(angles, whatsapp, linewidth=2)
ax.fill(angles, whatsapp, alpha=0.2)

ax.plot(angles, imo, linewidth=2)
ax.fill(angles, imo, alpha=0.2)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_title("WhatsApp vs IMO - Quality Comparison Radar Chart")

plt.show()