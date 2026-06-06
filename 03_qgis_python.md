# Automating the export of images

Normally to get an image of the current view of the map we would either go to **Project > Import/Export > Export Map to Image...** or go to **Project > New Print Layout...**. 

But what if you want to do this for lots of different parts of the country?

This is a job for code. 

## Download the Python script

I've written a Python script that will generate multiple images from our map. It is called `qgis_take_pix.py` and is [located here](https://github.com/paulbradshaw/QGIS_param/blob/main/qgis_take_pix.py). 

To download it, click the three dots in the upper right corner and select **Download**, or click **Raw** to see the [raw file](https://raw.githubusercontent.com/paulbradshaw/QGIS_param/refs/heads/main/qgis_take_pix.py) and click **File > Save As...** in your browser. Save the file in the project folder you've been using for this QGIS project.

Check that folder to make sure it ends in `.py` - if it doesn't, repeat the steps above, making sure you open the *Raw* version of the file, not the HTML preview (which would end in `.html`). Alternatively, you can click on the three dots in the upper right corner of the [page](https://github.com/paulbradshaw/QGIS_param/blob/main/qgis_take_pix.py) and select **Download** to download the Python file.

## Edit the script to point at your folder

The script was written for my laptop, so it points to the Downloads folder, and then creates a sub-folder called "qgis_images". This may not work on your laptop, or you might not want to put it there. In either case, you'll need to uncomment and change one line of code to point to your own folder.

The line in question is this:

`# out_prefix = "/Users/paul/Downloads/testqgis/images/"`

Delete the `#` to uncomment that line (change it from a comment to working code). Then change the path in quotation marks to one that works on your machine.

To find out the path to your folder, right click on it and select **Get info** (on a Mac). The window that appears will show you the path under *Where:* 

## Opening the Python console to run a script

1. In QGIS, with your project still open, go to **Plugins > Python console**
2. The Console should open at the bottom half of the map. The console is a window that shows any code (in this case Python) that you might be running. There are six buttons at the top of this window: hover over the third button (a document icon with a pencil) and it should say ‘Show Editor’. Click that button to open the code editor to the right of the console.  
3. This new area also has a series of buttons. The first button should be a yellow folder (‘Open file’): click on that the button, and locate the `qgis_take_pix.py` file you downloaded from [here](https://raw.githubusercontent.com/paulbradshaw/QGIS_param/refs/heads/main/qgis_take_pix.py).
4. The file should now be shown in a tab below, with the name `qgis_take_pix.py`
5. Press the green ‘run’ button above it to execute the code. You should see some things appear in the console to the left - these are the results of `print` commands in the script, but also any errors will appear here too. If it works, you should see some images appear in your folder.

## What the code does

This is what it does:  

1. Specifies a folder to store all the images
2. Stores a list of lat-longs
3. Creates a transformer to convert those to the projection used by your shape files (the coordinate reference system, or CRS)
4. Sets a map size and scale
5. Loops through each location in the list, zooms to that scale, and adds a label with the location and scale
6. Sets a filename that includes the name of the location
7. Exports an image with that name (for each location in the list)

