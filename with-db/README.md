Setup:<br/>
In advance: I decided not to explain in detail how to use it without authentication because I think authentication should be used with MongoDB in this project.
1. Download MongoDB<br/>
1.1 Install MongoDB on your system. https://www.mongodb.com/docs/manual/installation/ <br/>
1.2 I found MongoDB Compass very helpful but it is not necassary. https://www.mongodb.com/try/download/compass <br/>
1.3 Decide wether you want to use authentication or not. If you want to use it, I can recommend this tutorial. https://blog.tericcabrel.com/enable-authentication-and-authorization-on-mongodb/ (Note the version you are using. I used a Mac with M1 and started the mongo shell with ```mongosh``` instead of ```mongo``` ) <br/>
1.4 (Optional) if you don't want to use authentication: Change the lines containing ```pymongo.MongoClient(authenticate(user, password))``` to ```pymongo.MongoClient("YOURNORMALURI")``` and change the forms in create_blog_entry.html, create_portfolio_entry.html and create_cv_entry.html and the functions in admin.py and change the URI in setup.py to a normal one so that no authentication is used.<br/>
1.4. (Optional) if you want to use authentication: Paste in your URI for MongoDB with a reading only User in setup.py <br/>
1.5 Configure the authenticate() function in admin.py how you want it to be. When you don't use authentication you can delete it.<br/>
2. Create <br/>
2.1 The admin credentials you need to provide are the ones you specify when you create an admin user. See 1.3<br/>
2.2 When your website is up and running visit for CV http://127.0.0.1:3000/admin/cv to create a new article.<br/>
2.3 When your website is up and running visit for Portfolio http://127.0.0.1:3000/admin/portfolio to create a new article.<br/>
2.4 When your website is up and running visit for Blog articles http://127.0.0.1:3000/admin/blog to create a new article.<br/>
3. choose Language<br/>
3.1 Go to /app.py line 21 and give the TEXT variable a value. You can choose between German and English.<br/>
4. set up Website<br/>
4.1 Go to /setup.py and fill the propertys with desired values.<br/>


<b>This section is not finished</b>:
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

You need a Procfile located in the root directory. I already added it to the root directory so you don't need to create it on your own.<br/>
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
(if you don't provide appname, heroku creates a random name.)<br/>
To give heroku acces to your git repo run:
```
heroku git:remote <appname>
```
Now is the time to push your repo to heroku with(heroku will automatically build the application and you can visit it under https://appname.herokuapp.com/index):
```
git push heroku master
```
(master is the default name for your repository. If you decided to name it something else, use that name at this point.)<br/>



