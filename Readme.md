# Sassy Flask (SaaS Boilerplate)
Just another API boilerplate for your next restful saas application. Uses flask with praetorian to handle backend, authorization. The static website is built with gridsome. Finally extend new functionality with the API by creating your vue components. 

## Gridsome Frontend Static Website
Read Gridsome Docs.
Dont forget to "gridsome build" in the web directory (dist, build ready.)

## Dependencies
These are required to replicate on your local machine or production.
- Node, Gridsome

### Server
- Flask, SQLAlchemy, Flask-Praestorian

From requirements.txt

blinker==1.4
click==7.1.2
Deprecated==1.2.10
Flask==1.1.2
flask-buzz==0.1.15
Flask-Mail==0.9.1
flask-praetorian==1.0.0
Flask-SQLAlchemy==2.4.4
inflection==0.3.1
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
passlib==1.7.2
pendulum==2.1.2
py-buzz==1.0.3
PyJWT==1.7.1
python-dateutil==2.8.1
python-dotenv==0.14.0
pytzdata==2020.1
six==1.15.0
SQLAlchemy==1.3.19
Werkzeug==1.0.1
wrapt==1.12.1

### Route Testing
If you're using VSCode there is a handy plugin called Rest Client by Huachao Mao. Simply open up the test.rest and confirm your routes are functioning correctly.