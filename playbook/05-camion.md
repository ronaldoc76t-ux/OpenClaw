# Architecture camion autonome

## Story
- En tant qu’ingénieur véhicule autonome, je veux un plan détaillé du camion pour guider conception matérielle et logiciels embarqués.
- Critère d’acceptation : architecture mécanique, capteurs, actuateurs, trémie et controle ROS2 documentés.

## 1. Mécanique & électronique
- Châssis renforcé avec plateforme de dépôt et stabilisation.
- Capteurs: lidar 360°, caméras stéréo, radar long portee, GPS RTK, IMU.
- Actuateurs: direction assistée + EPS, freinage électronique, propulsion hybride ou électrique.
- Trémie: zone réception amortie, capteurs niveau, compacteur hydraulique, sécurités anti-retournement.
- Alimentation: LiFePO4, alternateur, UPS, gestion BMS.
- Sécurité: barrières, E-stop, prototypes anti-obstacle.

## 2. Logiciel ROS2 Camion
- Nodes principaux: odometry, perception, localisation, controller, rendezvous, trajectory_predictor, tranche_manager, backend_interface.
- Topics: /pose, /cmd_vel, /rendezvous_request, /rendezvous_status, /payload_state, /obstacle_alert.
- Services/actions: start_mission, cancel_mission, dump_payload, calibrate_sensor.
- Fonctionnalités: navigation en mouvement continue, prédiction 30-120s, gestion rendez-vous drones, régulation trémie.
- Gestion risques: e-stop, dérive, perte communication, recalage.
