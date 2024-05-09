from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Replace the following values with your actual Supabase credentials
DATABASE_URL = "postgres://postgres.zpaipupkywpctcmqorsw:ing-sw-i-20241-todo-list@aws-0-sa-east-1.pooler.supabase.com:5432/postgres"

engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)