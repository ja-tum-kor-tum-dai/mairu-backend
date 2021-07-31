from pymongo import MongoClient
import json

client = MongoClient("mongodb://mongo:27017")
db = client['mairu']
quote_collection = db['quotes']


def main():
    """ read data.json file and insert data into mongodb """
    f = open('data.json')
    data = json.load(f)
    # for i in data:
    #     print(i)
    quote_collection.insert_many(data)


if __name__ == '__main__':
    main()
