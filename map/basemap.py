# Libraries for upload
# - plotly
# - kaleido
# - pillow

import plotly.express as px
from PIL import Image

# Define the center coordinates
center_lat = 37.2710
center_lon = -76.7140
access_token = 'pk.eyJ1IjoicG5lbHNvbjciLCJhIjoiY2x2OGloa2tyMGFvYjJqbnRkbXh5dnd4ZSJ9.x52_5NJmQidFPvN2pZBs6g'
# Create a Plotly figure with Mapbox satellite imagery
px.set_mapbox_access_token(access_token)
fig = px.scatter_mapbox(lat=[center_lat], lon=[center_lon], zoom=15.75,opacity=0,hover_data=None,height=600,width=800)
fig.update_layout(mapbox_style="basic")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(hovermode=False)

# Show figure
fig.write_image("initialmap.png")

# Crop base image 
base = Image.open("initialmap.png").copy()
width, height = base.size
left = 0
top = 10
right = 800
bottom = height - 30
base = base.crop((left,top,right,bottom))
base.save("base.png")