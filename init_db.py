from database import Base, engine
from models import Task  # Import models to register them

# Create all tables in the database
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")

