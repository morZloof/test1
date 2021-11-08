import uuid
import datetime
from query import query_insert,query_select
import json as jsonModule
from sanic import response
from responses import send_error,send_success

def add_reservation(request):
    id = str(uuid.uuid4())
    if 'id' in request.args:#if the user didn't send the id
        id = request.args['id'][0]
    
    if 'hotelId' in request.args:
        hotel_id = request.args['hotelId'][0]
    else:
        return send_error('hotelId is missing')

    if 'roomType' in request.args:
        room_type = request.args['roomType'][0]
    else:
        return send_error('roomType is missing')

    if 'checkIn' in request.args:
        check_in = int(request.args['checkIn'][0])
        check_in = datetime.date.fromtimestamp(check_in/1000.0)
    else:
        return send_error('checkIn is missing')

    if 'checkOut' in request.args:
        check_out = int(request.args['checkOut'][0])
        check_out = datetime.date.fromtimestamp(check_out/1000.0)
    else:
        return send_error('checkOut is missing')

    if 'status' in request.args:
        status = request.args['status'][0]
    else:
        return send_error('status is missing')

    if status != 'active' and status != 'cancelled':
        return send_error('status invalud, you can send only cancelled or active')

    #check that the hotel exist 
    checkHotel = query_select(f"SELECT count(*) as counter FROM hotels WHERE id = {hotel_id}")
    
    if checkHotel[0][0] == 0:
        return send_error("hotel doesn't exist")

    #check that the room exist
    checkRoom = query_select(f"SELECT amount FROM rooms WHERE hotels_id={hotel_id} and room_type='{room_type}'")
    
    if len(checkRoom) == 0 or len(checkRoom[0]) == 0:
        return send_error("room doesn't exist")
    
    amountRooms = checkRoom[0][0] # the number of rooms the hotel have
    roomsReserved = query_select(f"SELECT count(*) FROM reservations WHERE hotels_id={hotel_id} and room_type='{room_type}'")

    if len(roomsReserved) > 0 and roomsReserved[0][0]>=amountRooms:
        return send_error("All rooms are occupied")

    try:
        sql = f"INSERT INTO reservations (id,hotels_id,room_type,check_in,check_out,status) values ('{id}',{hotel_id},'{room_type}','{check_in}','{check_out}','{status}')"
        query_insert(sql)
    except:
        return send_error("insert failed")

    return send_success('reservation saved')