from sanic import response

def sendError(err):#send error status
    return response.json(
            {'error': err},
            headers={'X-Served-By': 'sanic'},
            status=500
        )

def sendSuccess(msg):#send success status
    return response.json(
            {'success': msg},
            headers={'X-Served-By': 'sanic'},
            status=200
        )