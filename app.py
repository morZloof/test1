from sanic import Sanic
from sanic.response import json
import json as jsonModule
from get_reservations import get_reservations
from cancel_reservation import cancel_reservation
from add_reservation import add_reservation
from room_inventory import room_inventory

app = Sanic("My Hello, world app")

# http://127.0.0.1:8000/addReservation?hotelId=2&roomType=small&checkIn=1636291039807&checkOut=1636291039806&status=active
@app.route('/addReservation')
async def add_reservation_api(request):
    return add_reservation(request)

#http://127.0.0.1:8000/cancelReservation?id=4d441196-5788-46e4-a151-02c18c1bc312
@app.route('/cancelReservation')
async def cancel_aeservation_api(request):
    return cancel_reservation(request)

#http://127.0.0.1:8000/roomInventory?checkIn=2021-10-01&checkOut=2021-12-01
@app.route('/roomInventory')
async def room_inventory_api(request):
    return room_inventory(request)

#http://127.0.0.1:8000/getReservations?id=1
@app.route('/getReservations')
async def get_reservations_api(request):
    return get_reservations(request)

if __name__ == '__main__':
    app.run()