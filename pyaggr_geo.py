from pymongo import MongoClient
import pprint   

def main():

    try:    
        
        atlas_connection="mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/test?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"
        client = MongoClient(atlas_connection)
        database = client['test']


        pipeline = [
            {'$match': {'name':'jefferson'}},
            {'$project': {'_id': 0, 'uuid': 1, 'name': 1, 'location': 1}},
        ]

        results = database.counties.aggregate(pipeline)
        pprint(results)

    except Exception as e:
        print("An exception occurred ::", e)

    finally:
        client.close()
