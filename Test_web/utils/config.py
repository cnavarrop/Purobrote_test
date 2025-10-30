from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    url_staging = os.getenv("URL_STAGING")
    correo_cliente = os.getenv("CORREO_CLIENTE")
    correo_admin = os.getenv("CORREO_ADMIN")
    pass_cliente = os.getenv("PASS_CLIENTE")
    pass_admin = os.getenv("PASS_ADMIN")
    bienvenida_cliente = os.getenv("Bienvenida_Cliente")
