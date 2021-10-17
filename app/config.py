import os

from dotenv import load_dotenv


load_dotenv()

db_user = os.getenv("DB_USERNAME")
db_pw = os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://{db_user}:{db_pw}@127.0.0.1:5432/testimonial"
