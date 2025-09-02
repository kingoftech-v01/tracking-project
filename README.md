# 📱 Phone Number Analyzer 🔍

Un outil simple et efficace pour **analyser un numéro de téléphone international** et obtenir :  
- 🌍 **Pays** et **région**  
- 📡 **Fournisseur télécom (opérateur)**  
- ⏰ **Fuseaux horaires** possibles  
- 🗺️ **Localisation géographique approximative** via [OpenCage API](https://opencagedata.com/)  
- 🖥️ **Carte interactive générée en HTML** grâce à [Folium](https://python-visualization.github.io/folium/)  

Le tout accessible via une **interface graphique (Tkinter)** conviviale ! 🚀  

---

## ✨ Fonctionnalités

✔️ Analyse d’un numéro avec son **indicatif international**  
✔️ Récupération du **pays**, **région** et **opérateur téléphonique**  
✔️ Détermination du ou des **fuseaux horaires**  
✔️ Génération automatique d’une **carte HTML** ouverte dans le navigateur  
✔️ **Interface graphique** facile à utiliser  

---

## 📦 Installation

Clone le dépôt et installe les dépendances :  

git clone [https://github.com/tonutilisateur/phone-analyzer](https://github.com/kingoftech-v01/tracking-project).git

cd tracking-project

pip install -r requirements.txt

---

## 🔑 Configuration

1. Crée un compte sur [OpenCage](https://opencagedata.com/)  
2. Récupère ta **clé API**  
3. Ouvre le script et modifie la ligne suivante :  

OPENCAGE_KEY = "YOUR_OPENCAGE_API_KEY"

---

## 🚀 Utilisation

Lancer le programme :  

python phone_analyzer.py

Dans l’application :  
1. Entrez un numéro complet avec indicatif international  *(ex: `+14155552671`)*  
2. Cliquez sur **Analyser**  
3. Consultez :  
   - 📋 Infos détaillées dans l’interface  
   - 🌐 Carte générée dans `phone_location.html` (ouvrira automatiquement dans votre navigateur)  

---

## ⚠️ Limitations

- La localisation est **approximative** (niveau *pays/région*, pas suivi temps réel).  
- Ce script ne permet **PAS** de tracer un téléphone ou d’accéder à la position GPS exacte.  
- Destiné à un **usage éducatif et technique**.  

---

## 🔧 Exemple de sortie

  📌 Country : United States
  
  📍 Region : California
  
  📡 Carrier : AT&T Wireless
  
  ⏰ Timezone(s) : ('America/Los_Angeles',)
  
  🌍 Latitude : 36.7783, Longitude : -119.4179
  
  ✅ Carte générée : phone_location.html

---

## 🤝 Contribuer

Les contributions sont les bienvenues !  
- Ouvrez une **issue** pour proposer des améliorations 📝  
- Faites un **pull request** pour ajouter des fonctionnalités 🚀   

---

👤 Développé en Python & Tkinter


