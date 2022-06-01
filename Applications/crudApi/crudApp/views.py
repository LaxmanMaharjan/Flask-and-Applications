from flask import request, Blueprint, jsonify, make_response
from flask.views import MethodView
from crudApp.serializers import UserSchema
from crudApp.models import User

from crudApi import app, docs
from flask_apispec import marshal_with
from flask_apispec import MethodResource


crud_blueprint = Blueprint('crud',__name__)

class CreateResource(MethodResource):
    """Performing CRUD in user"""

    @marshal_with(UserSchema(many=True), code=200)
    def get(self):
        try:
            users = User.objects.all()
            return users
            # result = UserSchema(many=True).dump(users)
            # return make_response(jsonify(result)), 200

        except Exception as e:
            print(e.__class__)
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
        }
            return make_response(jsonify(responseObject)), 401

    def post(self):
        try:
            data= UserSchema().load(request.get_json())
            # user = User(user_id = data.get('user_id'),first_name=data.get('first_name'),last_name=data.get('last_name'), email=data.get('email'))
            user = User(user_id = data['user_id'],first_name=data['first_name'],last_name=data['last_name'], email=data['email'])
            user.save()
            responseObject = {
                'status': 'success',
                'message': 'Successfully created.',
            }
            return make_response(jsonify(responseObject)), 201

        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.',
                'exception':str(e)
        }
            return make_response(jsonify(responseObject)), 401

class UpdateDeleteView(MethodView):

    def put(self,id=None):
        try:
            data = request.get_json()
            user = User.objects(pk=id).first()
            if user == None:
                responseObject = {
                    'status': 'fail',
                    'message': 'No user found with provided id.'
                }
                return make_response(jsonify(responseObject)), 401
            user.update(user_id = data.get('user_id'),first_name=data.get('first_name'),last_name=data.get('last_name'))
            responseObject = {
                'status': 'success',
                'message': 'Successfully updated.',
            }
            return make_response(jsonify(responseObject)), 201

        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.',
                'exception': str(e)
        }
            return make_response(jsonify(responseObject)), 401

    def delete(self, id = None):
        try:
            user = User.objects(pk=id).first()
            if user == None:
                responseObject = {
                    'status': 'fail',
                    'message': 'No user found with provided id.'
                }
                return make_response(jsonify(responseObject)), 401
            user.delete()
            responseObject = {
                'status': 'success',
                'message': 'Successfully deleted.',
            }
            return make_response(jsonify(responseObject)), 201

        except Exception:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
        }
            return make_response(jsonify(responseObject)), 401



# modification_view = UpdateDeleteView.as_view('modification_api')

crud_blueprint.add_url_rule(
        "/crud/",
        view_func = CreateResource.as_view('create'),
        methods = ["GET","POST"]
        )
# crud_blueprint.add_url_rule(
#         "/crud/<string:id>",
#         view_func=modification_view,
#         methods = ["PUT","DELETE"]
#         )

#app.add_url_rule('/crud', view_func=CreateView.as_view('crud'))

#docs.register(CreateView)

@app.route('/populate',methods=["POST"])
def populate():
    user = User(user_id="1",first_name="laxman",last_name="maharjan",email="lxmn@python.org")
    user.save()
    return "done"
