#personal Website
Description:<br/>
Static website with the Flask Web Framework. You can customise it for yourself to show yourself and your work. It offers the opportunity to present projects, explain a curriculum vitae and let others know more about you with a short information headline and text.<br/>

Why I have buil this project:<br/>
I started this project to learn HTML, CSS, a little JS as well as the Python framework Flask to create a website for my project portfolio and resume.<br/>

Download:<br/>
Use this command in your directory to clone the project:
```
git clone https://github.com/comhendrik/personalWebsite.git
```
or download it directly from Github and unzip it in your directory.<br/>

Setup:<br/>
1. create CV<br/>
1.1 Go to /data/cv.json and create resume entries according to the instructions. Icons should always be an icon name from goole material icons https://fonts.google.com/icons?selected=Material+Icons.<br/>
2. create Portfolio<br/>
2.1 Go to /data/portfolio.json and create portfolio entries according to the instructions.<br/>
2.2 If you want to use images, create a folder with the project name under /static/images and copy some images in the folder /static/images/<YourNewProject>. Now you can go to /data/portfolio.json and create a image Path in the images array.<br/>
3. create Blog article<br/>
3.1 Go to /data/blog.json and create blog articles according to the instructions. Icons should always be an icon name from goole material icons https://fonts.google.com/icons?selected=Material+Icons.<br/>
3.2 The body property can be filled with normal HTML Code and your article will be rendered properly.<br/>
4. choose Language<br/>
4.1 Go to /app.py line 21 and give the TEXT variable a value. You can choose between German and English.<br/>
5. set up Website<br/>
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
Now open the website under http://127.0.0.1:3000/index<br/>

2. Option (Docker Container)
Create the connection to Docker(open Docker Desktop) and run the following commands in a terminal window
```
docker image build -t <imageName> .
docker run -dp 3000:3000 <imageName>
```
Now open the website under http://127.0.0.1:3000/index<br/>

A ready-to-use container is available on the Docker Hub (https://hub.docker.com/r/comhendrik/webpage/tags) <br/>

3. Option (Host Flask application on heroku)
First, make sure you have the Heroku CLI installed in addition to git.<br/>
Create a virtual environment in the directory with:

```
python3 -m venv <venvName>
```

and activate it with
```
. <venvName>/bin/activate
```

Now install gunicorn
```
pip install gunicorn
```
You also need a Procfile located in the root directory. I already added to the root directory so you don't need to create on your own.<br/>
Now run:
```
git init
git add .
git commit -m "<your commit message>"
```
You are ready for the preperations on your local directory. Yeah!<br/>
We are starting with the deployment on heroku:
Run and follow the instructions:
```
heroku login
```
You need to create a app with:
```
heroku create <appname>
```
(if you don't provide <appname>, heroku creates a random name.)<br/>
To give heroku acces to your git repo run:
```
heroku git:remote <appname>
```
Now is the time to push your repo to heroku with(heroku will automatically build the application and you can visit it under https://<appname>.herokuapp.com/index):
```
git push heroku master
```
(master is the default name for your repository. If you decided to name it something else, use that name at this point.)



