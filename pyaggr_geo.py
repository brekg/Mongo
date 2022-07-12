from matplotlib.pyplot import box
from pymongo import MongoClient
from pandas import DataFrame
import pprint
import json 

#https://stackoverflow.com/questions/63162823/mongo-geowithin-error-polygon-coordinates-must-be-an-array
#https://www.mongodb.com/docs/manual/tutorial/geospatial-tutorial/
def main():
    # Call one of the outside functions
    try:    
        
        atlas_connection="mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/test?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"
        client = MongoClient(atlas_connection)
        database = client['test']

        for doc in database.riverGuage.find({"location": {$geoWithin: "$centerSphere": [-90.3729,38.4537]}}).limit(3):pprint.pprint(doc)
        #river_gauge_cur = list(river_gauge)



    except Exception as e:        
        print("An exception occurred ::", e)

    finally:
        client.close()

# The conditional stays with main
if __name__ == "__main__":
    main()
