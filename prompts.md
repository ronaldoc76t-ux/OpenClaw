# 📦 Bibliothèque complète de prompts — Projet Camion-Benne Autonome + Drones Collecteurs
Version : 1.2  
Auteur : Ronald + Copilot  
Format : Markdown  
Usage : Copie-colle n’importe quel prompt dans Claude, GPT, Gemini ou Copilot pour générer les livrables correspondants.

---

# 🧠 PROMPT MAÎTRE — Orchestration complète du projet

Tu es un expert senior en robotique, systèmes multi‑agents, ROS2, simulation, architecture logicielle, cloud, sécurité, et coordination de flottes autonomes.

Ta mission : orchestrer la conception complète d’un système de collecte de déchets composé de :
- un camion‑benne autonome qui roule en permanence (pas de stationnement),
- une flotte de drones volants collecteurs,
- un backend cloud,
- une application mobile,
- un orchestrateur multi‑agents.

Contraintes majeures :
- Le camion ne s’arrête jamais : les drones doivent effectuer des rendez‑vous dynamiques avec un véhicule en mouvement.
- Les drones doivent prédire la position future du camion pour synchroniser le dépôt.
- Le système doit être modulaire, scalable, sécurisé et compatible ROS2.
- Le système doit fonctionner en environnement urbain dense.

Ta tâche :
1. Générer l’architecture haut‑niveau.
2. Générer l’architecture détaillée de chaque composant :
   - camion (mécanique, électronique, logiciel),
   - drones (mécanique, électronique, logiciel),
   - backend cloud,
   - application mobile,
   - coordination multi‑agents.
3. Proposer un plan de simulation complet.
4. Proposer un plan de développement complet.
5. Identifier les risques et stratégies d’atténuation.
6. Produire les diagrammes textuels nécessaires (Mermaid inclus).

Format attendu :
- Markdown structuré,
- tableaux,
- diagrammes textuels (Mermaid si utile),
- sections claires et exploitables par une équipe d’ingénierie.

Commence par l’architecture haut‑niveau.

---

# 🧱 1. ARCHITECTURE HAUT‑NIVEAU

## 🟦 Prompt 1 — Architecture système globale

Tu es un expert en robotique, systèmes multi‑agents, ROS2, simulation, et architecture logicielle.

Ta mission : produire l’architecture haut‑niveau complète d’un système de collecte de déchets composé de :
- un camion‑benne autonome qui roule en permanence,
- une flotte de drones volants collecteurs,
- un backend cloud,
- une application mobile,
- un orchestrateur multi‑agents.

Contraintes :
- Le camion ne s’arrête jamais.
- Les drones doivent effectuer des rendez‑vous dynamiques.
- Le système doit être modulaire, scalable, sécurisé et compatible ROS2.

Livrables :
1. Diagramme logique haut‑niveau.
2. Rôle de chaque composant.
3. Flux de données.
4. Contraintes critiques.
5. Liste des modules logiciels principaux.
6. Risques majeurs + atténuation.

Format : Markdown structuré.

---

## 🟦 Prompt 2 — Architecture fonctionnelle

Génère l’architecture fonctionnelle complète du système camion‑benne autonome + drones collecteurs.

Inclure :
- cas d’usage,
- flux opérationnels,
- interactions entre acteurs,
- séquences temporelles,
- préconditions et postconditions.

Contraintes :
- camion en mouvement continu,
- rendez‑vous dynamiques,
- plusieurs drones simultanés.

Format : Markdown + diagrammes textuels.

---

## 🟦 Prompt 3 — Architecture technologique

Produis l’architecture technologique complète du système camion + drones.

Inclure :
- choix des technologies (ROS2, DDS, simulateur, backend),
- communication camion ↔ drones ↔ backend,
- protocole de synchronisation,
- sécurité,
- langages et frameworks,
- contraintes temps réel,
- logs et télémétrie.

Format : Markdown structuré.

---

# 🚛 2. ARCHITECTURE DU CAMION AUTONOME

## 🟧 Prompt Camion 1 — Architecture mécanique & électronique

Décris l’architecture détaillée du camion‑benne autonome.

