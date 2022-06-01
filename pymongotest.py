import pymongo

atlas_cluster = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.zlntu.mongodb.net/sample_airbnb?authSource=admin&replicaSet=atlas-mqtc1h-shard-0&readPreference=primary"
client = pymongo.MongoClient(atlas_cluster)
db = client.sample_airbnb
print(db.name)