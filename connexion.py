<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Connexion — IFRI MentorLink</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="page-center">
    <div class="container">
      <div class="card">

        <div class="card-logo">
          <div class="logo-circle">
            <svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
          </div>
          <h1 class="card-title">IFRI_MentorLink</h1>
          <p class="card-subtitle">Connectez-vous pour retrouver votre mentor</p>
        </div>

        <div class="msg msg-error" id="msg-error"></div>

        <form id="login-form" novalidate>

          <div class="form-group">
            <label for="email">Adresse e-mail</label>
            <div class="input-wrap">
              <input class="has-icon" type="email" id="email" placeholder="etudiant@ifri.uac.bj" autocomplete="email" required>
              <svg class="input-icon" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
            </div>
          </div>

          <div class="form-group">
            <label for="password">Mot de passe</label>
            <div class="input-wrap">
              <input class="has-icon" type="password" id="password" placeholder="••••••••" autocomplete="current-password" required>
              <svg class="input-icon" viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
            </div>
          </div>

          <div class="btn-group">
            <button class="btn btn-primary" type="submit" id="submit-btn">
              Se connecter
            </button>
          </div>

        </form>

        <p class="footer-note">
          Pas encore de compte ?
          <a class="link" href="inscription.html">Créer un compte</a>
        </p>

      </div>
    </div>
  </div>
  <script src="connexion.js"></script>
</body>
</html>
