import os
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url:str=os.getenv('DATABASE_URL','sqlite:///./mathspace.db')
    jwt_secret:str=os.getenv('JWT_SECRET','development-secret')
    cors_origins:str=os.getenv('CORS_ORIGINS','http://localhost:3000')
settings=Settings()
