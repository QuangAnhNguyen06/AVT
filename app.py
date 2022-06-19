from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

#from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'QA'
api = Api(app)

#jwt = JWT(app,authenticate,identity)

items = []

class Item(Resource): #kế thừa Resource
	#@jwt_required()
	def  get(self, name): #filter lọc qua các gt name 
		item = next(filter(lambda x: x['name'] == name, items), None) # None ở cuối là gt trả về khi hàm next đạt gt end
		return {"item": item}, 200 if item else 404
	
	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None) is not None:
			return {'message': "Item voi name '{}' da ton tai".format(name)} ,400
		
		data = request.get_json()
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Xoa Item'}

	def put(self, name):
		data = request.get_json()
		item = next(filter(lambda x: x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else:
			item.update(data)
		return item


class ItemList(Resource):
	def get(self):
		return {'items': items}



api.add_resource(Item , '/item/<string:name>')
api.add_resource(ItemList , '/items')
app.run(port=5000)