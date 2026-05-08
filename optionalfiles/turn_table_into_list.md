# Turning a table into a list in Excel

1. [Download the CSV of cities](https://github.com/paulbradshaw/QGIS_param/blob/main/optionalfiles/gbcities.csv) and open in Excel
2. Type this formula in cell J2. It will take the lat, long and name from three cells and insert them into a Python dict: `="{'lat': np.float64("&B2&"), 'long': np.float64("&C2&"), 'officialname': '"&A2&"'}"`
3. Copy the formula down for each row. You now have a column of dicts.
4. Type this formula to join the results, with a comma between each dict (the TRUE means ignore blank cells): `=TEXTJOIN(", ",TRUE,J:J)`
5. You now have the contents of a list - you just need to delete the last comma, and add a square bracket on either side to indicate the beginning and end of the list*. 
6. In your code, type an opening and closing square bracket, and then paste the list of dicts between them.
7. Finally, delete the comma at the end of your list before the closing square bracket.

