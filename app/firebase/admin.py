import firebase_admin

from firebase_admin import credentials

from app.config import FIREBASE_CREDENTIALS_JSON_PATH


creds = credentials.Certificate(FIREBASE_CREDENTIALS_JSON_PATH)
firebase_app = firebase_admin.initialize_app(creds)
