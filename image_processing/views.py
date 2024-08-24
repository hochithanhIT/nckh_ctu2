from django.http.response import HttpResponse
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

firebase = pyrebase.initialize_app(
    {
        "apiKey": os.getenv("FIREBASE_API_KEY"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
        "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.getenv("FIREBASE_APP_ID"),
    }
)
storage = firebase.storage()


def upload_to_firebase(req):
    image_url = upload_helper()
    return HttpResponse(image_url)


def upload_helper():
    # Use the credentials obtained during project setup on Firebase, leave
    # databaseUrl as "", since we aren't using Firebase provided database
    # services for our app
    file_path = "G:/HoChiThanh/NCKH/nckh_project/media/images/acne-5_jpeg.rf.2d6671715f0149df7b494c4d3f12a98b.jpg"  # specify absolute path to any image on your local computer
    image_name = "random_image_1"

    storage.child(f"images/{image_name}.jpg").put(file_path)
    url = storage.child(f"images/{image_name}.jpg").get_url(None)
    
    return url