Inclure :
- châssis et modifications,
- capteurs (lidar, caméras, radar, GPS, IMU),
- actuateurs (direction, freinage, propulsion),
- trémie de réception pour drones,
- plateforme stabilisée pour dépôt en mouvement,
- compacteur,
- alimentation électrique,
- systèmes de sécurité.

Format : Markdown + tableaux.

---

## 🟧 Prompt Camion 2 — Architecture logicielle ROS2

Décris l’architecture logicielle ROS2 complète du camion‑benne autonome.

Inclure :
- nodes ROS2,
- topics, services, actions,
- navigation en mouvement continu,
- prédiction de trajectoire (30–120 s),
- gestion des rendez‑vous drones,
- gestion de la trémie,
- gestion des risques,
- interface backend.

Format : Markdown + schémas textuels.

---

# 🛸 3. ARCHITECTURE DES DRONES COLLECTEURS

## 🟩 Prompt Drone 1 — Architecture mécanique & électronique

Décris l’architecture détaillée d’un drone collecteur.

Inclure :
- type de drone,
- moteurs, ESC, batterie,
- capteurs (caméra, lidar léger, GPS, IMU),
- système de préhension,
- système de dépôt sécurisé dans un camion en mouvement,
- communication (5G, WiFi mesh),
- contraintes de masse et autonomie.

Format : Markdown + tableaux.

---

## 🟩 Prompt Drone 2 — Architecture logicielle ROS2

Décris l’architecture logicielle ROS2 complète d’un drone collecteur.

Inclure :
- nodes ROS2,
- topics, services, actions,
- détection des sacs/bacs,
- planification de trajectoire,
- synchronisation avec camion en mouvement,
- gestion batterie,
- gestion des échecs.

Format : Markdown structuré.

---

# ☁️ 4. ARCHITECTURE BACKEND CLOUD

## 🟦 Prompt Backend — Architecture cloud complète

Décris l’architecture backend complète du système.

Inclure :
- API,
- base de données,
- orchestrateur de missions,
- gestion des drones,
- gestion du camion,
- prédiction de trajectoire,
- gestion utilisateurs,
- sécurité,
- logs et télémétrie,
- scalabilité.

Format : Markdown + diagrammes textuels.

---

# 📱 5. ARCHITECTURE APPLICATION MOBILE

## 🟪 Prompt App — Architecture mobile

Décris l’architecture de l’application mobile pour les particuliers.

Inclure :
- écrans,
- flux utilisateur,
- API consommées,
- notifications,
- sécurité,
- paiements.

Format : Markdown structuré.

---

# 🧠 6. COORDINATION MULTI‑AGENTS

## 🟥 Prompt Coordination — Algorithmes multi‑agents

Décris l’architecture complète de la coordination multi‑agents entre :
- le camion en mouvement continu,
- plusieurs drones collecteurs,
- le backend.

Inclure :
- prédiction de position du camion,
- assignation des missions drones,
- gestion des conflits,
- fenêtres de rendez‑vous,
- protocole de communication,
- gestion des échecs.

Format : Markdown structuré.

---

# 🧪 7. SIMULATION

## 🟫 Prompt Simulation — Gazebo / Webots / Ignition

Décris un plan de simulation complet pour le système camion + drones.

Inclure :
- choix du simulateur,
- modèles 3D nécessaires,
- scénarios de test,
- simulation des rendez‑vous dynamiques,
- simulation des échecs,
- métriques de performance,
- intégration ROS2.

Format : Markdown structuré.

---

# 📅 8. PLAN DE DÉVELOPPEMENT

## 🟨 Prompt Planning — Roadmap 12 semaines

Génère un plan de développement complet sur 12 semaines pour le projet camion + drones.

Inclure :
- phases,
- jalons,
- livrables,
- dépendances,
- risques,
- ressources nécessaires.

Format : Markdown structuré.

---

# 🖼️ 9. PROMPTS POUR DIAGRAMMES MERMAID (fusionnés)

## 🟦 Prompt Mermaid 1 — Diagramme haut‑niveau du système

Génère un diagramme Mermaid représentant l’architecture haut‑niveau du système camion‑benne autonome + drones collecteurs.

Inclure :
- camion autonome,
- flotte de drones,
- backend cloud,
- application mobile,
- orchestrateur multi‑agents.

Format attendu :  
```mermaid
<diagramme ici>
