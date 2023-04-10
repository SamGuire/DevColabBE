from flask import Blueprint,request,jsonify,Response

user_controller = Blueprint('user_controller',__name__,url_prefix='/users')

@user_controller.route('',methods=['GET'])
def get_user() :
    return 'A user',200

@user_controller.route('/<id>')
def get_user_by_id(id:int) :
    return f'user with {id}',200


@user_controller.route('',methods=['POST'])
def add_user() :
    user_data = request.json
    return jsonify(user_data),201