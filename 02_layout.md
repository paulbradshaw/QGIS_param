# Creating a print/image layout

1. Zoom to the part of the map you want to create an image of (or a part similar to how you will want to, e.g. zoomed on a town)
2. Go to **Project > New Print Layout...** 
3. A window should open asking you to name the new layout. Give it a name (e.g. cityzoom) and click **OK**
4. The layout window should now appear with a blank canvas. Click the Add Map button on the left (it is a page icon with a green plus)
5. Click and drag across the whole canvas to draw the area where you want your map to appear. It should take a moment to render the map you were looking at.
6. Go to the Item Properties tab on the right side and scroll down to *Position and Size*. Alter this to any dimensions you want your image to be (change the measure to pixels if it's for web). *Make a note of these numbers because you may need it for any code later*
7. Use the *Main Properties* area at the top to see what the current **scale** is, and change that to a simpler rounded number. *Make a note of this number because you will need it for any code later*
8. Switch to the the Layout Tab next to that, and scroll down to the **Resize layout** button. Click it. The image should now take up the whole canvas (you can zoom in by using the zoom buttons in the upper left corner)
9. When you are happy with the image go to **Layout > Export as Image**
10. Close the Print Layout window and return to the QGIS project
