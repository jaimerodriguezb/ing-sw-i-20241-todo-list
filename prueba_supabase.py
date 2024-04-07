import os
from supabase import create_client

url = "https://asndmmlykkcminkzyruq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzbmRtbWx5a2tjbWlua3p5cnVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI1MDA5NDQsImV4cCI6MjAyODA3Njk0NH0.VgKOkeQonU3vZSqy0BdPrG5xREXxnSv_I1mfo-O_dys"
supabase = create_client(url, key)


response = supabase.table('Activity').select("*").execute()

print(response)


data, count = supabase.table('Category').insert({"cate_name": "Cuidado Personal"}).execute()