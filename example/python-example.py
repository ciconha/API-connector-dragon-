# Exemplo de uso em Python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'python'))

from mongo_connector import MongoConnector
from supabase_connector import SupabaseConnector

# Configurações (use variáveis de ambiente na produção)
MONGO_URI = "sua_connection_string_mongodb"
SUPABASE_URL = "sua_url_supabase"
SUPABASE_KEY = "sua_key_supabase"

def run_examples():
    print("=== EXEMPLO MONGODB ===")
    
    mongo = MongoConnector(MONGO_URI)
    if mongo.connect():
        # Inserir dados
        insert_result = mongo.insert("users", {
            "name": "Carlos Oliveira",
            "email": "carlos@email.com",
            "age": 35
        })
        print("Insert:", insert_result)
        
        # Buscar dados
        find_result = mongo.find("users", {"name": "Carlos Oliveira"})
        print("Find:", find_result)
        
        mongo.disconnect()

    print("\n=== EXEMPLO SUPABASE ===")
    
    supabase = SupabaseConnector(SUPABASE_URL, SUPABASE_KEY)
    
    # Inserir dados
    supabase_insert = supabase.insert("users", {
        "name": "Ana Costa",
        "email": "ana@email.com",
        "age": 28
    })
    print("Supabase Insert:", supabase_insert)
    
    # Buscar dados
    supabase_select = supabase.select("users", {
        "where": {"name": "Ana Costa"}
    })
    print("Supabase Select:", supabase_select)

if __name__ == "__main__":
    run_examples()