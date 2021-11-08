from query import query_select
import json as jsonModule
from responses import send_error, send_success

def room_inventory(request):
    if 'checkIn' in request.args:
        check_in = request.args['checkIn'][0]
    else:
        return send_error('check_in is missing')

    if 'checkOut' in request.args:
        check_out = request.args['checkOut'][0]
    else:
        return send_error('check_out is missing')

    res = query_select(f"SELECT * FROM reservations WHERE check_in>'{check_in}' and check_out<'{check_out}'")

    return send_success(jsonModule.dumps(res, indent=0, sort_keys=True, default=str))