import pandas as pd

class Emissions:
  def __init__(self):
    ds = pd.read_csv('tri.csv')
    df = pd.DataFrame(ds)
    self.data = pd.DataFrame(columns=['Facility','Sector','FRS-ID','Latitude','Longitude','Chemical','Emissions','Off-Site','Production-Waste'])

    lf = []
    ls = []
    lfi = []
    lla = []
    llo = []
    lc = []
    le = []
    lo = []
    lp = []

    for i in range(len(df)):
      row = df.iloc[i]

      county = row[6]
      caa = row[37]
      car = row[41]
      if pd.isna(row[113]) == True:
        row[113] = 0
      emis = row[100] + row[101] + row[103] + row[104] + row[113]

      if county == 'LOS ANGELES':
        if (caa == 'YES') or (car == 'YES'):
          if emis > 1:
            frsid = row[2]
            fac = row[3]
            lat = row[11]
            lon = row[12]
            sect = row[19]
            chem = row[33]
            os = row[81]
            pw = row[112]
            lf.append(fac)
            ls.append(sect)
            lfi.append(frsid)
            lla.append(lat)
            llo.append(lon)
            lc.append(chem)
            le.append(emis)
            lo.append(os)
            lp.append(pw)
    
    self.data['Facility'] = lf
    self.data['Sector'] = ls
    self.data['FRS-ID'] = lfi
    self.data['Latitude'] = lla
    self.data['Longitude'] = llo
    self.data['Chemical'] = lc
    self.data['Emissions'] = le
    self.data['Off-Site'] = lo
    self.data['Production-Waste'] = lp

    self.facilities = []

    for i in range(len(self.data)):
      row = self.data.iloc[i]
      fn = row[0]

      if fn not in self.facilities:
        self.facilities.append(fn)

class Asthma:
  def __init__(self):
    ds = pd.read_csv('asthma-ed.csv')
    df = pd.DataFrame(ds)
    self.geometry = pd.DataFrame(columns=['Zip','Visits','Age'])
    lzip = []
    lvisit = []
    lage = []

    for i in range(len(df)):
      row = df.iloc[i]

      z = row[0]
      v = row[1]
      ag = row[3]
      c = row[4]

      if c == 'Los Angeles':
        lzip.append(z)
        lvisit.append(v)
        lage.append(ag)
    
    self.geometry['Zip'] = lzip
    self.geometry['Visits'] = lvisit
    self.geometry['Age'] = lage