import json as jsonModule
from query import query_select
from responses import send_error, send_success

def get_reservations(request):
    # return {'success': 'ok'}
    if 'id' in request.args:
        id = int(request.args['id'][0])
    else:
        return send_error('id is missing (hotel_id)')

    sql = f"SELECT hotels_id,check_in FROM reservations where hotels_id={id}"
    res = query_select(sql)
    
    return send_success(jsonModule.dumps(res, indent=0, sort_keys=True, default=str))