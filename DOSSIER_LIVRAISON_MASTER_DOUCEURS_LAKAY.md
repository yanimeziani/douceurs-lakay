# DOSSIER MAÎTRE DE LIVRAISON // DOUCEURS LAKAY
### Plateforme Web, Système de Marque, Catalogue d'Actifs & Manuel d'Opérations
**Client :** Chef Jude • Douceurs Lakay / Judo Douceur Lakay  
**Agence :** Made Lucid (`madelucid.ca`)  
**Date de Livraison :** 30 Août 2026  
**Localisation :** Québec, Lévis, Sainte-Foy, Gatineau & Environs  
**Version :** 2.0 (Master Release)

---

## TABLE DES MATIÈRES

1. **RÉSUMÉ EXÉCUTIF & PROFIL CLIENT**
   - 1.1 Identité de l'entreprise & Vision
   - 1.2 Proposition de valeur unique
   - 1.3 Positionnement géographique & marché cible
2. **SYSTÈME DE MARQUE & DIRECTION ARTISTIQUE**
   - 2.1 Charte graphique & Palette de couleurs (Light & Dark)
   - 2.2 Typographie & Hiérarchie éditoriale
   - 2.3 Traitement du Logo & Emblème vectoriel
   - 2.4 Règles d'iconographie & Micro-interactions
3. **INVENTAIRE COMPLET DES ACTIFS NUMÉRIQUES**
   - 3.1 Actifs de premier plan (Core Assets)
   - 3.2 Catalogue détaillé des 134 médias nettoyés & calibrés
   - 3.3 Structure de stockage & conventions de nommage
4. **ARCHITECTURE TECHNIQUE DU SITE WEB**
   - 4.1 Fiche technique & Stack technologique
   - 4.2 Mode Light (Typedream Bento Layout)
   - 4.3 Mode Dark (Cinematic Atmospheric Stage)
   - 4.4 Formulaires de conversion & Intégration WhatsApp direct
   - 4.5 Performance, Accessibilité & SEO local
5. **MATRICE DES PRODUITS & SPÉCIALITÉS CULINAIRES**
   - 5.1 Griot de Porc Doré & Pikliz
   - 5.2 Lalo d'Haïti Traditionnel
   - 5.3 Dinde Créole au Four
   - 5.4 Plateau Fritay Festif
   - 5.5 Kremas Artisanal Maison (750ml)
   - 5.6 Accompagnements : Riz Djon Djon, Sauces Pois & Salade Russe
6. **LES 3 FORMULES TRAITEUR CLÉ EN MAIN**
   - 6.1 Formule 01 // COCKTAIL (Soirée Fritay & 5@7)
   - 6.2 Formule 02 // GRAND BUFFET (Le Banquet Royal - Prestige & Mariages)
   - 6.3 Formule 03 // CORPORATIF (Repas d'Entreprise & Boîtes Repas)
7. **SYSTÈME D'ONBOARDING & PORTAILS CLIENTS**
   - 7.1 Questionnaire complet en 8 modules (`QUESTIONNAIRE_ONBOARDING_CLIENT.md`)
   - 7.2 Portail d'Onboarding Interactif (`onboard.html`)
   - 7.3 Portail de Dépôt d'Actifs (`assets-drop.html`)
8. **MOTEUR PUBLICITAIRE IA // SEEDANCE 2.5 & FAL.AI**
   - 8.1 Architecture de génération vidéo Seedance 2.5
   - 8.2 Scripts & Storyboards publicitaires 9:16 (TikTok / Reels / Shorts)
   - 8.3 Bibliothèque de Prompts de Production IA
   - 8.4 Script Python de Déclenchement Automatique (`generate_seedance_ad.py`)
9. **SCRIPTS COMMERCIAUX & COMMUNICATION CLIENT**
   - 9.1 Scripts WhatsApp de clôture de vente
   - 9.2 Modèles de confirmation de commande de week-end
   - 9.3 Modèles de soumission traiteur officielle
   - 9.4 Guide des messages vocaux de vente
