#from app.spider import download_image
#from app.spider import db_init
from app import create_app
from app.system_db.orders import CRUDOrders
from app.store.cache_orders import add_orders



if __name__ == "__main__":
    #download_image.download_main_image()
    app = create_app()
    app.run(host="0.0.0.0")
    '''for order in CRUDOrders.get_order_for_redis():
        add_orders(order.order_id,order.title,order.body,order.main_image,order.images,order.full_price,order.price)'''