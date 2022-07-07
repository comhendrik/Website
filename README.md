#personal Website
Description:<br/>
Static website build with plain HTML and CSS.  You can customise it for yourself to show yourself and your work. It offers the opportunity to present projects, explain a curriculum vitae and let others know more about you with a short information headline and text. To make it easy for you, you can create Blog entrys anytime without having the need to rebuild the page on a server. <br/>

Why I have buil this project:<br/>
I started this project to learn HTML, CSS, a little bit of JS  and to create a website for my project portfolio and CV.<br/>

Download:<br/>
Use this command in your directory to clone the project:
```
git clone https://github.com/comhendrik/personalWebsite.git
```
or download it directly from Github und unzip in your directory.

Setup:<br/>
1. create CV
1.1 Go to /data/cv.json and create resume entries according to the instructions. Icons should always be an icon name from goole material icons https://fonts.google.com/icons?selected=Material+Icons.<br/>
2. create Portfolio
2.1 Go to /data/portfolio.json and create portfolio entries according to the instructions.<br/>
2.2 If you want to use images, create a folder with the project name under /static/images and copy some images in the folder /static/images/<YourNewProject>. Now you can go to /data/portfolio.json and create a image Path in the images Array.<br/>
3. create Blog article
3.1 Go to /data/blog.json and create blog articles according to the instructions. Icons should always be an icon name from goole material icons https://fonts.google.com/icons?selected=Material+Icons.<br/>
3.2 The body property can be filled with normal HTML Code and your article will be rendered properly<br/>
4. choose Language
4.1 Go to /app.py line 21 and give the TEXT variable a value. You can choose between German and English.<br/>
5. set up Website
5.1 Go to /setup.py and fill the propertys with desired values.<br/>

Run:
1. Option (Locally):
Create a terminal window and run the following commands
```
python3 -m venv <venvName>
. <venvName>/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:3000 wsgi:application 
```
Now open the website under http://127.0.0.1:3000/index
2. Option (Docker Container)
Create the connection to docker(open Docker Desktop) and run the following commands in a terminal window
```
docker image build -t <imageName> .
docker run -dp 3000:3000 <imageName>
```
Now open the website under http://127.0.0.1:3000/index
3. Option (Host Docker container on heroku)



