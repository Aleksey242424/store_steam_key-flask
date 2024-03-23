from redis import Redis
from app.system_db.orders import CRUDOrders


redis_client = Redis()
def cache_order(user_id,order_id):
    user_orders = redis_client.lrange(f"user_id_{user_id}",0,-1)
    if not str(order_id).encode("ascii") in user_orders:
        redis_client.lpush(f"user_id_{user_id}",order_id)
    redis_client.ltrim(f"user_id_{user_id}",0,11)
    order = redis_client.hgetall(f"order:{order_id}")
    order_data:dict = {k.decode('utf-8'):v.decode("utf-8") for k,v in order.items()}
    order_data["body"] = [content.decode("utf-8") for content in redis_client.lrange(f"order_content_{order_id}",0,-1)]
    return order_data

def get_orders(page):
    orders:dict = {}
    for i in range(int(page)*10-10,int(page)*10):
        if i == 0:continue
        order = redis_client.hgetall(f"order:{i}")
        orders[f"order_id:{i}"] = {}
        for k,v in order.items():
            orders[f"order_id:{i}"][k.decode("utf-8")] = v.decode("utf-8")
    return orders
    
    
def add_orders(order):
    title = ""
    add_chars = lambda char,content:content + char
    data = order.title.split("_")[:-1]
    for item in data:
        if not item.isupper():
            for char in item:
                if char.isupper():
                    title = add_chars(" ",title)
                title = add_chars(char,title)
        else:
            title = add_chars(item,title) + " "
    for content in order.body.split("^"):
        redis_client.lpush(f"order_content_{order.order_id}",content)
    order_data = {
        "order_id":order.order_id,
        "title":title.strip(),
        "main_image":order.main_image,
        "images":order.images,
        "full_price":order.full_price,
        "price":order.price
    }

    redis_client.hset(f"order:{order.order_id}",mapping=order_data)

    return order.order_id

'''for order in CRUDOrders.get_order_for_redis():
    print(add_orders(order))'''

        
def get_order_by_id(order_id):
    order = {k.decode("utf-8"):v.decode("utf-8") for k,v in redis_client.hgetall(f"order:{order_id}").items()}
    return order

def get_orders_by_id(orders_id):
    orders = [redis_client.hgetall(f"order:{order_id[0]}") for order_id in orders_id]
    order:dict={}
    for i in range(len(orders)):
        for k,v in orders[i].items():
            order[k.decode("utf-8")] = v.decode("utf-8")
        orders[i] = order.copy()
        order.clear()
    return orders

def get_order_history_list(user_id):
    order:dict = {}
    order_id_list = redis_client.lrange(f"user_id_{user_id}",0,-1)
    for order_id in order_id_list:
        order_data = redis_client.hgetall(f"order:{order_id.decode('utf-8')}")
        order[f"order:{order_id.decode('utf-8')}"] = {}
        for k,v in order_data.items():
            order[f"order:{order_id.decode('utf-8')}"][k.decode("utf-8")] = v.decode("utf-8")
    return order

def get_count_group():
    return round(len(redis_client.keys("order:*"))/10)
