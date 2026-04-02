# Architecture camion autonome

## Story
- En tant qu’ingénieur véhicule autonome, je veux un plan détaillé du camion pour guider conception matérielle et logiciels embarqués.
- Critère d’acceptation : architecture mécanique, capteurs, actuateurs, trémie et controle ROS2 documentés.

## 1. Mécanique & électronique
- Châssis renforcé avec plateforme de dépôt et stabilisation.
- **Vitesse cible: 30-50 km/h** (mode urbain)

### Capteurs (avec redondance)
| Capteur | Primary | Backup | Role |
|---------|---------|--------|------|
| LiDAR | Velodyne VLP-16 | Livox Mid-360 | Percepción 360° |
| Caméra | Stereolabs ZED 2 | Realsense D455 | Vision AI |
| Radar | Continental ARS408 | - | Détection longue portée |
| GPS | u-blox ZED-F9P RTK | - | Position cm-level |
| IMU | XSens MTi-680G | - | Orientation/-heading |

- Actuateurs: direction assistée + EPS, freinage électronique, propulsion hybride ou électrique.
- Trémie: zone réception amortie, capteurs niveau, compacteur hydraulique, sécurités anti-retournement.
- Alimentation: LiFePO4 (100kWh), alternateur, UPS, gestion BMS.
- Sécurité: barrières, E-stop, prototypes anti-obstacle.

## 2. Logiciel ROS2 Camion
- Nodes principaux: odometry, perception, localisation, controller, rendezvous, trajectory_predictor, tranche_manager, backend_interface.
- Topics: /pose, /cmd_vel, /rendezvous_request, /rendezvous_status, /payload_state, /obstacle_alert.
- Services/actions: start_mission, cancel_mission, dump_payload, calibrate_sensor.
- Fonctionnalités: navigation en mouvement continue, prédiction 30-120s, gestion rendez-vous drones, régulation trémie.
- Gestion risques: e-stop, dérive, perte communication, recalage.
