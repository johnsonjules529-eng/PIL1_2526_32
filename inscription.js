<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inscription — IFRI MentorLink</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="page-scroll">
    <div class="container--wide">
      <div class="card">

        <div class="card-logo">
          <span class="badge">IFRI_MentorLink</span>
          <h1 class="card-title">Créer mon compte</h1>
          <p class="card-subtitle">Rejoignez le réseau d'entraide de l'IFRI</p>
        </div>

        <div class="msg msg-error"   id="msg-error"></div>
        <div class="msg msg-success" id="msg-success"></div>

        <form id="register-form" novalidate>

          <!-- Nom / Prénom -->
          <div class="form-row">
            <div class="form-group">
              <label for="lastname">Nom</label>
              <input type="text" id="lastname" placeholder="ex : SOSSOU" autocomplete="family-name" required>
            </div>
            <div class="form-group">
              <label for="firstname">Prénom</label>
              <input type="text" id="firstname" placeholder="ex : Jean" autocomplete="given-name" required>
            </div>
          </div>

          <!-- E-mail -->
          <div class="form-group">
            <label for="email">E-mail institutionnel</label>
            <div class="input-wrap">
              <input class="has-icon" type="email" id="email" placeholder="jean.sossou@ifri.uac.bj" autocomplete="email" required>
              <svg class="input-icon" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
            </div>
          </div>

          <!-- Téléphone -->
          <div class="form-group">
            <label for="phone">Numéro de téléphone</label>
            <div class="input-wrap">
              <input class="has-icon" type="tel" id="phone" placeholder="+229 97 00 00 00" autocomplete="tel" required>
              <svg class="input-icon" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
            </div>
          </div>

          <!-- École -->
          <div class="form-group">
            <label for="school">École</label>
            <select id="school" required>
              <option value="" disabled selected hidden>Choisir votre école</option>
              <option value="IFRI">IFRI — Institut de Formation et de Recherche en Informatique</option>
              <option value="Autre">Autre entité de l'UAC</option>
            </select>
          </div>

          <!-- Filière / Niveau -->
          <div class="form-row">
            <div class="form-group">
              <label for="branch">Filière</label>
              <select id="branch" required>
                <option value="" disabled selected hidden>Sélectionner</option>
                <option value="GL">GL — Génie Logiciel</option>
                <option value="SI">SI — Sécurité Informatique</option>
                <option value="IA">IA — Intelligence Artificielle</option>
                <option value="IM">IM — Internet des Objets &amp; Multimédia</option>
                <option value="SE&IoT">SE&amp;IoT</option>
              </select>
            </div>
            <div class="form-group">
              <label for="level">Niveau d'études</label>
              <select id="level" required>
                <option value="" disabled selected hidden>Sélectionner</option>
                <option value="licence1">Licence 1</option>
                <option value="licence2">Licence 2</option>
                <option value="licence3">Licence 3</option>
                <option value="master1">Master 1</option>
                <option value="master2">Master 2</option>
              </select>
            </div>
          </div>

          <!-- Mot de passe / Confirmation -->
          <div class="form-group">
            <label for="password">Mot de passe</label>
            <div class="input-wrap">
              <input class="has-icon" type="password" id="password" placeholder="8 caractères minimum" autocomplete="new-password" required>
              <svg class="input-icon" viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
            </div>
          </div>

          <div class="form-group">
            <label for="confirm">Confirmer le mot de passe</label>
            <div class="input-wrap">
              <input class="has-icon" type="password" id="confirm" placeholder="••••••••" autocomplete="new-password" required>
              <svg class="input-icon" viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
            </div>
          </div>

          <div class="btn-group">
            <button class="btn btn-primary" type="submit" id="submit-btn">
              Finaliser l'inscription
            </button>
          </div>

        </form>

        <p class="footer-note">
          Déjà inscrit ?
          <a class="link" href="connexion.html">Se connecter</a>
        </p>

      </div>
    </div>
  </div>
  <script src="inscription.js"></script>
</body>
</html>
