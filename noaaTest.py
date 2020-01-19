#! /opt/anaconda3/bin/python

# "iCloud Documents" version
# OK - this is working. The values you get are in tenth of degrees Celsius.
# https://rstudio-pubs-static.s3.amazonaws.com/275033_a87f8c52176d4aed8880d56dbf6c3ada.html
# ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

from noaa_api_v2 import NOAAData
api_token = "wmQiLvhBGjPXtuPlEEpdwFdoTqzFxbRQ"

data = NOAAData(api_token)

# Daily Summaries, Global Summaries, etc. - the big group?
#categories = data.datasets(locationid='ZIP:05401', sortfield='name')

# First freeze, total precip, total snowfall, monthly mean min temp, etc.
#categories = data.data_types(locationid='ZIP:05401', sortfield='name')

# NOTE: data_categories has temperature in it
categories = data.data_categories(locationid='ZIP:05401', sortfield='name')

for i in categories:
    print(i)
# https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?stationid=COOP:310090&stationid=COOP:310184&stationid=COOP:310212

# https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datacategoryid=TEMP&limit=56

print("Divider: ----------------")
#weather_data = data.fetch_data(datasetid='GHCND', datacategoryid = 'TEMP', locationid='ZIP:05401', startdate='2010-05-01', enddate='2010-05-02', limit=5)
# Works, but don't understand where "NORMAL_HLY" from yet
#weather_data = data.fetch_data(datasetid='NORMAL_HLY', datatypeid = 'HLY-TEMP-NORMAL', locationid='ZIP:05401', startdate='2010-05-01', enddate='2010-05-02', limit=2)
weather_data = data.fetch_data(datasetid='GHCND', datatypeid = 'TAVG', locationid='ZIP:05401', startdate='2019-12-05', enddate='2019-12-05', limit=10)
#weather_data = data.fetch_data(datasetid='GHCND', datacategoryid = 'TEMP', locationid='ZIP:05401', startdate='2019-12-01', enddate='2019-12-10', limit=100)

#for j in weather_data:
#    print("where is temp")
#    print(weather_data)
print(weather_data)

print("Here is temperature in 1/10 degree C: " + str(weather_data[0]['value']))
temp = weather_data[0]['value']
temp = temp/10
print ("Here is the temperature in C: " + str(temp))

print("hello")