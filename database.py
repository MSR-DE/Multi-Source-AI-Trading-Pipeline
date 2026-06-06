from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession
from sqlalchemy.orm import declarative_base

## URL to DB
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./trading_api.db"


## 1) Engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

## Session local
SessionLocal = async_sessionmaker(autoflush=False, autocommit=False, bind=engine, class_=AsyncSession)

## Base 

Base = declarative_base()


## Bouncer to open the door

async def get_db():

    db = SessionLocal()
    try: 
        yield db 
    finally: 
        await db.close()



    





