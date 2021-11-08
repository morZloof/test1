from sanic import response

def send_error(err):#send error status
    return response.json(
            {'error': err},
            headers={'X-Served-By': 'sanic'},
            status=500
        )

def send_success(msg):#send success status
    return response.json(
            {'success': msg},
            headers={'X-Served-By': 'sanic'},
            status=200
        )