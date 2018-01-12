= Pictures Gallery =

== How to set up the web app ==

* pip install Flask
* cd to the directory where PicGallery located
* export FLASK_APP=server.py
* execute: flask run
* access  http://127.0.0.1:5000/init to initialize database. Five pictures are added by default.
* access http://127.0.0.1:5000/images using your browser to ensure the following json displayed.



== What need to do ==
* Make a page "index.html" under static directory with pictures and data responed from javascript call to ttp://127.0.0.1:5000/images: 
Using bootstrap, Jquery to make a page similar to page1.png, page2.png using the json data responsed from ttp://127.0.0.1:5000/images

* Upload a picture and information using javascript: 
In page2.png, click the "+" on the top-right, a form will pop out, 
	and ask you input file and picture information. after clicking "save", the form will call 
	http://127.0.0.1:5000/images to save data. checking server.py to learn to know how that works.

* After uploading a image, the result should be displayed as page3.png

response json data after call http://127.0.0.1:5000/images
[
  {
    "dd": "2016-09-29", 
    "extention": "image/jpeg", 
    "id": 1, 
    "name": "DSC_0146.jpg", 
    "tag": "Grasslands", 
    "username": "Traveller"
  }, 
  {
    "dd": "2016-09-29", 
    "extention": "image/jpeg", 
    "id": 2, 
    "name": "DSC_0082.jpg", 
    "tag": "Sea", 
    "username": "Traveller"
  }, 
  {
    "dd": "2016-09-29", 
    "extention": "image/jpeg", 
    "id": 3, 
    "name": "DSC_0079.jpg", 
    "tag": "Sea", 
    "username": "Partner"
  }, 
  {
    "dd": "2016-09-29", 
    "extention": "image/jpeg", 
    "id": 4, 
    "name": "DSC_0004.jpg", 
    "tag": "Forest", 
    "username": "Traveller"
  }, 
  {
    "dd": "2016-09-29", 
    "extention": "image/jpeg", 
    "id": 5, 
    "name": "DSC_0001.jpg", 
    "tag": "Forest", 
    "username": "Partner"
  }, 
  {
    "dd": "2018-01-10", 
    "extention": "image/jpeg", 
    "id": 6, 
    "name": "1500518835247.jpg", 
    "tag": "Test", 
    "username": "TEst"
  }
]