import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')
valid_pers_acc = os.getenv('valid_pers_acc')