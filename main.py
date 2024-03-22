#import modul
"""from app.spider import download_image"""
#add data in model orders
"""from app.spider import db_init"""
#part for insert orders in redis
"""
from app.system_db.orders import CRUDOrders
from app.store.cache_orders import add_orders
"""

from app import create_app



if __name__ == "__main__":
    #download image
    """download_image.download()"""

    #add in redis orders
    '''for order in CRUDOrders.get_order_for_redis():
        add_orders(order.order_id,order.title,order.body,order.main_image,order.images,order.full_price,order.price)'''
    
    app = create_app()
    app.run(host="0.0.0.0")