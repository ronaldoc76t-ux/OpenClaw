# Architecture backend cloud

## Story
- En tant qu’architecte backend, je veux un plan de service pour construire l’orchestrateur, API et ingestion télémétrie.
- Critère d’acceptation : architecture microservices, DB, sécurité, scalabilité et logs inclues.

## 1. Composants
- API Gateway + Auth (OAuth2/JWT)
- Microservices: mission, fleet, trajectory, telemetry, coordination, user.
- DB: PostgreSQL (+Timescale), Redis cache.
- Message bus: Kafka.

## 2. Orchestrateur et gestion
- Mission planning: assignation, slot rendez-vous.
- Trajectoire: prédicteur EKF + LSTM.
- Télémétrie: ingestion temps réel, dashboard.
- Gestion pannes: replanification, failover.

## 3. Sécurité & scalabilité
- IAM, WAF, politique RBAC.
- mTLS, chiffrement, rotation clés.
- Kubernetes autoscaling.

## 4. Logs
- Flux: Kafka -> ELK / Grafana, métriques Prometheus.
