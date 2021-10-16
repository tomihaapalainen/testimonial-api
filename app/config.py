import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = f"""\
postgresql://{os.getenv("PSSQL_USERNAME")}:{os.getenv("PSSQL_PASSWORD")}@127.0.0.1:5432/testimonial\
"""
