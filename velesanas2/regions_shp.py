import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

shapefile_path = 'administrativas_teritorijas_2021/Administrativas_teritorijas_2021.shp'
gdf = gpd.read_file(shapefile_path)

np.random.seed(42)  # For reproducible results
gdf['random_value'] = np.random.uniform(-2, 2, len(gdf))

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Create the map
cmap = 'coolwarm'
gdf_plot = gdf.plot(column='random_value',
         cmap=cmap,  # Use a colormap that goes from cool (negative) to warm (positive)
         linewidth=0.8,
         ax=ax,
         edgecolor='0.8')


title = ax.set_title('Gender Bias by Region', fontsize=14, fontweight='bold', fontname='Times New Roman', pad=20)

# Create a divider for the existing axes instance to place the colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)  # Adjust size and padding as needed

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=-2, vmax=2))
sm._A = []  # Fake up the array for the scalar mappable
cbar = fig.colorbar(sm, cax=cax)
cbar.set_label('Value', fontsize=12, fontname='Times New Roman')  # Set the colorbar label with the specified font

# Set tick labels font
cbar.ax.yaxis.set_tick_params(labelsize=12)
cbar.ax.set_yticklabels(cbar.ax.get_yticklabels(), fontname='Times New Roman', fontsize=12)

ax.set_axis_off()

plt.savefig('gender_bias_map.png', dpi=300)

plt.show()


# if 'LABEL' in gdf.columns:
#     region_ids = gdf['LABEL'].unique()
# else:
#     raise ValueError("Please replace 'region_id' with the correct column name for your data.")

# for region_id in region_ids:
#     print(region_id)