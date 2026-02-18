# Automating the export of images

Normally to get an image of the map, or part of the map, we would go to **Project > Import/Export > Export Map to Image...** - by default this will export a PNG image of the current view of the map.

But what if you want to do this for lots of different parts of the country?

This is a job for code. 

1. Open the project created above in QGIS  
2. Go to Plugins \> Python console  
3. The Console should open at the bottom half of the map. There are six buttons on it: hover over the third button and it should say ‘Show Editor’. Click that button to open the code editor.  
4. If the code editor doesn’t open with the file *qgis\_take\_pix.py* already open, click on the first button above that area, the ‘Open file’ button, and locate the file with that name.  
5. Press the ‘run’ button to execute the code \- the files should start to appear in the same location. This is what it does:  
   1. Import QGIS Python libraries  
   2. Store a list of lat-longs. These come from a MySociety data download: [UK Local Authorities (past and current)](https://pages.mysociety.org/uk_local_authority_names_and_codes/datasets/uk_la_past_current/latest)  

      `listofdicstocsv = [{'lat': np.float64(50.844441271809465), 'long': np.float64(-0.29853 ...`

   3. Choose a map window size

      `# choose a map window size in degrees`

      `half_w = 0.1`

      `half_h = 0.07`

   4. Set a prefix for each image:

      `out_prefix = 	"/Users/paul/Documents/wip/QGIS_floodDefences/imageexports"`

   5. Label each image:

      `# update the label text for context`

      `label.setText(f"centre: {officialname} (lon {lon:.4f}, lat {lat:.4f})")`

   6. Name each image:

      `# make a filesystem-safe version of the official name`

          `safe_name = re.sub(r'[^A-Za-z0-9._-]+', '_', officialname).strip('_')`

      `# export this page to a single image`

      `out_path = f"{out_prefix}{safe_name}.png"`

   7. Add a placemarker (there are two large code blocks that control this, one inside the loop and one outside)  
6. 

## The Python code

`print("hello script")`  
`from qgis.PyQt.QtCore import QRectF`  
`from qgis.core import (`  
    `QgsProject,`  
    `QgsVectorLayer,`  
    `QgsCoordinateReferenceSystem,`  
    `QgsPrintLayout,`  
    `QgsLayoutItemMap,`  
    `QgsLayoutItemLabel,`  
    `QgsLayoutPoint,`  
    `QgsLayoutSize,`  
    `QgsUnitTypes,`  
    `QgsLayoutExporter,`  
    `QgsRectangle`  
`)`

`# --- optional: load any layers you want visible (reuse your grid, add others, etc.) ---`  
`grid_path = "/Users/paul/Documents/wip/QGIS_floodDefences/AIMS_Spatial_Flood_Defences_inc_standardised_attributes.shp/Spatial_Flood_Defences_Including_Standardised_Attributes.shp"`  
`vlyr = QgsVectorLayer(grid_path, "grid", "ogr")`  
`if vlyr.isValid():`  
    `QgsProject.instance().addMapLayer(vlyr)`

`print("setting CRS")`  
`# --- set project CRS to WGS 84 (lon/lat in degrees) ---`  
`QgsProject.instance().setCrs(QgsCoordinateReferenceSystem("EPSG:4326"))`

`print("create simple layout")`  
`# --- create a simple layout with one big map and a small label ---`  
`project = QgsProject.instance()`  
`layout = QgsPrintLayout(project)`  
`layout.initializeDefaults()`  
`layout.setName("centres_layout")`

`map_item = QgsLayoutItemMap(layout)`  
`map_item.setFrameEnabled(True)`  
`map_item.attemptMove(QgsLayoutPoint(20, 20, QgsUnitTypes.LayoutMillimeters))`  
`map_item.attemptResize(QgsLayoutSize(257, 170, QgsUnitTypes.LayoutMillimeters))  # larger map area`  
`if vlyr.isValid():`  
    `map_item.setExtent(vlyr.extent())  # initial extent just so we see something`  
`layout.addLayoutItem(map_item)`

`label = QgsLayoutItemLabel(layout)`  
`layout.addLayoutItem(label)`  
`label.attemptMove(QgsLayoutPoint(20, 5, QgsUnitTypes.LayoutMillimeters))`

`# --- helper to make an extent centred on (lon, lat) with a buffer in degrees ---`  
`def rect_around(lon, lat, half_w_deg, half_h_deg=None):`  
    `if half_h_deg is None:`  
        `half_h_deg = half_w_deg`  
    `return QgsRectangle(lon - half_w_deg, lat - half_h_deg, lon + half_w_deg, lat + half_h_deg)`

`print("store test latlongs")`  
`# --- list of UK centres (lon, lat) ---`  
`centres = [`  
    `(-0.1276, 51.5074),   # London`  
    `(-3.1883, 55.9533),   # Edinburgh`  
    `(-2.2426, 53.4808),   # Manchester`  
    `(-1.5491, 53.8008),   # Leeds`  
    `(-3.1791, 51.4816),   # Cardiff`  
`]`

`# choose a map window size in degrees (adjust to taste)`  
`half_w = 2.0`  
`half_h = 1.5`

`exporter = QgsLayoutExporter(layout)`  
`settings = QgsLayoutExporter.ImageExportSettings()`  
`# settings.dpi = 200`

`out_prefix = "/Users/paul/Documents/wip/QGIS_floodDefences/output_"`

`for (lon, lat) in centres:`  
    `# set the map extent around the current centre`  
    `map_item.setExtent(rect_around(lon, lat, half_w, half_h))`

    `# update the label text for context`  
    `label.setText("centre: lon {0:.4f}, lat {1:.4f}".format(lon, lat))`

    `# export this page to a single image (no atlas here)`  
    `out_path = "{0}{1:.4f}_{2:.4f}.png".format(out_prefix, lon, lat)`  
    `result = exporter.exportToImage(out_path, settings)`  
    `if result != QgsLayoutExporter.Success:`  
        `raise RuntimeError("Export failed for {0}".format(out_path))`  
    `print("wrote", out_path)`

