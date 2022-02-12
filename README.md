# tri-map
### what is this project?

EPA Toxic Release Inventory (TRI) Mapping Software

View this project LIVE at: https://fguattari.github.io/tri-map/
Contact: fguattari-dev@protonmail.com

This project is meant to preprocess EPA TRI 2019 data and display all Carcinogenic and/or Clean Air Act-classified chemical-emitting facilities in Southern California, Los Angeles County specifically. This is an ongoing project, and can be accessed from 'save-socal.github.io/tri-mapping'.

Current functionality:

- Icons are draggable - A longer drop-shadow indicates a larger bunch of markers; move these around to view other chemical reports for the same facility/location
- Current data includes LA County
- HeatMap functionality enabled by default; disable through LayerControl
- Use MeasureControl to measure the distance of TRI facilities to schools, hospitals, and other vulnerable spots

Future functionality:

- Combine chemical reports for facilities to display all at once, with pages for different chemicals
- Include all CA EPA TRI data
- Ability to refine chemical search, refine sector, and include all available data points (>4600 known chemical reports)
- Demographic Information - Preliminarily, however; one can see that most TRI facilities reside within African-American or Hispanic majority areas
- Conduct extensive Data Refinement for Death Reports + Reporting for Diagnoses of Asthma, Emphysema, Lung Cancers, and more
- Establish causal link between the prevalence of lung afflictions and releases

### file descriptions

[pp.py]

- Constructs DataFrame from 2019 EPA TRI data
- PreProcesses Data to find Carcinogenic and/or EPA Clean Air Act-classified chemical-emitting Facilities in Southern California
- Exports the data as a class attribute

[mp.py]

- Constructs folium map
- Maps all available Datapoints, with markers for each Chemical Emission report and a HeatMap of area trends
- Exports map as 'map.html'

