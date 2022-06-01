from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_mongoengine import MongoEngine

database_name = 'blogDatabase'
password = '9849559082'
DB_URI = f'mongodb+srv://laxmanMaharjan:{password}@cluster17.dadlw.mongodb.net/{database_name}?retryWrites=true&w=majority'

app = Flask(__name__)

@app.route('/')
def index():
    return "api is working"


DATABASE ={
        'host':DB_URI,
        'connect':False
        }

app.config["MONGODB_SETTINGS"]=DATABASE
# app.config["MONGODB_HOST"]=DB_URI

SWAGGER_SETTINGS = {
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
}
app.config.update(SWAGGER_SETTINGS)

db = MongoEngine(app)

docs = FlaskApiSpec(app)


from crudApp.views import CreateResource
from crudApp.views import crud_blueprint
docs.register(CreateResource, blueprint="crud", endpoint='create')
#from swaggerApi.views import swagger_blueprint
app.register_blueprint(crud_blueprint)
#app.register_blueprint(swagger_blueprint)

