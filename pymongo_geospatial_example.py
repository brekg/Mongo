import pymongo
import pprint
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

	
course_cluster_uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/test?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"

course_client = pymongo.MongoClient(course_cluster_uri)

# sample Database
db = course_client['sample_geospatial']

# sample Collection
shipwrecks = db['shipwrecks']

l = list(shipwrecks.find({}))

lngs = [x['londec'] for x in l]
lats = [x['latdec'] for x in l]

# Clear the figure (this is nice if you
# execute the cell multiple times)
plt.clf()

# Set the size of our figure
plt.figure(figsize =(14, 8))

# Set the center of our map with our
# first pair of coordinates and set
# the projection
""" m = Basemap(lat_0 = lats[0],
			lon_0 = lngs[0],
			projection ='cyl')

# Draw the coastlines and the states
m.drawcoastlines()
m.drawstates()

# Convert our coordinates to the system
# that the projection uses
x, y = m(lngs, lats) 

# Plot our converted coordinates
plt.scatter(x, y)

# Display our beautiful map
plt.show()"""
