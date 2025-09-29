from supabase import create_client, Client
from typing import Dict, List, Any, Optional
import os

class SupabaseConnector:
    def __init__(self, supabase_url: str, supabase_key: str):
        self.supabase: Client = create_client(supabase_url, supabase_key)
    
    def insert(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            response = self.supabase.table(table_name).insert(data).execute()
            return {"success": True, "data": response.data}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def select(self, table_name: str, query: Dict[str, Any] = None) -> Dict[str, Any]:
        try:
            request = self.supabase.table(table_name).select("*")
            
            if query and 'where' in query:
                for key, value in query['where'].items():
                    request = request.eq(key, value)
            
            response = request.execute()
            return {"success": True, "data": response.data}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def update(self, table_name: str, query: Dict[str, Any], update_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            request = self.supabase.table(table_name).update(update_data)
            
            for key, value in query.items():
                request = request.eq(key, value)
            
            response = request.execute()
            return {"success": True, "data": response.data}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def delete(self, table_name: str, query: Dict[str, Any]) -> Dict[str, Any]:
        try:
            request = self.supabase.table(table_name).delete()
            
            for key, value in query.items():
                request = request.eq(key, value)
            
            response = request.execute()
            return {"success": True, "data": response.data}
        except Exception as e:
            return {"success": False, "error": str(e)}