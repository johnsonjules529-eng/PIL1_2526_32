# Configuration OpenAI - Guide d'Installation

## Étape 1: Obtenir une clé API OpenAI

1. Allez sur https://platform.openai.com/account/api-keys
2. Connectez-vous avec votre compte OpenAI (créez-en un si nécessaire)
3. Cliquez sur "Create new secret key"
4. Copiez la clé générée

## Étape 2: Ajouter la clé à votre fichier .env

Ouvrez le fichier `.env` à la racine du projet et remplacez:
```
OPENAI_API_KEY=your_api_key_here
```

Par:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Collez votre clé API OpenAI à la place de `sk-xxxxx...`

## Étape 3: Redémarrer le serveur

Arrêtez le serveur (Ctrl+C) et relancez-le:
```bash
node server.js
```

Vous devriez voir dans le terminal:
```
✓ OpenAI API: ✓ Configuré
```

## Fonctionnement

- **Réponses automatiques**: Si le message contient un mot-clé connu, une réponse automatique est envoyée
- **OpenAI**: Si aucune réponse automatique n'est trouvée, OpenAI génère une réponse intelligente
- **Historique**: L'IA tient compte de l'historique de conversation pour des réponses cohérentes

## Coûts

Chaque appel à OpenAI coûte quelques centimes (très peu). Surveillez votre consommation sur https://platform.openai.com/account/billing/overview

## Notes de sécurité

- ⚠️ Ne partagez jamais votre clé API
- ⚠️ Le fichier `.env` ne doit jamais être commité sur Git
- ⚠️ Vérifiez régulièrement vos limites de consommation
