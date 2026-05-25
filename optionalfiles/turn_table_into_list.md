# Turning a table into a list in Excel

1. [Download the CSV of cities](https://github.com/paulbradshaw/QGIS_param/blob/main/optionalfiles/gbcities.csv) and open in Excel
2. Type this formula in cell J2. It will take the lat, long and name from three cells and insert them into a Python dict: `="{'lat': "&B2&", 'long': "&C2&", 'officialname': '"&A2&"'}"`
3. Copy the formula down for each row. You now have a column of dicts.
4. Type this formula to join the results using the [TEXTJOIN function](https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c), with a comma between each dict (the TRUE means ignore blank cells): `=TEXTJOIN(", ",TRUE,J:J)`
5. You now have the contents of a list - you just need to add a square bracket on either side to indicate the beginning and end of the list*. 
6. In your code, type an opening and closing square bracket, and then paste the list of dicts between them.

*Alternatively you can just add them in the formula like this: `="[ "&TEXTJOIN(", ",TRUE,J:J)&" ]"`
