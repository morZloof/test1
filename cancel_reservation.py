import json as jsonModule
from query import query_insert
from responses import send_error, send_success

def cancel_reservation(request):
    if 'id' in request.args:
        id = request.args['id'][0]
    else:
        return send_error('id is missing')

    sql = f"UPDATE reservations SET status='cancelled' WHERE id='{id}'"
    query_insert(sql)

    return send_success('reservation canceled')