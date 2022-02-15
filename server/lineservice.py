#ข้อความ
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#สติกเกอร์
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#รูปภาพ
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

#ส่งแจ้งเตือน
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'eH8fpUFOenC7Ys5i36ILWPZZ6OjaQ2ewHJP9HmzwIc0'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

def notifyFile(filename,msg):
    file = {'imageFile':open('static\\'+filename,'rb')}
    payload = {'message': msg}
    return _lineNotify(payload,file)

# lineNotify('เจออาวุธๆ')
# notifyPicture('http://localhost:8000/static/dog.jpg')
# notifyPicture('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=768:*')
# notifyFile()
