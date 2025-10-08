# 🧳 Agent Autonome de Planification de Voyage  

## 🚀 Description du projet  
Ce projet met en place un **agent IA autonome** capable de planifier un **itinéraire de voyage complet** en utilisant :  

- 🌐 **Recherche web en temps réel** pour obtenir les meilleures informations (vols, hôtels, attractions, météo).  
- ⚙️ **Function Calling** pour connecter l’agent à des **API externes** (Google Maps, Skyscanner, OpenWeather, Booking, etc.).  
- 🤖 **Raisonnement autonome** : l’agent choisit lui-même quelles fonctions appeler, dans quel ordre, et combine les résultats pour créer un plan cohérent.  

---

## 🛠️ Technologies Clés  
- **IA Agentique** : un agent autonome qui réfléchit, planifie et agit.  
- **Function Calling** : permet à l’IA d’appeler des fonctions définies pour interagir avec le monde réel.  
- **API Externes** : intégration avec des services de voyage (vols, hôtels, météo, cartes).  
- **Langage** : Python / Node.js (selon implémentation choisie).  
- **Orchestration** : utilisation d’un framework agentique (LangChain, OpenAI Agents, etc.).  

---

## 📂 Fonctionnalités  
✅ Trouver et comparer des vols ✈️  
✅ Réserver ou suggérer des hôtels 🏨  
✅ Vérifier la météo et ajuster l’itinéraire 🌦️  
✅ Proposer des activités locales 🗺️  
✅ Générer un itinéraire optimisé (jour par jour) 📅  
✅ Adapter les choix selon le **budget** et le **style de voyage** (détente, aventure, culture).  

---

## ⚙️ Comment ça marche ?  

### 1. Entrée utilisateur  
Tu indiques :  
- La **destination** (ex: Tokyo 🇯🇵)  
- Les **dates de voyage**  
- Ton **budget** et préférences  

### 2. Raisonnement de l’agent  
L’agent :  
1. Analyse la demande  
2. Décide quelles fonctions appeler (ex: `searchFlights`, `getHotels`, `getWeather`, `findAttractions`)  
3. Combine les résultats  
4. Produit un **plan de voyage complet**  

### 3. Sortie  
Un **itinéraire détaillé**, par exemple :  

Jour 1 : Arrivée à Tokyo - installation à l’hôtel Shinjuku
Jour 2 : Visite du quartier d’Asakusa + Tokyo Skytree
Jour 3 : Excursion au Mont Fuji (météo favorable)
Jour 4 : Shopping à Shibuya et Harajuku
Jour 5 : Retour


---

## 📦 Installation  

```bash
# Cloner le projet
git clone https://github.com/username/travel-agent.git
cd travel-agent

# Installer les dépendances
npm install   # ou pip install -r requirements.txt

# Configurer les clés API (Google Maps, Skyscanner, OpenWeather…)
cp .env.example .env

# Lancer l’agent
npm run start   # ou python main.py

Planifie un voyage à Lisbonne pour 5 jours avec un budget moyen.


📖 Exemple de scénario

👉 Entrée :

"Je veux aller à Barcelone du 5 au 10 août, budget 1200€, je préfère la culture et la gastronomie."

👉 Sortie (extrait généré) :

Vol recommandé : Paris → Barcelone (Air France, 120€ A/R)

Hôtel 3★ dans le quartier de l’Eixample (450€ total)

Jour 1 : arrivée + tapas tour 🍷
Jour 2 : Sagrada Familia + Parc Güell
Jour 3 : Marché de la Boqueria + musée Picasso
Jour 4 : Excursion à Montserrat
Jour 5 : plage + retour

Architecture
User Request
      ⬇️
  Agent (LLM + Reasoning)
      ⬇️
 Function Calling (APIs)
      ⬇️
  Aggregation & Planning
      ⬇️
    Travel Itinerary
