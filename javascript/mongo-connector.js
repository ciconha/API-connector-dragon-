const { MongoClient } = require('mongodb');

class MongoConnector {
  constructor(connectionString) {
    this.connectionString = connectionString;
    this.client = null;
    this.db = null;
  }

  async connect() {
    try {
      this.client = new MongoClient(this.connectionString);
      await this.client.connect();
      this.db = this.client.db();
      console.log('✅ Conectado ao MongoDB Atlas com sucesso!');
      return true;
    } catch (error) {
      console.error('❌ Erro ao conectar com MongoDB:', error);
      return false;
    }
  }

  async disconnect() {
    if (this.client) {
      await this.client.close();
      console.log('🔌 Desconectado do MongoDB');
    }
  }

  async insert(collectionName, data) {
    try {
      const collection = this.db.collection(collectionName);
      const result = await collection.insertOne(data);
      return { success: true, id: result.insertedId };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async find(collectionName, query = {}) {
    try {
      const collection = this.db.collection(collectionName);
      const results = await collection.find(query).toArray();
      return { success: true, data: results };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async update(collectionName, query, updateData) {
    try {
      const collection = this.db.collection(collectionName);
      const result = await collection.updateOne(query, { $set: updateData });
      return { success: true, modifiedCount: result.modifiedCount };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async delete(collectionName, query) {
    try {
      const collection = this.db.collection(collectionName);
      const result = await collection.deleteOne(query);
      return { success: true, deletedCount: result.deletedCount };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }
}

module.exports = MongoConnector;