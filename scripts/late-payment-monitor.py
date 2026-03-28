#!/usr/bin/env python3
"""Surveillance boîte email - Détection retards de paiement hybride + Auto-réponse + Alerte"""
import imaplib
import os
import json
import smtplib
import re
from email.mime.text import MIMEText
from email import message_from_bytes
from datetime import datetime

CREDS_FILE = os.path.expanduser("~/.openclaw/workspace/.email-creds")
STATE_FILE = os.path.expanduser("~/.openclaw/workspace/scripts/.late-payment-state.json")
NOTIF_FILE = os.path.expanduser("~/.openclaw/workspace/data/late-payment-alerts.json")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Mots-clés et patterns pour détecter un retard de paiement
KEYWORDS = [
    "late payment", "payment late", "unpaid", "impaye", "impayé",
    "retard de paiement", "paiement en retard", "delayed payment",
    "where is my payment", "where is the payment", "not received payment",
    "invoice unpaid", "facture impayée", "non payé", "pas payé",
    "you owe", "you owe me", "owe money", "money owed",
    "pay me", "pay now", "pay immediately", "pay as soon as possible",
    "ou sont", "ou est", "mon paiement", "ma paiement", "francs"
]

def load_creds():
    with open(CREDS_FILE) as f:
        lines = f.read().strip().split("\n")
        return lines[0], lines[1]

def detect_late_payment(subject, body):
    """Détection hybride de retard de paiement"""
    text = (subject + " " + body).lower()
    
    # Check keywords
    for kw in KEYWORDS:
        if kw in text:
            return True, kw
    
    # Check for amount patterns with payment context
    amount_pattern = r'\$?\d+[\.,]?\d*\s*(\$|dollars?|USD|EUR|€|pounds?|francs?|CHF)'
    if re.search(amount_pattern, text):
        payment_context = ["pay", "invoice", "bill", "due", "owe", "money", "payment"]
        if any(ctx in text for ctx in payment_context):
            return True, "amount + payment context"
    
    return False, None

def send_auto_reply(to_email, subject):
    """Envoyer une réponse automatique"""
    email_addr, password = load_creds()
    
    msg = MIMEText("""Bonjour,

Nous avons bien reçu votre message concernant le retard de paiement.

Nous vous informons que nous allons renvoyer l'argent rapidement dans les plus brefs délais.

Nous vous prions de bien vouloir accepter nos excuses pour ce désagrément.

Cordialement,
L'équipe""", 'plain', 'utf-8')
    
    msg['Subject'] = f"Re: {subject}"
    msg['From'] = email_addr
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(email_addr, password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Erreur envoi: {e}")
        return False

def check_and_reply():
    email_addr, password = load_creds()
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_addr, password)
    mail.select('INBOX')
    
    state = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            state = json.load(f)
    
    seen = state.get("seen", [])
    replies_sent = []
    
    status, messages = mail.search(None, 'ALL')
    if not messages[0]:
        mail.logout()
        return []
    
    message_ids = messages[0].split()
    
    for msg_id in message_ids:
        msg_id_str = msg_id.decode()
        if msg_id_str in seen:
            continue
        
        # Get full email
        typ, data = mail.fetch(msg_id, '(BODY.PEEK[])')
        if not data or not data[0]:
            continue
        
        msg = message_from_bytes(data[0][1])
        
        subject = msg.get('subject', '')
        
        # Get body
        body = ''
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
        else:
            body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        
        # Get sender
        sender = msg.get('from', '')
        email_match = re.search(r'<(.+?)>', sender)
        sender_email = email_match.group(1) if email_match else sender.strip()
        
        print(f"Analyse: {subject[:50]}...")
        
        # Detect late payment
        is_late, matched = detect_late_payment(subject, body[:2000])
        
        if is_late:
            print(f"✓ RETARD DÉTECTÉ (mot-clé: {matched}): {sender} - {subject}")
            
            # Send auto-reply
            success = send_auto_reply(sender_email, subject)
            
            if success:
                replies_sent.append({
                    "id": msg_id_str,
                    "timestamp": datetime.now().isoformat(),
                    "from": sender,
                    "subject": subject,
                    "keyword": matched,
                    "replied": True
                })
                print(f"✓ Réponse envoyée à {sender_email}")
            else:
                print(f"✗ Échec envoi à {sender_email}")
        else:
            print(f"  → Pas un retard de paiement")
        
        seen.append(msg_id_str)
    
    state["seen"] = seen
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)
    
    mail.logout()
    return replies_sent

def save_notifications(results):
    alerts = []
    if os.path.exists(NOTIF_FILE):
        with open(NOTIF_FILE) as f:
            alerts = json.load(f)
    
    alerts.extend(results)
    
    with open(NOTIF_FILE, 'w') as f:
        json.dump(alerts, f)

if __name__ == "__main__":
    results = check_and_reply()
    if results:
        print(f"✓ {len(results)} réponse(s) envoyée(s)")
        for r in results:
            print(f"  - {r['from']}: {r['subject']}")
        save_notifications(results)
    else:
        print("Aucun nouveau message sur retard de paiement")