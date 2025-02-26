from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# Database URL
DATABASE_URL = "sqlite:///./tasks.db"

# Create Engine and Session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ensure metadata is reused to prevent duplicate table issues
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Task Model
class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}  # Prevent duplicate table errors

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)  # Optional field


