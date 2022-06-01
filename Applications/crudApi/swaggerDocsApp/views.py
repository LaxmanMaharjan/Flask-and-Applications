from flask import request, Blueprint, jsonify, make_response
from flask.views import MethodView
from crudApp.models import User
from crudApp.serializers import UserSchema

from swaggerDocsApp.serializers import PostSchema
from swaggerDocsApp.models import Post

from crudApi import app

swagger_blueprint = Blueprint('swagger',__name__)

class CreateView(MethodView):
    """Performing CRUD in post"""

    def get(self):
        try:
            posts = Post.objects.all()
            result = PostSchema(many=True).dump(posts)
            return make_response(jsonify(result)), 200

        except Exception as e:
            print(e.__class__)
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.',
                'exception': str(e)
        }
            return make_response(jsonify(responseObject)), 401

    def post(self):
        try:
            received_data = request.get_json()
            user = User.objects(pk=received_data.get('user')).first()
            deserialized_data = UserSchema().dump(user)
            received_data['user'] = deserialized_data

            data= PostSchema().load(received_data)
            # user = User(user_id = data.get('user_id'),first_name=data.get('first_name'),last_name=data.get('last_name'), email=data.get('email'))
            post = Post(user=user, title=data['title'], content=data['content'])
            post.save()
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
            print(data)
            post = Post.objects(pk=id).first()
            print(post)
            if post == None:
                responseObject = {
                    'status': 'fail',
                    'message': 'No user found with provided id.'
                }
                return make_response(jsonify(responseObject)), 401
            #user.update(user_id = data.get('user_id'),first_name=data.get('first_name'),last_name=data.get('last_name'))
            post.update(content=data.get('content'))

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
            post = Post.objects(pk=id).first()
            if post == None:
                responseObject = {
                    'status': 'fail',
                    'message': 'No user found with provided id.'
                }
                return make_response(jsonify(responseObject)), 401
            post.delete()
            responseObject = {
                'status': 'success',
                'message': 'Successfully deleted.',
            }
            return make_response(jsonify(responseObject)), 201

        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.',
                'exception':str(e)
        }
            return make_response(jsonify(responseObject)), 401



create_post_view = CreateView.as_view('create_api')
modification_view = UpdateDeleteView.as_view('modification_api')

swagger_blueprint.add_url_rule(
        "/swaggerapp/",
        view_func=create_post_view,
        methods = ["GET","POST"]
        )
swagger_blueprint.add_url_rule(
        "/swaggerapp/<string:id>",
        view_func=modification_view,
        methods = ["PUT","DELETE"]
        )


@app.route('/hello')
def index1():
    return "hello world"

@app.route('/populate_post',methods=["POST"])
def populate_post():
    user = User.objects.all()[0]
    print(user)
    post = Post(title="The Batman",content="They think i'm hiding in shadows.",user=user)
    post.save()
    return "done"
