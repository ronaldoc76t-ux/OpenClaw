# Architecture application mobile

## Story
- En tant que product manager mobile, je veux des user stories pour l'interface client et le suivi en temps réel.
- Critère d'acceptation : écrans, flux, API, notifications et sécurité définis.

## 1. Écrans

### Écran 1: Dashboard Mission
- Carte avec position truck + drones
- Progress bar mission (collectés/total)
- Boutons: pause, cancel, assistance
- Stats temps réel: durée, distance, batteries

### Écran 2: Carte Interactive
- Mapbox/Google Maps avec clustering
- Couches: truck, drones, zones collecte, historique
- Filtres: status, battery, last update
- Search: par zone, par mission

### Écran 3: Historique
- Liste missions passées
- Stats agrégées: taux succès, kg collectés
- Filtres: date, drone, status

### Écran 4: Alertes & Incidents
- Timeline incidents
- Détails: cause, résolution, photos
- Actions: acknowledge, escalate

### Écran 5: Profil & Sécurité
- Infos compte (email, nom, rôle)
- 2FA setup (TOTP)
- Notifications preferences
- Déconnexion

## 2. Flux Utilisateur

### Auth Flow
```
Login → Email/Password → 2FA (optionnel) → Dashboard
       → OAuth (Google/Apple) → Dashboard
```

### Start Mission Flow
```
1. Sélectionner zone sur carte
2. Confirmer nombre drones
3. Démarrer mission
4. Suivre progression
```

### Incident Flow
```
1. Notification push
2. Tap → détail incident
3. Actions: acknowledge / escalate / resolve
```

## 3. API Consommées

### Auth
- `POST /api/v1/auth/login` - Login email/password
- `POST /api/v1/auth/oauth` - OAuth callback
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/2fa/setup` - Enable 2FA
- `POST /api/v1/auth/2fa/verify` - Verify 2FA

### Missions
- `GET /api/v1/missions` - Liste missions
- `GET /api/v1/missions/:id` - Détail mission
- `POST /api/v1/missions` - Créer mission
- `PUT /api/v1/missions/:id` - Modifier mission
- `DELETE /api/v1/missions/:id` - Annuler mission
- `POST /api/v1/missions/:id/pause` - Pause
- `POST /api/v1/missions/:id/resume` - Reprendre

### Telemetry
- `GET /api/v1/telemetry/live` - WebSocket stream
- `GET /api/v1/telemetry/history` - Historique

### Fleet
- `GET /api/v1/fleet/drones` - Liste drones
- `GET /api/v1/fleet/trucks` - Liste trucks
- `GET /api/v1/fleet/status/:id` - Status individuel

### Alerts
- `GET /api/v1/alerts` - Liste alertes
- `PUT /api/v1/alerts/:id/ack` - Acknowledge
- `PUT /api/v1/alerts/:id/escalate` - Escalate

## 4. Notifications Push

### Providers
- FCM (Firebase Cloud Messaging) pour Android
- APNS (Apple Push Notification Service) pour iOS

### Types Notifications
| Type | Priorité | Contenu |
|------|----------|----------|
| mission_start | HIGH | "Mission #123 démarrée" |
| mission_complete | HIGH | "Mission terminée: 45kg collectés" |
| drone_low_battery | MEDIUM | "Drone #7: 15% batterie" |
| incident | CRITICAL | "Incident: collision détectée" |
| rendezvous_fail | MEDIUM | "RV échoué avec Drone #3" |

## 5. Sécurité

### Auth
- JWT access token (15 min)
- JWT refresh token (7 jours)
- Stockage: Keychain (iOS) / Keystore (Android)
- Biométrie: FaceID / Fingerprint pour unlock

### Réseau
- Certificate pinning
- HTTPS only
- mTLS optionnel pour mode entreprise

### Données locales
- Chiffrement SQLite avec SQLCipher
- Clear cache sur logout
- Pas de données sensibles en clair

## 6. Mode Offline

### Fonctionnement
- Cache last known positions
- Queue actions pour sync
- Indicateur "offline" visible

### Sync Strategy
```
Online: Real-time sync
Offline: Queue actions locally
Reconnect: Batch upload queue + fetch updates
```

## 7. Paiements (Optional)

### Providers
- Stripe (recommandé)
- Adyen

### Features
- Abonnement premium (accès historqiue long terme)
- Facturation entreprise
- Webhooks pour receipts