# Architecture drones collecteurs

## Story
- En tant qu’ingénieur drone, je veux un plan pour la mécanique, les capteurs et le logiciel afin de livrer une flotte sûre et fiable.
- Critère d’acceptation : concept drone, communication, prise/dépôt et logique de pilotage couvert.

## 1. Mécanique & électronique
- **Type: Octocopter cargo** (plus stable que quad pour docking)
- Masse max: 15kg (avec charge)
- **Charge utile: 1 sac de 50L max (~10kg)**
- Autonomie: **15-20 min avec charge**, 25 min à vide

### Spécifications
| Composant | Modèle | Notes |
|-----------|--------|-------|
| Moteurs | T-Motor P80x2 | 800W chacun |
| ESC | Hobbywing X8 | 4-in-1 |
| Batterie | 8S LiPo 16Ah | 600g, 44.4V |
| LiDAR | Livox Mid-Mini | 40m range |
| Caméra | Oak-D Pro | AI vision |
| GPS | u-blox NEO-M9N | RTK Ready |
| IMU | BMI088 | High precision |

- Gestion thermique: ventilateurs actifs pour vol stationnaire
- Préhension: bras robotique + fixation magnétique
- Dépose: guidage vision (AprilTags sur trémie)
- Communication: 5G + Wi-Fi mesh + LoRa backup

## 2. Logiciel ROS2 Drone
- Nodes: vision_perception, object_detection, path_planner, approach_controller, docking_manager, battery_monitor, failsafe, comm_interface.
- Topics: /target_pose, /drone_pose, /battery_state, /docking_status.
- Actions/services: capture_target, rendezvous_execute, land_on_truck, return_base.
- Fonctions: détection sacs/bacs, planification, synchronisation camion mouvant, optimisation énergie, gestion échec.
