from pp import preprocess
import geopandas as gpd
import folium
from folium import plugins
from folium.plugins import MeasureControl,HeatMap

def fh(row):
  i = row

  facility = df['Facility'].iloc[i]
  sector = df['Sector'].iloc[i]
  frsid = df['FRS-ID'].iloc[i]
  ch = df['Chemical'].iloc[i]
  e = df['Emissions'].iloc[i]
  os = df['Off-Site'].iloc[i]
  pw = df['Production-Waste'].iloc[i]

  left_col_colour = "#2A799C"
  right_col_colour = "#C5DCE7"

  html = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:0"; width="300px">Facility: {}<br></br>Sector: {}</h4>""".format(facility,sector) + """
<br></br>
</head>
    <table style="height: 126px; width: 300px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">FRS-ID</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(frsid) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Chemical</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(ch) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">On-Site Emissions</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(e) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Off-Site Emissions</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(os) + """
</tr>
<tr>
<td style="background-color: """+ left_col_colour +""";"><span style="color: #ffffff;">Total Production-Waste</span></td>
<td style="width: 200px;background-color: """+ right_col_colour +""";">{}</td>""".format(pw) + """
</tr>
</tbody>
</table>
</html>
"""

  return html

p = preprocess()
fl = p.facilities
df = p.data

location = df['Latitude'].mean(), df['Longitude'].mean()
m = folium.Map(location=location,zoom_start=15,min_zoom=5)
plugins.ScrollZoomToggler().add_to(m)
m.add_child(MeasureControl())
plugins.Fullscreen(position='topright').add_to(m)

geometry = gpd.GeoDataFrame(columns=['latitude','longitude'])
geometry['latitude'] = df['Latitude']
geometry['longitude'] = df['Longitude']


for i in range(len(geometry)):
  row = df.iloc[i]
  geo = geometry.iloc[i]

  html = fh(i)
  iframe = folium.IFrame(html=html,width=400,height=300)
  popup=folium.Popup(iframe,parse_html=True)
  folium.Marker([geo[0],geo[1]],
                  popup=popup,
                  draggable=True).add_to(m)

# heatmap
f = folium.FeatureGroup().add_to(m)
folium.LayerControl().add_to(m)
heat_data = [[row['latitude'],row['longitude']] for index,row in geometry.iterrows()]
hm = HeatMap(heat_data).add_to(m)
f.add_child(hm,name='HeatMap')

m.save('map.html')