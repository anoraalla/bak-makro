import geopandas as gpd

# Load the shapefile
shapefile_path = 'administrativas_teritorijas_2021/Administrativas_teritorijas_2021.shp'
gdf = gpd.read_file(shapefile_path)

# Display the first few rows of data to identify the correct column
print(gdf.head())

# Assuming 'region_id' is the name of the column storing region IDs:
# If the actual column name is different, replace 'region_id' with the correct name.
if 'region_id' in gdf.columns:
    region_ids = gdf['region_id'].unique()
else:
    # Replace 'region_id' with the name of the actual column found in your data
    raise ValueError("Please replace 'region_id' with the correct column name for your data.")

# List all unique region IDs
for region_id in region_ids:
    print(region_id)