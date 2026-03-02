from fastapi import APIRouter

order_router = APIRouter(prefix = '/orders', tags = ['orders'])

@order_router.get('/')
async def order():
  return {'message': 'You are in the orders route.'}