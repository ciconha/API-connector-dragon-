from pymongo import MongoClient
from typing import Dict, List, Any, Union
import os

class MongoConnector:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.client = None
        self.db = None
    
    def connect(self) -> bool:
        try:
            self.client = MongoClient(self.connection_string)
            # Testa a conexão
            self.client.admin.command('ping')
            self.db = self.client.get_database()
            print("✅ Conectado ao MongoDB Atlas com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao conectar com MongoDB: {e}")
            return False
    
    def disconnect(self):
        if self.client:
            self.client.close()
            print("🔌 Desconectado do MongoDB")
    
    def insert(self, collection_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(data)
            return {"success": True, "id": str(result.inserted_id)}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def find(self, collection_name: str, query: Dict[str, Any] = None) -> Dict[str, Any]:
        try:
            if query is None:
                query = {}
            collection = self.db[collection_name]
            results = list(collection.find(query))
            # Convert ObjectId to string for JSON serialization
            for result in results:
                result['_id'] = str(result['_id'])
            return {"success": True, "data": results}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def update(self, collection_name: str, query: Dict[str, Any], update_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            collection = self.db[collection_name]
            result = collection.update_one(query, {"$set": update_data})
            return {"success": True, "modified_count": result.modified_count}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def delete(self, collection_name: str, query: Dict[str, Any]) -> Dict[str, Any]:
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(query)
            return {"success": True, "deleted_count": result.deleted_count}
        except Exception as e:
            return {"success": False, "error": str(e)}