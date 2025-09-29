// Exemplo de uso em JavaScript
const MongoConnector = require('../javascript/mongo-connector');
const SupabaseConnector = require('../javascript/supabase-connector');

// Configurações (use variáveis de ambiente na produção)
const MONGO_URI = 'sua_connection_string_mongodb';
const SUPABASE_URL = 'sua_url_supabase';
const SUPABASE_KEY = 'sua_key_supabase';

async function examples() {
  console.log('=== EXEMPLO MONGODB ===');
  
  const mongo = new MongoConnector(MONGO_URI);
  await mongo.connect();
  
  // Inserir dados
  const insertResult = await mongo.insert('users', {
    name: 'João Silva',
    email: 'joao@email.com',
    age: 30
  });
  console.log('Insert:', insertResult);
  
  // Buscar dados
  const findResult = await mongo.find('users', { name: 'João Silva' });
  console.log('Find:', findResult);
  
  await mongo.disconnect();

  console.log('\n=== EXEMPLO SUPABASE ===');
  
  const supabase = new SupabaseConnector(SUPABASE_URL, SUPABASE_KEY);
  
  // Inserir dados
  const supabaseInsert = await supabase.insert('users', {
    name: 'Maria Santos',
    email: 'maria@email.com',
    age: 25
  });
  console.log('Supabase Insert:', supabaseInsert);
  
  // Buscar dados
  const supabaseSelect = await supabase.select('users', {
    where: { name: 'Maria Santos' }
  });
  console.log('Supabase Select:', supabaseSelect);
}

examples().catch(console.error);