from sanic import Sanic
from sanic.response import json
import json as jsonModule
from getReservations import getReservations
from cancelReservation import cancelReservation
from addReservation import addReservation
from roomInventory import roomInventory
from sanic import response

app = Sanic("My Hello, world app")

# http://127.0.0.1:8000/addReservation?hotelId=2&roomType=small&checkIn=1636291039807&checkOut=1636291039806&status=active
@app.route('/addReservation')
async def addReservationApi(request):
    return addReservation(request)

#http://127.0.0.1:8000/cancelReservation?id=4d441196-5788-46e4-a151-02c18c1bc312
@app.route('/cancelReservation')
async def cancelReservationApi(request):
    return cancelReservation(request)

#http://127.0.0.1:8000/roomInventory?checkIn=2021-10-01&checkOut=2021-12-01
@app.route('/roomInventory')
async def roomInventoryApi(request):
    return roomInventory(request)

#http://127.0.0.1:8000/getReservations?id=1
@app.route('/getReservations')
async def getReservationsApi(request):
    return getReservations(request)

if __name__ == '__main__':
    app.run()