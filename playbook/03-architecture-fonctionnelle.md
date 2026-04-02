# Architecture fonctionnelle

## Story
- En tant que Product Owner, je veux des user stories des activités principales pour prioriser les développements fonctionnels.
- Critère d’acceptation : cas d’usage, flux, interactions, séquences, et conditions de succès sont décrits.

## Cas d’usage
1. Lancement mission
2. Ramassage déchets
3. Rendez-vous dynamique
4. Retour et recharge drone
5. Supervision mobile

## Flux opérationnels
- Backend planifie et assigne mission
- Drone détecte et collecte objets
- Camion reçoit timestamp + position projetée
- Rendez-vous dynamique et dépôt
- Retour de drone et reporting

## Acteurs et interactions
- Drone ↔ Orchestrateur (planning/état)
- Camion ↔ Orchestrateur (position projetée)
- Mobile ↔ Backend (statuts/incidents)

## Séquences temporelles
- T0 mission confirmée
- T+15s drone en route
- T+N rendez-vous camion
- T+N+5s dépôt
- T+N+10s confirmation

## Préconditions
- GPS valide, batterie suffisante, autorisations

## Postconditions
- Déchet collecté, mission mise à jour, drone retour

## Plan d’action séquentiel (Playbook 03)
1. Traduire chaque cas d’usage en user stories avec critères Acceptance (Given/When/Then).
2. Implémenter les flux opérationnels par composant (Orchestrateur, Camion, Drone, Backend, Mobile).
3. Définir scénarios de tests e2e et fuzz pour les points de rendez-vous dynamique.
4. Prioriser backlog pour MVP avec versionnage (v0.1->v1.0).
5. Exécution des tests et retour en rétroaction sur la roadmap.
