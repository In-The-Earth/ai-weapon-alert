import pymongo

myclient = pymongo.MongoClient("mongodb+srv://app:weapon123@cluster0.mauiw.mongodb.net/")
mydb = myclient["weapon"]
mycol = mydb["cameras"]

y = "4"

myquery = { "cam_id": y }

mydoc = mycol.find(myquery)
print(mycol)
print(len(list(mydoc.clone())))
for x in mydoc:
  print(x["info"])

# mydict = { "cam_id": "2", "location": "Highway 37" }
# mycol.insert_one(mydict)
