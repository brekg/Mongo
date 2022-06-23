import pymongo
import json
import pprint

try:

    atlas_cluster = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/sample_airbnb?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"
    client = pymongo.MongoClient(atlas_cluster)
    
    # Get a reference to the "sample_mflix" database:
    db = client["sample_mflix"]

    # Get a reference to the "movies" collection:
    movie_collection = db["movies"]

    # The Aggregation Pipeline is defined as an array of different operations

    # Limit to 100 document for development only:
    stage_limit_100 = { "$limit": 100}

    # Match title = "A Star Is Born":
    stage_match_title = {"$match": {"title": "A Star Is Born"}}

    # Sort by year, ascending:
    stage_sort_year_ascending = {"$sort": { "year": pymongo.ASCENDING }}

    # Limit to 1 document:
    stage_limit_1 = { "$limit": 1 }

    # Now the pipeline is easier to read:
    pipeline = [stage_limit_100,stage_match_title,stage_sort_year_ascending,stage_limit_1]

    results = movie_collection.aggregate(pipeline)

    for movie in results:
        print(" * {title}, {first_castmember}, {year}".format(
                title=movie["title"],
                first_castmember=movie["cast"][0],
                year=movie["year"],
    ))

except Exception as e:
        print("An exception occurred ::", e)

finally:
    print("*************** EXITING ****************")