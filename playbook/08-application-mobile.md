# Architecture application mobile

## Story
- En tant que product manager mobile, je veux des user stories pour l’interface client et le suivi en temps réel.
- Critère d’acceptation : écrans, flux, API, notifications et sécurité définis.

## Écrans
- Dashboard mission en cours
- Carte temps réel (camion + drones)
- Historique et rapports
- Alertes et incidents
- Profil et sécurité

## Flux utilisateur
- Auth (2FA) -> sélection zone -> suivi mission -> interactions (assistance, pause)
- Notifications push (arrivée, erreur, succès)

## API consommées
- /api/v1/status
- /api/v1/missions
- /api/v1/telemetry
- /api/v1/alerts

## Sécurité
- JWT + renouvellement
- Chiffrement local des données sensibles

## Paiements
- Stripe / Adyen
- Plans d’abonnement, transactions sécurisées
