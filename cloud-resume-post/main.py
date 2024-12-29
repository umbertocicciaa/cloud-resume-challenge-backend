import os
from google.cloud import firestore

def update_visitor(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    
    db = firestore.Client(database=os.getenv('DATABASE_NAME'))
    collection_name = os.getenv('COLLECTION_NAME')
    document_id = os.getenv('DOCUMENT_ID')
    
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()
    
    if doc.exists:
        current_count = doc.to_dict().get('counter', 0)
        new_count = current_count + 1
        
        doc_ref.update({'counter': new_count})
        
        return f"Counter updated to {new_count}", 200, headers
    else:
        return "Document not found", 404, headers