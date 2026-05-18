#add a print command so we can follow progress in the QGIS console
print("running script")
#import QGIS Python libraries 
from qgis.PyQt.QtCore import QRectF
from qgis.core import (
    QgsProject, QgsCoordinateReferenceSystem, QgsPrintLayout, QgsLayoutItemMap,
    QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes, QgsLayoutItemLabel,
    QgsLayoutExporter, QgsRectangle,
    QgsCoordinateTransform, #for transforming lat long into EPSG 27700
    QgsPointXY #for transforming lat long into EPSG 27700
)
# import math to deal with numbers, re to deal with text in filenames etc.
import math, re
# import os to create local folders
import os
print("imported libraries")


#set the directory we want to use
out_dir = os.path.join(os.path.expanduser("~"), "Downloads", "qgis_images")
#make that directory
os.makedirs(out_dir, exist_ok=True)
#store it
out_prefix = out_dir + "/"
# end of code for making folder

#set the Coordinate Reference System (CRS) - EPSG:4326 is used for GPS 
#but 27700 is used for UK flood defences so we use this to make the map more rigorous
print("setting CRS")
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem("EPSG:27700"))


#Using EPSG:27700 means we need to convert lat/long into British National Grid coordinates
# first set the source (EPSG:4326) and destination systems (EPSG:27700)
source_crs = QgsCoordinateReferenceSystem("EPSG:4326")
dest_crs = QgsCoordinateReferenceSystem("EPSG:27700")
#then create the transformer that uses those two
transformer = QgsCoordinateTransform(
    source_crs,
    dest_crs,
    project
)


#create layout
print("create simple layout")
project = QgsProject.instance()
layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName("centres_layout")


#put a map panel on that layout
map_item = QgsLayoutItemMap(layout)
#add a border
map_item.setFrameEnabled(True)
#position the map panel 20mm from left and top
map_item.attemptMove(QgsLayoutPoint(20, 20, QgsUnitTypes.LayoutMillimeters))
#size the map 257mm x 170mm
map_item.attemptResize(QgsLayoutSize(257, 170, QgsUnitTypes.LayoutMillimeters))
#add that map to the layout
layout.addLayoutItem(map_item)


#create a label for the map
label = QgsLayoutItemLabel(layout)
layout.addLayoutItem(label)
#position the label from the left and top
label.attemptMove(QgsLayoutPoint(20, 5, QgsUnitTypes.LayoutMillimeters))


#create a function which will create a rectangle centred on a coordinate
#it takes 4 ingredients and names them
def rect_around(x, y, half_width, half_height=None):
    # If no height is provided,
    # use the same value as width
    if half_height is None:
        half_height = half_width
    # Return a rectangle object that uses those
    return QgsRectangle(
        x - half_width,
        y - half_height,
        x + half_width,
        y + half_height
    )


print("store test latlongs")
#store a list of dicts - currently only two but can be replaced with more
#each dict has a lat, long and name
listofdicstocsv = [
    {'lat': 50.844441271809465, 'long': -0.2985307978506628, 'officialname': 'Adur District Council'}, 
    {'lat': 54.71108952940033, 'long': -3.2472347297148736, 'officialname': 'Allerdale Borough Council'}
]


# SET MAP SCALE (replaces width and height)
# We are now controlling zoom properly using cartographic scale.
# 175000 means 1 unit on the map = 175000 units in the real world

MAP_SCALE = 175000


#The exporter saves the layout as image files
exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.ImageExportSettings()
# settings.dpi = 200

# SET OUTPUT IMAGE SIZE
# 1000px x 600x
settings.imageSize = QSize(1000, 600)


print("entering loop")
#Now we loop through that list of dicts containing each location
for rec in listofdicstocsv:
    #fetch each item in the dict and store them in a new variable
    lat = rec.get('lat', float('nan'))
    lon = rec.get('long', float('nan'))
    officialname = rec.get('officialname', 'unknown')
    #if the lat or long are empty, skip this dict
    if math.isnan(lat) or math.isnan(lon):
        print(f"skipping '{officialname}': missing lat/long")
        continue
    # set the map extent around the current centre
    # which means we need to convert the lat/lngs into British National Grid using that transformer
    transformed_point = transformer.transform(
        QgsPointXY(lon, lat)
    )
    # Extract transformed coordinates
    x = transformed_point.x()
    y = transformed_point.y()
    #Create a temporary rectangle around the point to centre it
    map_item.setExtent(
        rect_around(x, y, 1000, 1000)
    )
    #Set a scale to control the zoom. Each map will use that.
    map_item.setScale(MAP_SCALE)
    #add a label with that info
    label.setText(
        f"{officialname} | scale 1:{MAP_SCALE:,}"
    )
    #refresh the map before exporting
    map_item.refresh()
    #give a file name - remove any tricky characters
    safe_name = re.sub(
        r'[^A-Za-z0-9._-]+',
        '_',
        officialname
    ).strip('_')
    #use that to determine the path to save to
    out_path = (
        f"{out_prefix}"
        f"{safe_name}.png"
    )
    #and export to that path
    result = exporter.exportToImage(
        out_path,
        settings
    )
    #if it's not a success
    if result != QgsLayoutExporter.Success:
        #show an error message
        raise RuntimeError(f"Export failed for {out_path}")
    #print a message at the end of each loop
    print("wrote", out_path)

#and print at the end of the whole thing
print("script finished")