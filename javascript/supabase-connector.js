const { createClient } = require('@supabase/supabase-js');

class SupabaseConnector {
  constructor(supabaseUrl, supabaseKey) {
    this.supabase = createClient(supabaseUrl, supabaseKey);
  }

  async insert(tableName, data) {
    try {
      const { data: result, error } = await this.supabase
        .from(tableName)
        .insert(data)
        .select();

      if (error) throw error;
      return { success: true, data: result };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async select(tableName, query = {}) {
    try {
      let request = this.supabase.from(tableName).select('*');
      
      // Filtros básicos
      if (query.where) {
        Object.keys(query.where).forEach(key => {
          request = request.eq(key, query.where[key]);
        });
      }

      const { data, error } = await request;

      if (error) throw error;
      return { success: true, data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async update(tableName, query, updateData) {
    try {
      let request = this.supabase.from(tableName).update(updateData);
      
      Object.keys(query).forEach(key => {
        request = request.eq(key, query[key]);
      });

      const { data, error } = await request.select();

      if (error) throw error;
      return { success: true, data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async delete(tableName, query) {
    try {
      let request = this.supabase.from(tableName).delete();
      
      Object.keys(query).forEach(key => {
        request = request.eq(key, query[key]);
      });

      const { data, error } = await request.select();

      if (error) throw error;
      return { success: true, data };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }
}

module.exports = SupabaseConnector;