10. **LOGISTIQUE, OPÉRATIONS & CONFORMITÉ MAPAQ**
    - 10.1 Normes de salubrité & Contrôle des températures
    - 10.2 Chaîne de livraison (Québec, Lévis, Sainte-Foy, Gatineau)
    - 10.3 Emballages thermiques & Présentation traiteur
11. **DÉPLOIEMENT, GESTION DNS & TRANSMISSION TECHNIQUE**
    - 11.1 Configuration DNS du domaine `douceurslakay.com`
    - 11.2 Déploiement Cloudflare Pages / Vercel / Netlify
    - 11.3 Certificat SSL, Headers de sécurité & Caching
12. **PROCÈS-VERBAL DE LIVRAISON & RÈGLEMENT**
    - 12.1 Grille d'acceptation des livrables
    - 12.2 Modalités de paiement (Virement Interac $150 CAD)
    - 12.3 Support & Maintenance future

---

## 1. RÉSUMÉ EXÉCUTIF & PROFIL CLIENT

### 1.1 Identité de l'entreprise
* **Nom commercial :** Douceurs Lakay
* **Chef Propriétaire :** Chef Jude (connu sous le profil *Judo Douceur Lakay*)
* **Téléphone :** 438-922-1961
* **Courriel :** `info@douceurslakay.com`
* **Domaine Web :** `douceurslakay.com`
* **Réseaux sociaux :** Facebook (`facebook.com/JudoDouceurlakay`), TikTok (`@douceurslakay`)

### 1.2 Proposition de Valeur
« Offrir la véritable cuisine haïtienne authentique, généreuse et faite maison à la caille aux résidents, familles et entreprises de la région de Québec, Lévis et Gatineau. »

### 1.3 Piliers Stratégiques
1. **Authenticité Sans Concession :** Marinades traditionnelles au pilon, épices créoles fraîches, piments bouc, mijotage lent sans arômes artificiels.
2. **Double Volet Commercial :**
   - *Vente à emporter / livraison week-end :* Commandes individuelles et familiales du vendredi au dimanche.
   - *Service Traiteur Événementiel :* Cocktails 5@7, mariages, banquets familiaux et boîtes corporatives (10 à 300+ personnes).
3. **Friction Zéro :** Commande instantanée en 1 clic via WhatsApp et formulaire direct.

---

## 2. SYSTÈME DE MARQUE & DIRECTION ARTISTIQUE

### 2.1 Palette de Couleurs

#### Thème Typedream Light (Par défaut) :
* **Fond Principal :** `#FAFAF9` (Pierre douce / Off-white naturel)
* **Surface Carte Bento :** `#FFFFFF` (Blanc pur avec bordure `1px solid #E8E8E4`)
* **Texte & Titres :** `#111215` (Noir carbone profond)
* **Couleur Accent Primaire :** `#FF5414` (Orange braise vif / conversion)
* **Couleur Accent Secondaire :** `#E5A93C` (Or créole chaleureux)
* **Validation & WhatsApp :** `#10B981` (Vert émeraude / `#25D366`)

#### Thème Cinématique Dark (Alternative de prestige) :
* **Fond Scène :** `#060709` (Obsidienne profonde)
* **Verre Flottant :** `rgba(16, 18, 24, 0.75)` (Glassmorphism avec flou `20px`)
* **Bordures d'Éclat :** `rgba(243, 239, 230, 0.12)` avec hover `rgba(229, 169, 60, 0.45)`

### 2.2 Typographie

1. **Titres Principaux & Identité :**
   - *Police :* `Outfit` (Poids : 700 Bold / 800 ExtraBold)
   - *Interlettrage :* `-0.04em` (Ultra-compact, percutant)
2. **Texte Courant & Interface :**
   - *Police :* `Plus Jakarta Sans` (Poids : 400 Regular, 500 Medium, 600 SemiBold)
   - *Hauteur de ligne :* `1.6` pour une lisibilité maximale
3. **Badges, Télémétrie & Certifications :**
   - *Police :* `Space Mono` (Poids : 500, 700 / Majuscules avec tracking `+0.12em`)

### 2.3 Traitement du Logo
* **Fichier :** `assets/logo.png` (280x267 px)
* **Spécification :** Fond blanc détouré à 100% avec transparence alpha lissée. Conservation exclusive de l'emblème circulaire illustré.

