from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Chongdae(Resource):
    def get(self):
        return {
            'products': [
                'Ice Cream',
                'Chocolate',
                'Fruit',
                'Tdest'
            ]
        }
api.add_resource(Chongdae, '/')
if __name__ == '__main__':
    app.run(host='0.0.0', port=80, debug=True)