#import modul
"""from app.spider import download_image"""
#add data in model orders
'''from app.spider import db_init'''
#part for insert orders in redis

'''from app.cache_orders import add_orders'''


from app import create_app

'''from app.system_db.users import CRUDUsers'''

if __name__ == "__main__":
    #download image
    """download_image.download()"""

    #add in redis orders
    app = create_app()
    app.run(host="0.0.0.0")