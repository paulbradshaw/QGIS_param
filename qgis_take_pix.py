print("hello script")
from qgis.PyQt.QtCore import QRectF
from qgis.core import (
    QgsProject, QgsCoordinateReferenceSystem, QgsPrintLayout, QgsLayoutItemMap,
    QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes, QgsLayoutItemLabel,
    QgsLayoutExporter, QgsRectangle
)
# imports
import math, re
import numpy as np
print("imported libraries")

# --- optional: load layers (kept commented as per your note) ---
# grid_path = "/Users/paul/Documents/wip/QGIS_floodDefences/AIMS_Spatial_Flood_Defences_inc_standardised_attributes.shp/Spatial_Flood_Defences_Including_Standardised_Attributes.shp"
# vlyr = QgsVectorLayer(grid_path, "grid", "ogr")
# if vlyr.isValid():
#     QgsProject.instance().addMapLayer(vlyr)

# import os to create local folders
import os
out_dir = os.path.join(os.path.expanduser("~"), "Downloads", "qgis_images")
os.makedirs(out_dir, exist_ok=True)
out_prefix = out_dir + "/"
# end of code for making folder

print("setting CRS")
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem("EPSG:4326"))

print("create simple layout")
project = QgsProject.instance()
layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName("centres_layout")

map_item = QgsLayoutItemMap(layout)
map_item.setFrameEnabled(True)
map_item.attemptMove(QgsLayoutPoint(20, 20, QgsUnitTypes.LayoutMillimeters))
map_item.attemptResize(QgsLayoutSize(257, 170, QgsUnitTypes.LayoutMillimeters))
# if vlyr.isValid():
#     map_item.setExtent(vlyr.extent())
layout.addLayoutItem(map_item)

label = QgsLayoutItemLabel(layout)
layout.addLayoutItem(label)
label.attemptMove(QgsLayoutPoint(20, 5, QgsUnitTypes.LayoutMillimeters))

# helper: extent centred on (lon, lat) with buffer (degrees)
def rect_around(lon, lat, half_w_deg, half_h_deg=None):
    if half_h_deg is None:
        half_h_deg = half_w_deg
    return QgsRectangle(lon - half_w_deg, lat - half_h_deg,
                        lon + half_w_deg, lat + half_h_deg)

print("store test latlongs")
# (your long list of dicts)
listofdicstocsv = [
    {'lat': np.float64(50.844441271809465), 'long': np.float64(-0.2985307978506628), 'officialname': 'Adur District Council'}, {'lat': np.float64(54.71108952940033), 'long': np.float64(-3.2472347297148736), 'officialname': 'Allerdale Borough Council'}
]


# choose a map window size in degrees (adjust to taste)
half_w = 0.1
half_h = 0.07

exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.ImageExportSettings()
# settings.dpi = 200

out_prefix = "/Users/paul/Downloads/testqgis/images/"

print("entering loop")
# --- MAIN LOOP (no marker layer anymore) ---
for rec in listofdicstocsv:
    lat = float(rec.get('lat', float('nan')))
    lon = float(rec.get('long', float('nan')))
    officialname = rec.get('officialname', 'unknown')

    if math.isnan(lat) or math.isnan(lon):
        print(f"skipping '{officialname}': missing lat/long")
        continue

    # set the map extent around the current centre
    map_item.setExtent(rect_around(lon, lat, half_w, half_h))

    # update the layout label (kept with name + coords)
    label.setText(f"centre: {officialname} (lon {lon:.4f}, lat {lat:.4f})")

    # refresh so the new extent/label are rendered
    map_item.refresh()

    # filesystem-safe file name
    safe_name = re.sub(r'[^A-Za-z0-9._-]+', '_', officialname).strip('_')

    # export this page to a single image
    out_path = f"{out_prefix}{safe_name}.png"
    result = exporter.exportToImage(out_path, settings)
    if result != QgsLayoutExporter.Success:
        raise RuntimeError(f"Export failed for {out_path}")
    print("wrote", out_path)
