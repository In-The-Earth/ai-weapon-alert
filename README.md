# ai-weapon-alert
![1651742479177](https://user-images.githubusercontent.com/48666197/167086778-44551e4e-0b1a-46b7-b6a8-b26092e00604.jpg)
![1651742492503](https://user-images.githubusercontent.com/48666197/167086801-f476c5c1-fe5b-4274-a8e5-47c2614f36fb.jpg)
![1651742504017](https://user-images.githubusercontent.com/48666197/167086930-72a25570-5c4c-427b-a826-0372b035c406.jpg)

 #### Alert info.
 
![1651742515685](https://user-images.githubusercontent.com/48666197/167086823-a76b0114-fc5e-4c97-a9a2-b8bbbd28fe6c.jpg)


 #### Alert notification in line application.
 
![1651742528694](https://user-images.githubusercontent.com/48666197/167086831-fc86b1de-dc83-4858-a54b-6f58804d22b4.jpg)

Weapon Alert arises from the fact that organizers foresee the problem of the crime. Attempting to report the incident could hurt the person that trying to signal for help and sometimes may not be in time, to reduce the risk of danger to the reporter that may occur. To solve this problem, the author has developed a Weapon-alert. It is a web application that has a camera system with artificial intelligence to detect weapons and immediately alerts without having any button to press or call. Weapon Alert using Python language and libraries such as Bootstrap, Flask, etc. to be used in the preparation of this project.

![ezgif-2-28d5dfc91e](https://user-images.githubusercontent.com/48666197/167089336-d91f3fe4-8412-4d98-942d-ea39a7b49400.gif)
![1651823368789](https://user-images.githubusercontent.com/48666197/167090136-4cfe7955-7e3f-431d-bf47-3df8bf53ed00.jpg)
![1651823388822](https://user-images.githubusercontent.com/48666197/167090143-5254d424-2364-4c01-a111-6fbafcde25fc.jpg)

Weapon-Alert Web Applicaion for CS-project.

## Getting Start
Weapon Alert is Web Application for Detect weapon include handgun and knife with human, then alerts to the web page and line application notify.

> For Run this project completely, you need to clone frontend frist : [HERE](https://github.com/GunAyng/project-weapon-alert)

### installing
install server
```
cd server
pipenv shell
pipenv install
```
install service for ai
```
cd service
pipenv shell
pipenv install
```

### Runing
Run video streamimg for webcam
```
cd videostream
python videostream.py
```
Run server
```
cd server
pipenv shell
python server.py
```
Run Service for ai
```
cd service
pipenv shell
python runallAI.py
```

port : http://localhost:8080/Home

## Deployment

port : http://localhost:8080/ctr
For control database, you can add more cameras or delete it from here.

![1651825358898](https://user-images.githubusercontent.com/48666197/167095069-30286acc-5602-4ded-a868-8fc76bf23c14.jpg)
![1651825375735](https://user-images.githubusercontent.com/48666197/167095081-abfe4f54-52d7-4e3e-bd71-e3885dec4114.jpg)
![1651825368375](https://user-images.githubusercontent.com/48666197/167095087-d37aa3d3-14e4-40b5-b8f1-0bf565758adc.jpg)

## Built With

* [Yolov5](https://github.com/ultralytics/yolov5) - Object Detection framwork
* [Mongodb](https://www.mongodb.com/) - Database
* [Vue js](https://vuejs.org/) - Frontend bootstrap
* [Roboflow](https://roboflow.com/) - Preprocess dataset
* [Line notify](https://notify-bot.line.me/th/) - line notification
* Flask Python - Python framwork for rest server
* Socketio Python - Python framwork for realtime server
* OpenCV Python - Python framwork for videostreamimg
* [Weapon Detecion dataset](https://dasci.es/transferencia/open-data/24705/) - Dataset Reference
