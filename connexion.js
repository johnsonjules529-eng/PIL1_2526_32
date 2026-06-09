(function () {
  "use strict";

  const form      = document.getElementById("login-form");
  const emailIn   = document.getElementById("email");
  const passIn    = document.getElementById("password");
  const submitBtn = document.getElementById("submit-btn");
  const msgError  = document.getElementById("msg-error");

  /* Affiche un message d'erreur */
  function showError(text) {
    msgError.textContent = text;
    msgError.classList.add("show");
    msgError.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  /* Cache le message d'erreur */
  function clearError() {
    msgError.classList.remove("show");
  }

  /* Validation e-mail simple */
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  /* État du bouton pendant chargement */
  function setLoading(loading) {
    submitBtn.disabled = loading;
    submitBtn.textContent = loading ? "Connexion en cours…" : "Se connecter";
  }

  /* Soumission du formulaire */
  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    clearError();

    const email    = emailIn.value.trim();
    const password = passIn.value;

    /* --- Validation côté client --- */
    if (!email) {
      showError("Veuillez saisir votre adresse e-mail.");
      emailIn.focus();
      return;
    }

    if (!isValidEmail(email)) {
      showError("Format d'e-mail invalide.");
      emailIn.focus();
      return;
    }

    if (!password) {
      showError("Veuillez saisir votre mot de passe.");
      passIn.focus();
      return;
    }

    if (password.length < 4) {
      showError("Mot de passe trop court.");
      passIn.focus();
      return;
    }

    setLoading(true);

    /* --- Appel API backend (à connecter à Flask/Django) ---
       Remplacez l'URL par votre endpoint réel, ex: /api/login
       Le backend vérifie le mot de passe haché en base de données.
    */
    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok && data.success) {
        /* Stocke les infos non-sensibles pour la session UI */
        sessionStorage.setItem("ml_email", email);
        sessionStorage.setItem("ml_role",  data.role  || "user");
        sessionStorage.setItem("ml_nom",   data.nom   || "");
        sessionStorage.setItem("ml_prenom",data.prenom|| "");

        /* Redirige selon le rôle */
        if (data.role === "admin") {
          window.location.href = "admin.html";
        } else {
          window.location.href = "choix.html";
        }

      } else {
        showError(data.message || "E-mail ou mot de passe incorrect.");
      }

    } catch (err) {
      /* Mode démo hors-ligne (à retirer en production) */
      if (err instanceof TypeError) {
        console.warn("[DÉMO] Serveur non disponible — simulation de connexion.");
        sessionStorage.setItem("ml_email",  email);
        sessionStorage.setItem("ml_role",   "user");
        sessionStorage.setItem("ml_nom",    "Doe");
        sessionStorage.setItem("ml_prenom", "John");
        window.location.href = "choix.html";
      } else {
        showError("Erreur réseau. Vérifiez votre connexion et réessayez.");
      }
    } finally {
      setLoading(false);
    }
  });

  /* Cache l'erreur dès que l'utilisateur modifie un champ */
  emailIn.addEventListener("input", clearError);
  passIn.addEventListener("input",  clearError);

})();
