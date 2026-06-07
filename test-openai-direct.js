const OpenAIService = require('./services/openaiService');

console.log('🔍 Vérification du service OpenAI\n');

console.log('OpenAI configuré?', OpenAIService.isConfigured());
console.log('Variable OPENAI_API_KEY:', process.env.OPENAI_API_KEY ? '✓ Présente' : '✗ Absente');

// Test de génération
console.log('\n⏳ Test de génération...\n');

OpenAIService.generateResponse('Bonjour, comment allez-vous?', [])
    .then(response => {
        console.log('✅ Réponse OpenAI reçue:');
        console.log(response);
    })
    .catch(error => {
        console.error('❌ Erreur OpenAI:', error.message);
    });
