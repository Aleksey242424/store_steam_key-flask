#from app.spider import download_image
from app import create_app



if __name__ == "__main__":
    #download_image.download_image()
    app = create_app()
    app.run()