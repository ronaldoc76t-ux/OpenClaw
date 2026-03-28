#!/usr/bin/env python3
"""Surveillance boîte email pour factures et paiements"""
import imaplib
import os
import json
from datetime import datetime

CREDS_FILE = os.path.expanduser("~/.openclaw/workspace/.email-creds")
STATE_FILE = os.path.expanduser("~/.openclaw/workspace/scripts/.email-state.json")
KEYWORDS = ["facture", "paiement", "invoice", "payment", "recu", "avis", "montant", "solde"]

def load_creds():
    with open(CREDS_FILE) as f:
        lines = f.read().strip().split("\n")
        return lines[0], lines[1]

def check_emails():
    email_addr, password = load_creds()
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_addr, password)
    mail.select('INBOX')
    
    # Load last seen
    state = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            state = json.load(f)
    
    new_emails = []
    status, messages = mail.search(None, 'ALL')
    message_ids = messages[0].split()
    
    for msg_id in message_ids:
        msg_id_str = msg_id.decode()
        if msg_id_str in state.get("seen", []):
            continue
        
        # Check this email
        typ, data = mail.fetch(msg_id, '(BODY.PEEK[HEADER])')
        header = data[0][1].decode('utf-8', errors='ignore')
        
        # Check subject for keywords
        for line in header.split('\n'):
            if line.startswith('Subject:'):
                subject = line[9:].strip().lower()
                if any(kw in subject for kw in KEYWORDS):
                    # Get sender too
                    for l in header.split('\n'):
                        if l.startswith('From:'):
                            new_emails.append({
                                "id": msg_id_str,
                                "from": l[6:].strip(),
                                "subject": line[9:].strip()
                            })
                            break
    
    # Update state
    state["seen"] = [msg_id.decode() for msg_id in message_ids]
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)
    
    mail.logout()
    return new_emails

if __name__ == "__main__":
    results = check_emails()
    if results:
        print(f"FOUND: {len(results)} new email(s)")
        for e in results:
            print(f"  - {e['from']}: {e['subject']}")
    else:
        print("No new invoice/payment emails")