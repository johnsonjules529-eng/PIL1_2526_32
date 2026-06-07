const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./messages.db', (err) => {
    if (err) {
        console.error('Erreur:', err.message);
        process.exit(1);
    }
});

console.log('\n📊 TEST DE LA BASE DE DONNÉES\n');

// Vérifier les réponses automatiques
db.all('SELECT COUNT(*) as count FROM auto_responses', (err, rows) => {
    if (err) {
        console.error('Erreur:', err.message);
    } else {
        console.log('Nombre de réponses automatiques:', rows[0].count);
    }
});

// Vérifier les messages
db.all('SELECT COUNT(*) as count FROM messages', (err, rows) => {
    if (err) {
        console.error('Erreur:', err.message);
    } else {
        console.log('Nombre de messages:', rows[0].count);
    }
});

// Afficher quelques réponses
setTimeout(() => {
    db.all('SELECT keyword, response FROM auto_responses LIMIT 5', (err, rows) => {
        if (err) {
            console.error('Erreur:', err.message);
        } else {
            console.log('\n📝 Exemples de réponses automatiques:');
            rows.forEach((row, index) => {
                console.log(`  ${index + 1}. "${row.keyword}" → "${row.response.substring(0, 50)}..."`);
            });
        }
        db.close();
    });
}, 1000);