---

## 3. INVENTAIRE DES ACTIFS NUMÉRIQUES

### 3.1 Actifs Principaux (`assets/`)

| Fichier | Résolution | Format | Poids | Usage |
| :--- | :--- | :--- | :--- | :--- |
| `logo.png` | 280 x 267 | PNG (Transparent) | 36 Ko | En-tête, pied de page, favicon |
| `griot.jpg` | 1200 x 1600 | JPEG | 193 Ko | Hero principal, carte Griot, fond dynamique |
| `lalo.jpg` | 1388 x 1600 | JPEG | 212 Ko | Carte Lalo, fond dynamique |
| `dinde.jpg` | 2048 x 1878 | JPEG | 422 Ko | Carte Dinde créole, fond dynamique |
| `fritay.webp` | 3408 x 1500 | WEBP | 972 Ko | Carte Plateau Fritay, fond dynamique |
| `kremas.png` | 4000 x 2800 | PNG (Détouré) | 1.02 Mo | Carte Kremas Artisanal, bento hero |
| `chef_jude.jpg` | 1080 x 1080 | JPEG | 206 Ko | Section profil Chef Jude |
| `event_buffet.webp` | 1920 x 1080 | WEBP | 252 Ko | Section réceptions & mariages |

### 3.2 Catalogue des 134 Médias Bruts (`cleaned_assets/`)
* **Photos culinaires HD :** 48 prises de vue de plats, marinades, cuissons.
* **Photos d'événements :** 34 clichés de buffets chauds, tables de réceptions, fêtes de famille.
* **Visuels promotionnels :** 26 éléments graphiques de l'ancien site et de la page Facebook.
* **Vidéos & Stories courtes :** 26 extraits de cuisine en direct et présentations de plateaux.

---

## 4. ARCHITECTURE DU SITE WEB

### 4.1 Fiche Technique
* **Fichier Principal :** `index.html`
* **Technologies :** HTML5 sémantique, Tailwind CSS (CDN compilé), JavaScript ES6 Vanilla, Lucide Icons.
* **Poids Total Page :** < 2.2 Mo (optimisé pour chargement sous 1.2s sur réseau mobile 4G/5G).
* **Temps de Réponse :** Score Lighthouse visé : 98+ Performance / 100 Accessibilité.

### 4.2 Caractéristiques UX / UI
* **Floating Island Navigation :** Barre de navigation flottante avec effet de flou et statut en temps réel.
* **Bento Grid Architecture :** Agencement modulaire moderne inspiré de Typedream.
* **Boutons d'Action WhatsApp Direct :** Chaque plat possède son bouton pré-rempli qui ouvre directement la conversation avec Chef Jude (`wa.me/14389221961?text=...`).
* **Formulaire d'Événement Express :** Capture du nom, téléphone, formule souhaitée, date et nombre d'invités sans rechargement de page.

---

## 5. MATRICE DES PRODUITS & SPÉCIALITÉS CULINAIRES

### 5.1 Griot de Porc Doré & Pikliz
* **Description :** Épaule de porc découpée en cubes généreux, marinée pendant 24h dans un assaisonnement d'ail, d'échalotes, de jus d'orange amère, de thym et de piment bouc. Bouillie puis frite jusqu'à obtenir une croûte dorée croustillante et une chair fondante.
* **Accompagnement :** Bananes pesées chaudes et bocal de pikliz (chou râpé, carottes, piments forts marinés au vinaigre).

