# 🚛 PROJET CAMION-BENNE AUTONOME + DRONES COLLECTEURS

## Vision CEO

**Produit** : Système de collecte de déchets autonome composé d'un camion-benne roulant en permanence et d'une flotte de drones collecteurs volants.

**Différenciateur** : Le camion ne s'arrête jamais — les drones doivent effectuer des rendez-vous dynamiques avec un véhicule en mouvement.

---

## Équipe & Rôles

| Agent | Rôle | Tâches |
|-------|------|--------|
| `arch-system` | Architecte Système | Architecture haut-niveau + fonctionnelle + technologique |
| `arch-truck` | Ingénieur Camion | Architecture mécanique, électronique, logicielle camion |
| `arch-drone` | Ingénieur Drones | Architecture mécanique, électronique, logicielle drones |
| `arch-backend` | Architecte Backend | API, BDD, orchestration, cloud |
| `arch-mobile` | Développeur Mobile | Application mobile utilisateurs |
| `coord-agent` | Spécialiste Multi-Agents | Coordination camion-drones, prédiction trajectoire |
| `sim-engineer` | Ingénieur Simulation | Plan simulation Gazebo/Webots |
| `pm` | PM / Roadmap | Plan développement 12 semaines, gestion risques |

---

## État du Projet

| Tâche | Status | Agent | Livrable |
|-------|--------|-------|----------|
| Architecture Haut-Niveau | ✅ Terminé | arch-system | 02-architecture-haut-niveau.md |
| Architecture Fonctionnelle | ✅ Terminé | arch-fonctionnelle | 03-architecture-fonctionnelle.md |
| Architecture Technologique | ✅ Terminé | arch-technologique | 04-architecture-technologique.md |
| Architecture Camion | ✅ Terminé | arch-truck | 05-camion.md |
| Architecture Drone | ✅ Terminé | arch-drone | 06-drone.md |
| Architecture Backend | ✅ Terminé (corrigé) | arch-backend | 07-backend.md |
| Architecture Mobile | ✅ Terminé (corrigé) | arch-mobile | 08-application-mobile.md |

## État du Projet

| Tâche | Status | Agent | Livrable | Notes |
|-------|--------|-------|----------|-------|
| Architecture Haut-Niveau | ✅ Terminé (corrigé) | arch-system | 02-architecture-haut-niveau.md | +QoS, DDS-Security, Edge |
| Architecture Fonctionnelle | ✅ Terminé (corrigé) | arch-fonctionnelle | 03-architecture-fonctionnelle.md | +erreurs, protocoles, trace |
| Architecture Technologique | ✅ Terminé | arch-technologique | 04-architecture-technologique.md | |
| Architecture Camion | ✅ Terminé (corrigé) | arch-truck | 05-camion.md | +bilan massique, 400kWh |
| Architecture Drone | ✅ Terminé (corrigé) | arch-drone | 06-drone.md | +autonomie réelle, PX4 |
| Architecture Backend | ✅ Terminé (corrigé) | arch-backend | 07-backend.md | +RGPD, CI/CD, Argon2 |
| Architecture Mobile | ✅ Terminé (corrigé) | arch-mobile | 08-application-mobile.md | +Flutter, offline, pinning |
| Coordination Multi-Agents | ✅ Terminé | coord-agent | 09-coordination-multi-agents.md | |
| Plan Simulation | ✅ Terminé | sim-engineer | 10-simulation-plan.md | |
| Roadmap 12 semaines | ✅ Terminé (corrigé) | pm | 11-roadmap-12-semaines.md | +redondance orchestrateur |
| Coordination Multi-Agents | ✅ Terminé | coord-agent | 09-coordination-multi-agents.md |
| Plan Simulation | ✅ Terminé | sim-engineer | 10-simulation-plan.md |
| Roadmap 12 semaines | ✅ Terminé | pm | 11-roadmap-12-semaines.md |
| Diagrammes Mermaid | ✅ Terminé | mermaid-diagrams | 12-mermaid-diagram.md |

---

## Progrès

- [ ] Phase 1: Architecture (Tous livrables playbook)
- [ ] Phase 2: Implémentation (non démarré)
- [ ] Phase 3: Simulation (non démarré)
- [ ] Phase 4: Tests & Validation (non démarré)

---

## Métriques

- **Progression**: 100% (11/11 livrables)
- **Budget**: À définir
- **Équipe**: 8 agents spécialisés
- **Timeline**: 12 semaines (roadmap)