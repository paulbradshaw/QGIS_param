# Vibe coding in Gemini

You can [see the chat here](https://gemini.google.com/share/cf63ba133e98).

## Prompt 1: meta prompting

The first prompt uses **meta prompting** to ask Gemini to design a prompt. This contains the key information any good prompt needs:

1. The context (journalism)
2. The objective
3. Detailed instructions

```
You are an expert in prompt design. 

Suggest a prompt that could be used to help a data journalist write some Python code for QGIS. 

The journalist is working on a story on flood defences. 

The story will be used by dozens of organisations across the country. 

Each organisation will want a map for their city or region.

The journalist has shape files on flood defences and has mapped them. 

They want a script that will loop through a list of city lat-longs and export an image of the map centred on each of those. 

Some are small towns and some large cities so they want two images for each map - one with a closer zoom for smaller cities and one a bit wider for larger conurbations.
```

## Response 1

> Creating a script for automated map exports in QGIS (using the **PyQGIS** library) is a classic "work smarter, not harder" move. Since this involves spatial loops and scale logic, the prompt needs to be specific about the QGIS API classes, like `QgsLayout` and `QgsMapCanvas`.
> 
> Here is a professionally engineered prompt you can provide to an LLM to get high-quality, functional code.

---

### The Suggested Prompt

> **Copy and paste the text below:**
> 
> "I am a data journalist working in QGIS on a national flood defense story. I have a project with shapefiles already styled and a list of locations (Name, Latitude, Longitude).
> Please write a **PyQGIS script** that automates the following:
> 1. **Input Data:** Use a Python list of dictionaries or a path to a CSV containing 'CityName', 'Lat', and 'Lon'.
> 2. **Layout Setup:** Create or use a print layout template (e.g., 'FloodMap_Template').
> 3. **The Loop:** For each location:
> * Center the map on the specific Lat/Long coordinates.
> * **Export 1 (Tight Zoom):** Set the map scale to  (for small towns/detail) and export as a PNG named `{CityName}_close.png`.
> * **Export 2 (Wide Zoom):** Set the map scale to  (for large conurbations/context) and export as a PNG named `{CityName}_wide.png`.
> 
> 
> 4. **Requirements:** >     * Ensure the script handles CRS transformations (assume project is EPSG:3857 or EPSG:4326).
> * Include comments explaining how to refresh the map canvas and layout for each iteration to avoid 'ghosting' previous locations.
> * Output the files to a specific directory path."

---

### Why this prompt works

* **Explicit Scale Control:** By defining specific scales (e.g., ), you remove the ambiguity of what "close" and "wide" mean to an AI.
* **API Specifics:** Mentioning **PyQGIS** and **Layouts** ensures the AI doesn't give you generic Python code that won't run inside the QGIS Python Console.
* **The "Ghosting" Fix:** One common bug in QGIS scripting is that the map doesn't update fast enough before the export triggers. Asking for "refresh" logic forces the AI to include `iface.mapCanvas().refresh()` or similar commands.

### Pro-Tips for the Journalist

* **The Template is Key:** Tell them to create one "Print Layout" in QGIS first with their logo, legend, and a map item named "Map 1". The script will simply "drive" that layout.
* **CRS Check:** If their coordinates are in , but their map is in , the script needs to transform those points. The prompt above specifically asks the AI to handle this.

Would you like me to generate a draft of the actual Python script based on this prompt so you can test it yourself?

## Prompt 2: Agree to run the prompt

This is a simple one (but we can also run the same prompt in other LLMs):

```
Yes.
```

## Response 2:

> Since you’re ready to see the code, here is a robust PyQGIS script based on that prompt.
>
> This script is designed to be run from the Plugins > Python Console within QGIS. It assumes you have a Print Layout already created named "FloodMap_Template" with a map item inside it named "main_map".

```
import os
from qgis.core import (QgsProject, QgsCoordinateReferenceSystem, 
                       QgsCoordinateTransform, QgsPointXY, QgsUnitTypes)

# --- CONFIGURATION ---
LAYOUT_NAME = "FloodMap_Template" # The name of your Print Layout
OUTPUT_FOLDER = "C:/Users/Journalist/Desktop/Flood_Maps/" # Change this path
PROJECT_CRS = "EPSG:3857" # Standard Web Mercator (or your project CRS)

# List of locations: [Name, Lat, Lon]
locations = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Manchester", "lat": 53.4808, "lon": -2.2426},
    {"name": "Bristol", "lat": 51.4545, "lon": -2.5879}
]

# Ensure output directory exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

project = QgsProject.instance()
layout = project.layoutManager().layoutByName(LAYOUT_NAME)
map_item = layout.itemById("main_map") # Ensure your map item has this ID in the layout

# CRS Transformation: Convert Lat/Long (4326) to Project CRS
src_crs = QgsCoordinateReferenceSystem("EPSG:4326")
dest_crs = QgsCoordinateReferenceSystem(PROJECT_CRS)
transform = QgsCoordinateTransform(src_crs, dest_crs, project)

def export_map(location_name, lat, lon, scale, suffix):
    # 1. Transform coordinates
    point = QgsPointXY(lon, lat)
    transformed_point = transform.transform(point)
    
    # 2. Set map extent and scale
    map_item.setExtent(map_item.extent()) # Initialize
    map_item.setCenter(transformed_point)
    map_item.setScale(scale)
    
    # 3. Refresh and Export
    filename = f"{location_name}_{suffix}.png"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    
    exporter = QgsLayoutExporter(layout)
    settings = QgsLayoutExporter.ImageExportSettings()
    settings.dpi = 300 # High resolution for print/web
    
    result = exporter.exportToImage(filepath, settings)
    if result == QgsLayoutExporter.Success:
        print(f"Exported: {filename}")

# --- EXECUTION LOOP ---
for loc in locations:
    # Tight zoom for detail (1:25,000)
    export_map(loc['name'], loc['lat'], loc['lon'], 25000, "close")
    
    # Wide zoom for context (1:100,000)
    export_map(loc['name'], loc['lat'], loc['lon'], 100000, "wide")

print("Batch export complete!")
```

### How to use this in QGIS

> Preparation: Open your QGIS project with your flood defense layers.
> 
> Create Layout: Go to Project > New Print Layout. Name it FloodMap_Template.
> 
> Add Map: Add a map element to the page. In the "Item Properties" panel (usually on the right), find the Id field and type main_map.
> 
> Run Script: Open the Python Console (Ctrl+Alt+P), click the "Show Editor" icon (the notepad), paste the code above, and hit the green "Play" button.

### A Quick Note on "Wait Time"

> If your map layers are heavy (e.g., high-resolution LiDAR or global OSM tiles), the script might export before the tiles finish loading. If you see blank maps, we can add a time.sleep(2) command between the scale change and the export to give the renderer a moment to breathe.
> 
> Would you like me to show you how to modify this to read from a CSV file instead of typing the city list into the code?
