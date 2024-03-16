from redis import Redis
from app.system_db.orders import CRUDOrders


redis_client = Redis()
def cache_order(user_id,order_id):
    user_orders = redis_client.lrange(f"user_id_{user_id}",0,10)
    if not str(order_id).encode("ascii") in user_orders:
        redis_client.lpush(f"user_id_{user_id}",order_id)
        redis_client.ltrim(f"user_id_{user_id}",0,11)
    order = redis_client.hgetall(f"order:{order_id}")
    order_data = {}
    for k,v in order.items():
        order_data[f"{k.decode('utf-8')}"] = v.decode("utf-8")
    return order_data
    
    
def add_orders(order_id,title,body,main_image,images,full_price,price):
    order_data = {
        "title":title,
        "body":body,
        "main_image":main_image,
        "images":images,
        "full_price":full_price,
        "price":price
    }

    redis_client.hset(f"order:{order_id}",mapping=order_data)

    return order_id

        

