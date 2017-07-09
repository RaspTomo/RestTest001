# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
import peewee
# import json

db = peewee.SqliteDatabase("data.db")

class Quote(peewee.Model):
    code = peewee.TextField()
    price = peewee.TextField()
    name = peewee.TextField()

    class Meta:
        database = db

api = Flask(__name__)

#Select
@api.route('/1.0/getQuote/<string:code>', methods=['GET'])
def get_quote(code):
    try:
        requestQ = Quote.get(Quote.code == code)
    except User.DoesNotExist:
        abort(404)

    result = {
        "result":True,
        "data":{
            "code":requestQ.code,
            "price":requestQ.price,
            "name":requestQ.name
            }
        }

    return make_response(jsonify(result))
    # Unicodeにしたくない場合は↓
    #return make_response(json.dumps(result, ensure_ascii=False))

#Update
@api.route('/1.0/getQuote/<string:code>', methods=['PUT'])
def put_quote(code):
    dataDict = json.loads(request.data)
    try:
        q = Quote.update(code=dataDict["code"], price=dataDict["price"], name=dataDict["name"]).where(Quote.code == dataDict["code"])
    except Quote.DoesNotExist:
        abort(404)

    result = {
        "result":True
        }

    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
