from pymongo import MongoClient
import csv

client = MongoClient('mongodb+srv://<username>:<password>@cluster41x3n-nnaqa.mongodb.net/<database>?retryWrites=true')
db = client.Rajnikanth
rajnikanth = db.rajnikanth

with open('jokes.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader:
    result = rajnikanth.insert_one({
      'joke': row[0]
    })
