import os
import pymongo

print('Run All AI Cameras')

myclient = pymongo.MongoClient("mongodb+srv://app:weapon123@cluster0.mauiw.mongodb.net/")
mydb = myclient["weapon"]
mycol = mydb["cameras"]
for x in mycol.find():
    id = x["cam_id"]
    url = x["image"]
    os.system(f"start cmd /c python ai_cam_service.py --id {id} --url {url}")