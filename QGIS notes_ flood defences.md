# QGIS notes: flood defences

## Mapping the defences and rivers

1. Create a folder dedicated to the project, where you’ll keep all related files.  
2. Download the following shape files to that folder:  
   1. Go to [AIMS Spatial Flood Defences (inc. standardised attributes)](https://environment.data.gov.uk/dataset/8e5be50f-d465-11e4-ba9a-f0def148f590) and download the file named AIMS\_Spatial\_Flood\_Defences\_inc\_standardised\_attributes.shp.zip  
   2. Unzip that file   
   3. Go to [OS Open Rivers](https://www.data.gov.uk/dataset/dc29160b-b163-4c6e-8817-f313229bcc23/os-open-rivers1) and download the file [Shapefile download](https://api.os.uk/downloads/v1/products/OpenRivers/downloads?area=GB&format=ESRI%C2%AE+Shapefile&redirect) (no longer needed)   
   4. Unzip that file  
   5. Download a list of major UK cities and their lat-longs. One can be found at [https://simplemaps.com/data/gb-cities](https://simplemaps.com/data/gb-cities) but it lacks places like Bolton and Exeter while including smaller suburbs. The list at [https://time-ok.com/coordinates/england](https://time-ok.com/coordinates/england) is slightly better but has to be pasted into a CSV file first. Consider removing London as it is too big to have a single point, and areas of London like Basingstoke are also included.  
3. Download the data on flood defences compiled by the BBC Shared Data Unit. This is in a spreadsheet called ‘*July 25 spatial defences.xlsb.xlsx*’, in a sheet called ‘*Just EA mantained USE THIS*’. This sheet has also been saved as a CSV called [*defences\_classification.csv*](https://docs.google.com/document/d/1e-WF__CfjiclJaAuzLcFHP2Q6bVdmH5nZk8DTZbv5gM/edit?tab=t.0#heading=h.72l6plttbkq0)  
4. Create new project in QGIS (***Project \> New***) and save it in a folder on your laptop   
5. Select ***Layer \> Add Layer \> Add vector layer***. In the window that appears click on the … next to the **Source** section (where it says *Vector Dataset(s)*) and locate the file that you downloaded called **Spatial\_Flood\_Defences\_Including\_Standardised\_Attributes.shp**. Click *Add*. It should appear in the background behind the window. Click *Close* to return to that.  
6. Select ***Layer \> Add Layer \> Add vector layer***. In the window that appears click on the … next to the **Source** section (where it says *Vector Dataset(s)*) and locate the file that you downloaded called **WatercourseLink.shp** \- you’ll find this in the unzipped folder oprvrs\_essh\_gb, then the subfolder ‘data’. Click *Add*. It should appear in the background behind the window. Click *Close* to return to that.   
   1. *Note: the HydroNode.shp file seems to contain nodes along the course of each watercourse, so might also be useful.*   
7. Select ***Layer \> Add Layer \> Add Delimited Text Layer***. In the window that appears click on the … next to the *File Name* box and locate the data on flood defences (*defences\_classification.csv*). Click *Add*. It should appear in the background behind the window. Click *Close* to return to that.   
   1. You should now have three layers in the Layers window in the bottom right corner: two shape layers and one table layer.  
8. Join the two datasets on flood defences as follows:   
   1. in the Layers window (bottom left) right-click on **Spatial\_Flood\_Defences\_Including\_Standardised\_Attributes** and select *Properties*.   
   2. In the window that appears go to the *Joins* section.  
   3. Click the \+ button in the bottom left to create a new join  
   4. On the window that appears check that the *Join Layer* dropdown specifies the table on defences\_classification  
   5. Check that the two dropdowns under that specify asset\_id as the join field and the target field  
   6. You can tick the *Joined fields* option and select which fields you want to bring in from the table (we only need is less than, is failing, is POOR).  
   7. Click OK, and OK again, to return to the map. Nothing will have obviously changed, but the new fields should now be in the shape layer and can be used next.  
9. In the Layers window, untick the WatercourseLink layer so it’s not visible for now.  
10. To change the colours of the other layer:   
    1. In the Layers window right-click on **Spatial\_Flood\_Defences\_Including\_Standardised\_Attributes** and select *Properties*.   
    2. In the window that appears, select the *Symbology* section.   
    3. Change the opacity to 80% and the width to 0.4mm \- or customise other options for how you want the lines to look before applying any colour coding.  
    4. Right at the top is a dropdown menu set to ‘Single Symbol’. Change this to *Categorized*.  
    5. The window will now be blank. In the *Value* dropdown select the **defences\_classification\_is\_failing** field to use this as the basis of colour-coding  
    6. Click on **Classify** in the bottom left corner. The empty area in the middle should now have 3 entries \- one for each value from that column \- with a symbol for each (a different coloured line)  
    7. Double-click on any symbol to customise it (e.g. red for bad, green for good, grey/dotted for no data)  
    8. Click OK to return to the map.   
11. [To add satellite or OpenStreetMap](https://ongeo-intelligence.com/blog/satellite-basemaps-qgis):  
    1. In the ‘Browser’ area to the right of the map, scroll down to the **XYZ Tiles** button and expand that.  
    2. Right-click on **OpenStreetMap** and select **Add layer to project**  
    3. It should now appear in the layers, and on the map. However, other layers may now be hidden  
    4. In the Layers area to the bottom right of the map, right-click on the OpenStreeMap layer and select **Move to bottom**  
    5. Change the opacity by right-clicking on the layer and opening **Properties**: select the **Transparency** option on the left (fourth tab) and set it to 50%  
12. To add major cities:  
    1. Select ***Layer \> Add Layer \> Add Delimited Text Layer***. In the window that appears click on the … next to the *File Name* box and locate the CSV with GB cities (*gb.csv*).   
    2. Expand the *Geometry Definition* area and tick **Point coordinates**.  
    3. New boxes should appear for you to specify an X field and a Y field. Select the following:  
       1. X field: lng  
       2. Y field: lat  
    4. Click *Add*. It should appear in the background behind the window. Click *Close* to return to that.   
    5. Right-click on that layer and select **Properties**  
    6. Select **Symbology** to change the marker used for each point. We used *dot white*, set to 2.00mm and 50% opacity.  
    7. Select **Labels** to add the name. Change the dropdown at the top to ‘**Single Labels**’ and click OK.  
13. 

## Automating the export of images

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

