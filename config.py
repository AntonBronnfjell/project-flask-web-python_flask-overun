import os


def _normalize_database_url(url: str) -> str:
    # Ensure psycopg3 driver is used if scheme is plain postgresql
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


class Config:
    _default_url = "postgresql+psycopg://username:password@localhost/mi_flask_app"
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(os.environ.get("DATABASE_URL", _default_url))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "tu_clave_secreta_aqui")


