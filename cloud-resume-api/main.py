import os
from flask import jsonify
from google.cloud import firestore

def read(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)
    
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    try:
        db = firestore.Client(database=os.getenv('DATABASE_NAME'))
        collection_name = os.getenv('COLLECTION_NAME')
        visitors_ref = db.collection(collection_name)
        visitors = [doc.to_dict() for doc in visitors_ref.stream()]
        return jsonify(visitors), 200, headers
    except Exception as e:
        return f"An error Occured: {e}", 404, headers