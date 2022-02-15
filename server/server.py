from msilib.schema import File
from detect import run
from lineservice import notifyFile
# run(weights="pistol_v2.pt",conf_thres=0.5,source=0)
# data = run(weights="yolov5s.pt",conf_thres=0.5,source="data/images/woman.jpg")
# print(data)

from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path
import os
import pymongo

app = Flask(__name__)

home_dir = Path(__file__).parent
UPLOAD_FOLDER = os.path.join(home_dir, "static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home',methods=['POST'])
def Home():
    image = request.files['img']
    info = request.form['info']
    print(image.filename)
    print(info)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    try:
        data = run(weights="yolov5s.pt",conf_thres=0.5,source="static/"+image.filename) #check person
        if data :
            notifyFile(image.filename,info)
            return jsonify({'status': 'found'})
        else :
            return jsonify({'status': 'Notfound'})
    except:
        return 400

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

if __name__ == '__main__':
    print('Server Start')
    app.run(host='0.0.0.0', port=8000, debug=True)