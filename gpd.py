# Import the necessary packages
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the low resolution world map
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Plot the world map
world.plot(figsize=(15, 10), color='lightblue', edgecolor='black')

# Set title and show the plot
plt.title('World Map')
plt.show()
