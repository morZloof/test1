import json as jsonModule
from query import querySelect
from responses import sendError, sendSuccess

def getReservations(request):
    # return {'success': 'ok'}
    if 'id' in request.args:
        id = int(request.args['id'][0])
    else:
        return sendError('id is missing (hotel_id)')

    sql = f"SELECT hotels_id,check_in FROM reservations where hotels_id={id}"
    res = querySelect(sql)
    
    return sendSuccess(jsonModule.dumps(res, indent=0, sort_keys=True, default=str))