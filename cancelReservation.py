import json as jsonModule
from query import queryInsert
from responses import sendError, sendSuccess

def cancelReservation(request):
    if 'id' in request.args:
        id = request.args['id'][0]
    else:
        return sendError('id is missing')

    sql = f"UPDATE reservations SET status='cancelled' WHERE id='{id}'"
    queryInsert(sql)

    return sendSuccess('reservation canceled')