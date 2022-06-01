import pymongo
import json
import pprint

try:

    atlas_cluster = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/sample_airbnb?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"
    client = pymongo.MongoClient(atlas_cluster)
    db = client.sample_airbnb

    query =  {"bedrooms":{"$gt":1}}
    cursor = db.listingsAndReviews.find(query)
    list_cur = list(cursor)
    json_data = json.dumps(list_cur, indent = 2)
    pprint(json_data.count)

except Exception as e:
        print("An exception occurred ::", e)

finally:
    print("*************** EXITING ****************")
 