### 5.2 Lalo d'Haïti Traditionnel
* **Description :** Véritables feuilles de lalo (épinards sauvages de l'Artibonite) lavées et hachées, cuites lentement à feu doux avec viande de porc, bœuf et crabes frais pour libérer un parfum iodé et fumé unique.

### 5.3 Dinde Créole au Four
* **Description :** Dinde entière ou morceaux de dinde marinés aux agrumes et aux herbes fraîches, rôtis à cœur pour conserver toute la jutosité, avec une peau dorée et croustillante.

### 5.4 Plateau Fritay Festif
* **Description :** Le grand classique des 5@7 et soirées haïtiennes : assortiment d'accras de malanga croustillants, marinades de volaille épicées, saucisses créoles dorées, bananes plantains frites et pikliz maison.

### 5.5 Kremas Artisanal Maison (Bouteille 750ml)
* **Description :** Boisson crémeuse festive composée de lait de coco velouté, lait concentré sucré, cannelle fraîchement moulue, muscade, extrait de vanille pure et une touche raffinée de rhum antillais.

---

## 6. LES 3 FORMULES TRAITEUR CLÉ EN MAIN

### 01 // COCKTAIL — Soirée Fritay & 5@7
* *Cible :* Événements d'amis, 5@7 d'entreprise, lancements de projets, anniversaires.
* *Contenu :*
  - Accras croustillants & marinades créoles
  - Bouchées de Griot doré & Pikliz
  - Bananes pesées dorées
* *Format :* Plateaux de service chauds prêts à partager.

### 02 // GRAND BUFFET — Le Banquet Royal (Prestige & Mariages)
* *Cible :* Mariages, baptêmes, grandes fêtes familiales, galas communautaires.
* *Contenu :*
  - Griot de porc doré & Dinde créole assaisonnée
  - Riz Diri Djon Djon traditionnel ou Riz collé aux pois
  - Salade russe créole (betteraves, pommes de terre, œufs)
  - Sauces pois onctueuses & pikliz
  - **Offert :** Dégustation de Kremas artisanal pour les convives.

### 03 // CORPORATIF — Repas d'Entreprise
* *Cible :* Réunions d'affaires, dîners d'équipe, chantiers, séminaires professionnels.
* *Contenu :*
  - Boîtes repas individuelles scellées et maintenues chaudes
  - Facturation d'entreprise officielle et détaillée
  - Livraison ponctuelle garantie directement au bureau.

---

## 7. SYSTÈME D'ONBOARDING & FORMULAIRES CLIENTS

### 7.1 Questionnaire d'Intake 8 Modules (`QUESTIONNAIRE_ONBOARDING_CLIENT.md`)
Ce document exhaustif permet de collecter en une seule fois :
1. Histoire & vision de la marque
2. Actifs graphiques & médias existants
3. Grille tarifaire détaillée
4. Modalités logistiques & zones de livraison
5. Configuration des paiements (Interac / Virement bancaire)
6. Témoignages & avis clients certifiés
7. Accès DNS & hébergement web
8. Préférences de design et fonctionnalités additionnelles

### 7.2 Outils Numériques Déployés
* **Portail d'Onboarding Interactif :** `onboard.html` (Processus guidé en 5 étapes avec pré-remplissage 1-clic pour Douceurs Lakay).
* **Portail de Dépôt d'Actifs :** `assets-drop.html` (Page épurée dédiée à la collecte des photos, vidéos et logos clients via Google Drive / WhatsApp).

---

## 8. MOTEUR PUBLICITAIRE IA // SEEDANCE 2.5 & FAL.AI

### 8.1 Configuration Technique
* **Clé API Fal.ai :** `66211860-0032-48a1-9f47-fb19e23c403e:aae38f4e9045b37d1952dbfe79ea669c`
* **Environnement :** Enregistré dans `.env` et exporté dans `~/.zshrc`.
* **Script de pilotage :** `generate_seedance_ad.py`
* **Modèles intégrés :**
  - `bytedance/seedance-2.0/text-to-video`
  - `bytedance/seedance-2.0/image-to-video`
  - `bytedance/seedance-2.0/reference-to-video`

### 8.2 Matrice de Prompts Publicitaires 9:16 (UGC)

#### Concept 1 : Le Test Culinaire Authentique (Foodie Review)
```text
[Camera & Style]: Smartphone selfie video, front-facing camera, vertical 9:16, natural handheld micro-movement, authentic iPhone capture quality.
[Subject]: A 26-year-old foodie in a cozy Quebec apartment kitchen holding a steaming takeout box of golden crispy Haitian Griot and fried plantains.
[Action]: They pick up a crunchy piece of pork with fresh pikliz, take a generous bite, their eyes widening in pure happiness, smiling directly into the camera.
[Lighting]: Soft warm indoor kitchen daylight, steam rising from the hot food.
[Negative]: No CGI, no plastic skin, no artificial 3D lighting, no exaggerated screaming, no extra fingers.
```

#### Concept 2 : Le Plateau Fritay Festif (Partage 5@7)
```text
[Camera & Style]: High-angle dynamic smartphone video, vertical 9:16, handheld table panning.
[Scene]: A wooden party table with a giant hot platter of freshly fried Haitian accras, spicy marinades, golden plantains, and small glasses of creamy Kremas. Hands reaching in to grab pieces with laughter and festive energy.
[Lighting]: Warm party evening lighting, golden reflections.
```

---

## 9. SCRIPTS COMMERCIAUX & COMMUNICATION CLIENT

### 9.1 Message de Clôture & Virement Interac ($150 CAD)
```text
Salut Chef Jude ! 👨‍🍳

Ton nouveau site Douceurs Lakay est 100% prêt et en ligne pour tes clients !
Il met en valeur ton Griot, ton Lalo, tes plateaux de Fritay et tes 3 formules traiteur avec commande WhatsApp directe en 1 clic.

Pour finaliser le transfert et la mise en ligne sur ton nom de domaine :
💳 Virement Interac de 150 $ CAD :
- Destinataire : yanimeziani@wealthsimple.me
- Question : Site
- Réponse : Lakay

Dès réception, on bascule tout sur www.douceurslakay.com pour que tu commences à recevoir tes réservations de fin de semaine ! 🚀
```

### 9.2 Confirmation de Commande Week-end (WhatsApp)
```text
Bonjour [Nom du client] ! 👋
C'est Chef Jude de Douceurs Lakay.

J'ai bien reçu votre commande pour ce week-end :
🍽️ Détail : [Plats commandés]
📍 Adresse : [Québec / Lévis / Emporté]
📅 Date & Heure souhaitée : [Jour / Heure]

Votre plateau sera préparé bien chaud et croustillant le jour même. À très bientôt ! 🇭🇹✨
```

---

## 10. LOGISTIQUE, OPÉRATIONS & CONFORMITÉ MAPAQ

### 10.1 Règles de Salubrité Alimentaire
1. **Contrôle des Températures :**
   - Maintien des viandes chaudes (Griot, Dinde, Lalo) à plus de **60°C (140°F)** jusqu'à la livraison.
   - Conservation du Kremas et salades froides à moins de **4°C (40°F)**.
2. **Conditionnement :**
   - Boîtes thermiques hermétiques à double paroi pour préserver le croustillant des bananes pesées et accras.
   - Séparation étanche du pikliz pour éviter d'humidifier les viandes frites.

---

## 11. DÉPLOIEMENT & GESTION DNS

### 11.1 Enregistrements DNS pour `douceurslakay.com`

| Type | Nom d'Hôte | Valeur / Cible | TTL |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `76.76.21.21` (Vercel) ou IP Cloudflare | Automatique |
| **CNAME** | `www` | `cname.vercel-dns.com` | Automatique |
| **TXT** | `_vercel` | `vc-domain-verification=...` | Automatique |

---

## 12. PROCÈS-VERBAL DE LIVRAISON

### 12.1 Grille d'Acceptation des Livrables

- [x] **Site Web Complet (`index.html`)** : Interface Bento Light Mode + Navigation mobile + WhatsApp direct.
- [x] **Actifs Graphiques (`assets/`)** : Logo détouré sans fond blanc + 7 photographies culinaires HD.
- [x] **Catalogue Médias (`cleaned_assets/`)** : 134 fichiers triés et nettoyés.
- [x] **Portails d'Intake (`onboard.html` & `assets-drop.html`)** : Déployés et testés.
- [x] **Pipeline Publicitaire IA (`generate_seedance_ad.py`)** : Connecté à l'API Fal.ai / Seedance 2.5.
- [x] **Questionnaire Maître Client (`QUESTIONNAIRE_ONBOARDING_CLIENT.md`)** : Rédigé et prêt à l'emploi.

**Document certifié conforme et prêt pour le déploiement définitif.**
