from msilib.schema import File
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

myclient = pymongo.MongoClient("mongodb+srv://app:weapon123@cluster0.mauiw.mongodb.net/")
mydb = myclient["weapon"]
mycol = mydb["cameras"]
xx = mycol.find()
list_col = list(xx)
json_data = dumps(list_col, indent = 2)
print(json_data)
# num_cams = [i for i in range(10)]

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
    mydoc = mycol.find(myquery)
    if len(list(mydoc.clone())) == 1 :
        for x in mydoc:
            location = "" + x["location"]
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
            socketio.emit('my event',{'url' : 'urlforimg','detect':weapon_type,'location':location,'date':date,'time':timenow,'idcam':info})

            return jsonify({'status': 'found'})
        else :
            return jsonify({'status': 'Notfound'})
    except Exception as e:
        print(e)
        return {},400

@app.route('/test',methods=['POST'])
def Test():
    image = request.files['img']
    info = request.form['info']
    print(image.filename)
    print(info)
    return jsonify({'status': 'test'})

@app.route('/static/<img>',methods=['GET'])
def Images(img):
    return send_from_directory('static', img)

@app.route('/getdb',methods=['GET'])
def db():
    return json_data

# # Overide the update method in WebcamVideoStream class
# class webcam(WebcamVideoStream):
#     def update(self):
#         while True:
#             # if the thread indicator variable is set, stop the thread
#             if self.stopped:
#                 return
#             # otherwise, read the next frame from the stream
#             (self.grabbed, self.frame) = self.stream.read()
#             # custom
#             if not self.grabbed:
#                 self.stop()

# @app.route("/")
# def index():
#     return render_template("index.html")

# def gen(id):
#     vs = webcam(src=id).start()
#     while True:
#         frame = vs.read()
#         frame = imutils.resize(frame, width=500)
#         ret, buffer = cv2.imencode(".jpg", frame)
#         frame = buffer.tobytes()
#         yield (b"--frame\r\n" b"Content-Type: image/jpg\r\n\r\n" + frame + b"\r\n")

# @app.route("/cameras/<int:id>",methods=['GET'])
# def video(id):
#     return Response(gen(id), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    print('Server Start')
    # app.run(host='0.0.0.0', port=8000, debug=True)
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)