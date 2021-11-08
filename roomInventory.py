from query import queryInsert,querySelect
import json as jsonModule
from sanic import response
from responses import sendError, sendSuccess

def roomInventory(request):
    if 'checkIn' in request.args:
        check_in = request.args['checkIn'][0]
    else:
        return sendError('check_in is missing')

    if 'checkOut' in request.args:
        check_out = request.args['checkOut'][0]
    else:
        return sendError('check_out is missing')

    res = querySelect(f"SELECT * FROM reservations WHERE check_in>'{check_in}' and check_out<'{check_out}'")

    return sendSuccess(jsonModule.dumps(res, indent=0, sort_keys=True, default=str))