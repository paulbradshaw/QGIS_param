#we print this text at the start and others so we can tell what point the script is at
print("script is now running")

# Load tools that allow us to control QGIS maps and layouts from this script
from qgis.PyQt.QtCore import QRectF
from qgis.core import (
    QgsProject, QgsCoordinateReferenceSystem, QgsPrintLayout, QgsLayoutItemMap,
    QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes, QgsLayoutItemLabel,
    QgsLayoutExporter, QgsRectangle
)

# Load some libraries (collections of code for tackling particular problems)
# math and numpy tackle numerical problems, re (regex) for text, os for file navigation
import math, re
import numpy as np
import os
print("imported libraries")

# --- optional: load layers ---
# replace this with the path on your computer to the shp file you want added as a layer
# grid_path = "/Users/paul/Downloads/QGIS_floodDefences/AIMS_Spatial_Flood_Defences_inc_standardised_attributes.shp/Spatial_Flood_Defences_Including_Standardised_Attributes.shp"
# vlyr = QgsVectorLayer(grid_path, "grid", "ogr")
# if vlyr.isValid():
#     QgsProject.instance().addMapLayer(vlyr)

# Use the os library to create a folder on your computer to save the exported map images into.
# It will be placed in your Downloads folder, inside a sub-folder called "qgis_images".
# If the folder already exists, this does nothing — it won't overwrite anything.
out_dir = os.path.join(os.path.expanduser("~"), "Downloads", "qgis_images")
os.makedirs(out_dir, exist_ok=True)
out_prefix = out_dir + "/"

# To override the folder set up earlier uncomment and adapt the line below
# out_prefix = "/Users/paul/Downloads/testqgis/images/"

print("setting CRS")
# Tell QGIS to use the same CRS as the flood defence data. This ensures map scales are reliable and exports more consistent
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem("EPSG:27700"))

print("create simple layout")
# Get the currently open QGIS project so we can add things to it.
project = QgsProject.instance()

# Create a new blank print layout (which we will fill for printing)
layout = QgsPrintLayout(project)
layout.initializeDefaults()  # Set it up with sensible default settings
layout.setName("centres_layout")  # Give the layout a name

# Add a map panel to the layout — this is the rectangle that will actually show the map.
map_item = QgsLayoutItemMap(layout)
map_item.setFrameEnabled(True)  # Draw a border around the map panel

# Position the map panel 20mm from the left and 20mm from the top of the page.
map_item.attemptMove(QgsLayoutPoint(20, 20, QgsUnitTypes.LayoutMillimeters))

# Set the map panel to be 257mm wide and 170mm tall (roughly A4 landscape minus margins).
map_item.attemptResize(QgsLayoutSize(257, 170, QgsUnitTypes.LayoutMillimeters))

layout.addLayoutItem(map_item)  # Add the map panel to the layout page

# Add a text label to the layout, which will show the name and coordinates of each location.
label = QgsLayoutItemLabel(layout)
layout.addLayoutItem(label)

# Position the label near the top of the page (20mm from left, 5mm from top).
label.attemptMove(QgsLayoutPoint(20, 5, QgsUnitTypes.LayoutMillimeters))


# def creates a function (a recipe) that we can use later. 
# This function calculates a rectangular map area centred on a given point. 
# It needs to be provided with these ingredients: lon, lat (the longitude and latitude of the centre point); half_w_deg (how far left and right to show, in degrees) and half_h_deg (how far up and down to show. If not given, this will be the same as left/right)
# It returns a rectangle that can be used to set what the map is looking at.

def rect_around(lon, lat, half_w_deg, half_h_deg=None):
    if half_h_deg is None:
        half_h_deg = half_w_deg
    return QgsRectangle(lon - half_w_deg, lat - half_h_deg,
                        lon + half_w_deg, lat + half_h_deg)


print("store test latlongs")
# Create a list of locations to map. Each item has a latitude, longitude, and a name.
# We start with just two items for testing, but once we get it working, we would expand it to all locations we want to create images for
listofdicstocsv = [
    {'lat': np.float64(50.844441271809465), 'long': np.float64(-0.2985307978506628), 'officialname': 'Adur District Council'},
    {'lat': np.float64(54.71108952940033),  'long': np.float64(-3.2472347297148736), 'officialname': 'Allerdale Borough Council'}
]


# Set how much of the surrounding area to show around each location.
# These values are in degrees — smaller numbers zoom in more.
# half_w controls the east–west spread; half_h controls the north–south spread.
half_w = 0.1
half_h = 0.07

# Set up the tool that will save the layout as an image file.
exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.ImageExportSettings()
# settings.dpi = 200  # Uncomment this line to increase the image resolution

print("entering loop")
# Go through each location in the list, one at a time, and export a map image for it.
for rec in listofdicstocsv:

    # Read the latitude, longitude, and name for this location.
    lat = float(rec.get('lat', float('nan')))   # 'nan' means "not a number" — used as a stand-in if the value is missing
    lon = float(rec.get('long', float('nan')))
    officialname = rec.get('officialname', 'unknown')

    # If either the latitude or longitude is missing, skip this location and move on.
    if math.isnan(lat) or math.isnan(lon):
        print(f"skipping '{officialname}': missing lat/long")
        continue

    # Move the map view so it's centred on this location, showing the area defined by half_w and half_h.
    map_item.setExtent(rect_around(lon, lat, half_w, half_h))

    # Update the text label on the layout to show the current location's name and coordinates.
    label.setText(f"centre: {officialname} (lon {lon:.4f}, lat {lat:.4f})")

    # Tell QGIS to redraw the map with the new location and label before we export it.
    map_item.refresh()

    # Use the regex (re) library to turn location name into something safe to use as a file name:
    # replace any special characters or spaces with underscores.
    safe_name = re.sub(r'[^A-Za-z0-9._-]+', '_', officialname).strip('_')

    # Build the full file path for this image, e.g. ".../Adur_District_Council.png"
    out_path = f"{out_prefix}{safe_name}.png"

    # Export the current layout view as a PNG image.
    result = exporter.exportToImage(out_path, settings)

    # If the export didn't work, stop the script and show an error message.
    if result != QgsLayoutExporter.Success:
        raise RuntimeError(f"Export failed for {out_path}")

    print("wrote", out_path)
