# Architecture drones collecteurs

## Story
- En tant qu’ingénieur drone, je veux un plan pour la mécanique, les capteurs et le logiciel afin de livrer une flotte sûre et fiable.
- Critère d’acceptation : concept drone, communication, prise/dépôt et logique de pilotage couvert.

## 1. Mécanique & électronique
- Type: quad/octocopter cargo.
- Moteurs brushless + ESC 4-in-1.
- Batterie: 8S LiPo 15-20Ah, monitorée.
- Capteurs: caméra AI, lidar léger, GPS RTK, IMU.
- Préhension: bras + fixation magnétique + capteur charge.
- Dépose: guidage vision, interface camion stable.
- Communication: 5G + Wi-Fi mesh + LoRa backup.
- Contraintes: masse max + charge utile + autonomie.

## 2. Logiciel ROS2 Drone
- Nodes: vision_perception, object_detection, path_planner, approach_controller, docking_manager, battery_monitor, failsafe, comm_interface.
- Topics: /target_pose, /drone_pose, /battery_state, /docking_status.
- Actions/services: capture_target, rendezvous_execute, land_on_truck, return_base.
- Fonctions: détection sacs/bacs, planification, synchronisation camion mouvant, optimisation énergie, gestion échec.
