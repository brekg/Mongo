from pymongo import MongoClient
import pprint
import json 

def main():
    # Call one of the outside functions
    try:    
        
        atlas_connection="mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/test?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"
        client = MongoClient(atlas_connection)
        database = client['test']

        pipeline_county = [
            {'$match': {'name':'Jefferson'}},
            {'$project': {'_id': 0, 'uuid': 1, 'name': 1, 'location': 1}},
        ]

        results = database.counties.aggregate(pipeline_county)
        
        list_cur = list(results)
        json_data = json.dumps(list_cur, indent = 2)
        #pprint(json_data)

    except Exception as e:
        print("An exception occurred ::", e)

    finally:
        client.close()

# The conditional stays with main
if __name__ == "__main__":
    main()
