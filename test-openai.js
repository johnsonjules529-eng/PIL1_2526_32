const http = require('http');

// Test: Message sans mot-clé automatique (devrait utiliser OpenAI)
const testMessage = {
    sender: "Test User",
    content: "Quelle est la capitale de la France?"
};

const postData = JSON.stringify(testMessage);

const options = {
    hostname: 'localhost',
    port: 3000,
    path: '/api/messages',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': postData.length
    }
};

console.log('🤖 Test d\'OpenAI (sans mot-clé automatique)\n');
console.log('Message:', testMessage.content);
console.log('\n⏳ Génération de réponse par OpenAI...\n');

const req = http.request(options, (res) => {
    let data = '';

    res.on('data', (chunk) => {
        data += chunk;
    });

    res.on('end', () => {
        try {
            const response = JSON.parse(data);
            console.log('✅ Réponse reçue:\n');
            console.log('Status:', response.status);
            console.log('Source:', response.source || 'N/A');
            console.log('Réponse IA:', response.autoResponse);
        } catch (e) {
            console.error('❌ Erreur:', e.message);
        }
    });
});

req.on('error', (error) => {
    console.error('❌ Erreur:', error.message);
    console.error('Vérifiez que le serveur est en cours d\'exécution sur http://localhost:3000');
});

req.write(postData);
req.end();
