from flask import Blueprint, render_template, jsonify, request
import json
import os

base_route = Blueprint('base_route', __name__, url_prefix='/')

@base_route.route('/')
def home():
    cad_number = request.args.get('cadastral_number')
    return render_template('index.html', cad_number=cad_number)

@base_route.route('/land')
def land():
    cad_number = request.args.get('cad_num')
    print(cad_number)
    with open('src/data/kontur_test.json', 'r') as f:
        data = json.loads(f.read())
    features = data['features']
    cad_num = features[0]['properties']['cad_number']
    if cad_number == cad_num:
        return jsonify(data)
    else:
        return jsonify({})
        

@base_route.route('/ndvi')
def ndvi():
    with open('src/data/ndvi_test.json', 'r') as f:
        data = f.read()
        data = json.loads(data)
        return jsonify(data)