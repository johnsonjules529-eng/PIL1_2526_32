require('dotenv').config();

const express = require('express');
const path = require('path');

// Initialiser la base de données d'abord
const db = require('./config/database');

// Ensuite, utiliser les routes
const messageRoutes = require('./routes/messageRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware pour pouvoir lire le JSON envoyé par le front-end
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rendre le dossier 'public' accessible (pour notre interface HTML)
app.use(express.static(path.join(__dirname, 'public')));

// Utiliser nos routes de messagerie
app.use('/api/messages', messageRoutes);

// Gestion globale des erreurs
app.use((err, req, res, next) => {
    console.error('Erreur serveur :', err);
    res.status(500).json({ error: 'Erreur serveur : ' + err.message });
});

// Démarrer le serveur
app.listen(PORT, () => {
    console.log(`✓ Serveur de messagerie actif sur : http://localhost:${PORT}`);
    console.log(`✓ Accédez à l'interface : http://localhost:${PORT}`);
    console.log(`✓ OpenAI API: ${process.env.OPENAI_API_KEY && process.env.OPENAI_API_KEY !== 'your_api_key_here' ? '✓ Configuré' : '✗ Non configuré'}`);
});