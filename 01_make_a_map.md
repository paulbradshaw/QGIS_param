# Making the base map 

The first step is to make a base map that we can 'parameterise' from (generate multiple versions of).

We are going to make a basic map that shows flood defences.

1. Create a folder dedicated to the project, where you’ll keep all related files.  
2. Download the following shape files to that folder: go to [AIMS Spatial Flood Defences (inc. standardised attributes)](https://environment.data.gov.uk/dataset/8e5be50f-d465-11e4-ba9a-f0def148f590) and expand the **Spatial information** area. Download the file in that section named `AIMS\_Spatial\_Flood\_Defences\_inc\_standardised\_attributes.shp.zip` - then unzip that file   
3. Open QGIS and create a new project (***Project \> New***) 
4. Save it in the same folder (***Project \> Save As...***)
5. In the *Browser* area in the upper left side of the screen, scroll down to the **XYZ Tiles** section. Double-click on **OpenStreetMap** to add that base layer to your project. This should now appear in your Layers area in the lower left side.
6. Select ***Layer \> Add Layer \> Add vector layer***.
7. In the window that appears click on the … next to the **Source** section (where it says *Vector Dataset(s)*) and locate the file that you downloaded called **Spatial\_Flood\_Defences\_Including\_Standardised\_Attributes.shp**. Click **Add**. It should appear in the background behind the window. Click **OK** and then **Close** to return to that.
8. Zoom in to the area of the map (the UK) where the defences are. You need to now change the colours to make them more visible.
9. In the Layers window right-click on **OpenStreetMap** and select *Properties*.
10. Change the opacity of this layer by selecting the **Transparency** option on the left, if it's not already selected (fourth tab) and set it to 50%  
11. To change the colours of the other layer:
    1. In the Layers window right-click on **Spatial\_Flood\_Defences\_Including\_Standardised\_Attributes** and select *Properties*.   
    2. In the window that appears, select the *Symbology* section.   
    3. Change the opacity to 80% and the width to 0.4mm - or customise other options for how you want the lines to look before applying any colour coding.  
    8. Click OK to return to the map.   

You should now be able to zoom into different areas of the map to see how a particular area looks. 

This is all we need to do for now. But you'll probably want to come back and customise the map further. Here are some ideas.

## Customising the map

* **Design**: once you've tried out the map you might want to try a different style to more clearly communicate elements of the story visually. The transparency of layers, thickness of lines (or pattern), colour, etc. are all aspects you will want to make changes to see if it improves the effect.
* **Extra information/layers**: we can add extra layers to show extra information. For example we might add major cities, or data that provides information about these defences such as whether they are classified as satisfactory or not. 
* **Symbology**: once we have that extra information we can also use it to determine design, such as the colour of a line (satisfactory or unsatisfactory) etc.
