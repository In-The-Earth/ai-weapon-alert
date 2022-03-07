from msilib.schema import File

from importlib_metadata import NullFinder
from detect import run
from lineservice import notifyFile
import imutils
from imutils.video import WebcamVideoStream
from flask.helpers import url_for
import cv2
from bson.json_util import dumps, loads
from flask_cors import CORS
# run(weights="pistol_v2.pt",conf_thres=0.5,source=0)
# data = run(weights="yolov5s.pt",conf_thres=0.5,source="data/images/woman.jpg")
# print(data)

from flask import Flask, jsonify, request, send_from_directory,render_template, Response
from flask_socketio import SocketIO,send,emit
from pathlib import Path
import os
import pymongo

app = Flask(__name__)

CORS(app)
home_dir = Path(__file__).parent
UPLOAD_FOLDER = os.path.join(home_dir, "static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

def readDB():
    myclient = pymongo.MongoClient("mongodb+srv://app:weapon123@cluster0.mauiw.mongodb.net/")
    mydb = myclient["weapon"]
    mycol = mydb["cameras"]
    return mycol
# print(json_data)
# num_cams = [i for i in range(10)]

def GetJsonDB():
    xx = readDB().find()
    list_col = list(xx)
    json_data = dumps(list_col, indent = 2)
    return json_data

@app.route('/home',methods=['POST'])
def Home():
    image = request.files['img']
    info = request.form['info']
    weapon_type = request.form['wptype']
    date = request.form['date']
    timenow = request.form['timenow']
    print(image.filename)
    print(info)
    print(weapon_type)
    text = ''

    myquery = { "cam_id": info }
    mydoc = readDB().find(myquery)
    if len(list(mydoc.clone())) == 1 :
        for x in mydoc:
            location = "" + x["info"]
    else :
        location = "Not found location"

    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    try:
        data = run(weights="yolov5s.pt",conf_thres=0.5,source="static/"+image.filename) #check person
        if data :
            text = f'Cam: {info}\n'
            text += f'Detect: {weapon_type}\n'
            text += f'Location: {location}\n'
            text += f'Date: {date}\n'
            text += f'Time: {timenow}'
            
            notifyFile(image.filename,text)
            socketio.emit('my event',{'url' : f'http://127.0.0.1:8000/static/{image.filename}','detect':weapon_type,'location':location,'date':date,'time':timenow,'idcam':info})

            return jsonify({'status': 'found'})
        else :
            return jsonify({'status': 'Notfound'})
    except Exception as e:
        print(e)
        return {},400


@app.route('/static/<img>',methods=['GET'])
def Images(img):
    return send_from_directory('static', img)

@app.route('/getdb',methods=['GET'])
def db():
    return GetJsonDB()

@app.route('/addDB',methods=['POST'])
def AddDB():
    num_cam = len(list(readDB().find().clone()))
    cam_id = str(num_cam+1)
    for x in range(num_cam):
        y = str(x+1)
        mycol = readDB()
        myquery = { "cam_id": y }
        mydoc = mycol.find(myquery)
        if len(list(mydoc.clone())) == 0:
            cam_id = y
    url = request.form['url']
    info = request.form['info']
    name = request.form['name']
    display = False
    mydict = { "cam_id": cam_id, "info": info, "image": url, "name": name, "display": display}
    readDB().insert_one(mydict)
    return jsonify({'status': 'add DB done'})

@app.route('/deleteDB',methods=['POST'])
def DeleteDB():
    cam_id = request.form['cam_id']
    myquery1 = { "cam_id": cam_id }
    readDB().delete_one(myquery1)
    return jsonify({'status': 'delete DB done'})

if __name__ == '__main__':
    print('Server Start')
    # app.run(host='0.0.0.0', port=8000, debug=True)
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)