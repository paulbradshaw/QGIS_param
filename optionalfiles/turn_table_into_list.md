# Turning a spreadsheet table into a Python list

## The online tool method

There are plenty of online tools which will convert a CSV file into a list of dictionaries (typically exported as a JSON file). The website [CSV2JSON](https://csvjson.com/csv2json) is especially useful for our purposes because it provides the list of dictionaries as text which can be copied directly, rather than having to download it as a file. 

These tools tend to appear and disappear, so if that link is no longer working, search for 'CSV to JSON converter' and find a tool that works for you. 

## The spreadsheet method

A more environmentally-friendly way than using AI to convert a table to a list of dictionaries (see below), while also building spreadsheet skills, is as follows:

1. [Download the CSV of cities](https://github.com/paulbradshaw/QGIS_param/blob/main/optionalfiles/gbcities.csv) and open in Excel or Google Sheets
2. Type this formula in cell J2. It will take the lat, long and name from three cells and insert them into a Python dict: `="{'lat': "&B2&", 'long': "&C2&", 'officialname': '"&A2&"'}"`
3. Copy the formula down for each row. You now have a column of dicts.
4. Type this formula to join the results using the [TEXTJOIN function](https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c), with a comma between each dict (the TRUE means ignore blank cells): `=TEXTJOIN(", ",TRUE,J:J)`
5. You now have the contents of a list - you just need to add a square bracket on either side to indicate the beginning and end of the list*. 
6. In your code, type an opening and closing square bracket, and then paste the list of dicts between them. 

## The AI method

First, create a CSV which contains only the information you need in your Python list (the city name, latitude and longitude).

Then attach it in your AI chat with this template prompt. It should give you a Python list that fits your script:

```
Attached is a CSV with 3 columns: city, lat and long. 
Create a Python list from this CSV that follows this structure:
listofdicstocsv = [
    {'lat': 50.844441271809465, 'long': -0.2985307978506628, 'officialname': 'Adur District Council'}, 
    {'lat': 54.71108952940033, 'long': -3.2472347297148736, 'officialname': 'Allerdale Borough Council'}
]
The list will be used in QGIS to automate the process of generating images for multiple locations.
```

The key elements in this prompt are defining the **output**, and providing an example (**n-shot prompting**).

(You can [see an example here](https://chatgpt.com/share/6a141ee7-9d50-83eb-90c5-e0782bc63fff))
