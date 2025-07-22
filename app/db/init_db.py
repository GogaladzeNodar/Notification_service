from app.db.session import sync_engine, Base  
from app.models.notification import Notification  

def init_db():
    Base.metadata.create_all(bind=sync_engine) 
if __name__ == "__main__":
    init_db()