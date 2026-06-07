const http = require('http');

// Test 1: Message sans réponse automatique (devrait utiliser OpenAI)
const testMessage = {
    sender: "Test User",
    content: "Comment apprendre la programmation?"
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

console.log('🧪 Test d\'envoi de message à l\'API\n');
console.log('Message envoyé:', testMessage);
console.log('\n⏳ Attente de la réponse...\n');

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
            console.log('Réponse:', response.autoResponse);
            
            // Récupérer l'historique
            const getOptions = {
                hostname: 'localhost',
                port: 3000,
                path: '/api/messages',
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            };

            const getReq = http.request(getOptions, (getRes) => {
                let messages = '';
                getRes.on('data', (chunk) => messages += chunk);
                getRes.on('end', () => {
                    try {
                        const msgList = JSON.parse(messages);
                        console.log('\n📜 Derniers messages dans la base:\n');
                        msgList.slice(-3).forEach(msg => {
                            console.log(`[${msg.sender}] ${msg.content.substring(0, 60)}...`);
                        });
                    } catch (e) {
                        console.error('Erreur parsing messages:', e.message);
                    }
                });
            });

            getReq.end();
        } catch (e) {
            console.error('❌ Erreur parsing réponse:', e.message);
            console.log('Data brute:', data);
        }
    });
});

req.on('error', (error) => {
    console.error('❌ Erreur requête:', error.message);
});

req.write(postData);
req.end();
