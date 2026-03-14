# A map for every reader: how to generate hundreds of images for multiple audiences or partners using QGIS and Python

The BBC Shared Data Unit wanted to generate a map image for each authority in the UK showing the state of flood defences in that area — so they turned to the mapping tool QGIS’s built-in Python functionality. 

This repo contains files and tipsheets for learning how to generate and export dozens of maps in QGIS centred at different points, and how AI can help speed up the process. 

This process is sometimes called *parameterisation*: generating multiple outputs based on a list of parameters (e.g. a list of lat-long locations)

## Prerequisites and tools

You should have some basic knowledge of QGIS and be comfortable using Python or vibe coding. 

You should have [QGIS](https://qgis.org/download/) and [Python](https://www.askpython.com/python/examples/install-python-with-conda) installed on the computer and a free account with an AI tool such as ChatGPT, Gemini or Claude.

## Objectives

After using this repo you should be able to understand how Python works in QGIS and use AI to help generate, understand and adapt code

## Files

You will need the following files:

1. A shape file of some sort, to create a map with. The example used is `AIMS_Spatial_Flood_Defences_inc_standardised_attributes.shp.zip` from the Spatial Information section of [AIMS Spatial Flood Defences (inc. standardised attributes)](https://environment.data.gov.uk/dataset/8e5be50f-d465-11e4-ba9a-f0def148f590)
2. A list of lat-longs for the places you want to generate map images for
3. A Python file containing the code to automate multiple image exports

## Walkthrough steps

1. [01_make_a_map.md](https://github.com/paulbradshaw/QGIS_parameterisation/blob/main/01_make_a_map.md) describes how to create a basic map in QGIS
2. [02_python.md](https://github.com/paulbradshaw/QGIS_parameterisation/blob/main/02_python.md) describes how to use a Python file to automate map image exports

## Optional files

You can use the following files to practise the processes above, and expand them:

* [defences_classification.csv](https://github.com/paulbradshaw/QGIS_parameterisation/blob/main/optionalfiles/defences_classification.csv) - this contains extra data about the defences that allows you to classify them and therefore use separate symbology in mapping.
* [qgis_take_pix_twoSize.py](https://github.com/paulbradshaw/QGIS_param/blob/main/optionalfiles/qgis_take_pix_twoSize.py) is a Python script that generates two images for each lat-long, each at a different magnification (useful if some of your areas are large urban sprawls and some are small towns)
* [QGISlocationsINDICES.csv](optionalfiles/QGISlocationsINDICES.csv) contains the lat/long locations of centre points in each UK local authority. You can also get these from [UK Local Authorities (past and current)](https://pages.mysociety.org/uk_local_authority_names_and_codes/datasets/uk_la_past_current/latest)  
* [gbcities.csv](optionalfiles/gbcities.csv) contains the lat/long locations of centre points in Great Britain's cities
* [Historic Flood Map](https://www.data.gov.uk/dataset/76292bec-7d8b-43e8-9c98-02734fd89c81/historic-flood-map1) contains other shape files that you can map - the file `DownloadHistoric_Flood_Map.shp.zip` is what you need to download
* [Flood Risk Areas](https://www.data.gov.uk/dataset/42c31542-228d-439b-8dbe-e72135dae71c/flood-risk-areas) contains more flood-related shape files: download `DownloadFlood_Risk_Areas.shp.zip` (click *Show more* if you can't see it)
* [Flood Map for Planning - Flood Zones](https://www.data.gov.uk/dataset/104434b0-5263-4c90-9b1e-e43b1d57c750/flood-map-for-planning-flood-zones1)
* [Sensitive Areas - Eutrophic Rivers](https://www.data.gov.uk/dataset/ec3b6c16-3969-474d-a469-6b5f214eddbc/sensitive-areas-eutrophic-rivers) "showing the extent of Urban Wastewater Treatment Directive (91/271/EEC) (UWWTD) sensitive areas (eutrophic)."
* [Nitrate Vulnerable Zones (NVZ) 2021 Designations](https://www.data.gov.uk/dataset/77ffd32c-13db-4d83-a1f8-044c5397bc34/nitrate-vulnerable-zones-nvz-2021-designations): "areas designated as being at risk from agricultural nitrate pollution."

## Useful links

* BBC Shared Data Unit repo: [Thousands of flood defences below standard as Storm Bram hit](https://github.com/BBC-Data-Unit/flood-defences) - this links to the stories created using the flood defences data, and the wider methodology. The satellite images were not used in the end because we obtained more detailed data that could not be used for mapping for privacy reasons.
* Tim Green: [Vibe Coding Threatens Journalism: Why Newsrooms Need Governance Now](https://smarterarticles.co.uk/vibe-coding-threatens-journalism-why-newsrooms-need-governance-now) explores some of the ethical and security issues involved in vibe coding
* Simon Willison: [Not all AI-assisted programming is vibe coding (but vibe coding rocks)](https://simonwillison.net/2025/Mar/19/vibe-coding/) - "I’m concerned that the definition is already escaping its original intent. I’m seeing people apply the term “vibe coding” to all forms of code written with the assistance of AI. I think that both dilutes the term and gives a false impression of what’s possible with responsible AI-assisted programming." 
