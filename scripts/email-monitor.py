#!/usr/bin/env python3
"""Surveillance boîte email - Alerte + Impression PDF + Registre CSV"""
import imaplib
import os
import json
import csv
from datetime import datetime

CREDS_FILE = os.path.expanduser("~/.openclaw/workspace/.email-creds")
STATE_FILE = os.path.expanduser("~/.openclaw/workspace/scripts/.email-state.json")
REGISTRY_FILE = os.path.expanduser("~/.openclaw/workspace/data/email-registry.csv")
KEYWORDS = ["facture", "paiement", "invoice", "payment", "recu", "avis", "montant", "solde"]
OUTPUT_DIR = "/mnt/c/Users/OpenClaw/Documents/Factures"

# Ensure data directory exists
os.makedirs(os.path.dirname(REGISTRY_FILE), exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_creds():
    with open(CREDS_FILE) as f:
        lines = f.read().strip().split("\n")
        return lines[0], lines[1]

def init_registry():
    """Initialize CSV registry with headers if it doesn't exist"""
    if not os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'id', 'timestamp', 'folder', 'from', 'subject', 
                'keyword_found', 'file_path', 'printed', 'date_printed'
            ])

def add_to_registry(entry):
    """Add entry to CSV registry"""
    with open(REGISTRY_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            entry['id'],
            entry['timestamp'],
            entry['folder'],
            entry['from'],
            entry['subject'],
            entry['keyword_found'],
            entry['file_path'],
            entry.get('printed', 'false'),
            entry.get('date_printed', '')
        ])

def print_to_pdf(filepath):
    """Print text file to PDF using Windows PowerShell"""
    ps_script = f'''
$file = "{filepath}"
$printer = "Microsoft Print to PDF"
$raw = Get-Content -Path $file -Raw -Encoding UTF8
$shell = New-Object -ComObject Shell.Application
$folder = $shell.Namespace((Split-Path $file))
$item = $folder.ParseName((Split-Path $file -Leaf))
$verb = $item.Verbs() | Where-Object {{$_.Name -eq "Print"}}
if ($verb) {{
    $item.InvokeVerb($verb)
    Write-Output "Printed"
}} else {{
    # Alternative: use notepad to print
    Start-Process notepad.exe -ArgumentList $file -Wait
    Start-Sleep -Seconds 1
    $npp = Get-Process notepad -ErrorAction SilentlyContinue
    if ($npp) {{
        # Send Ctrl+P then Enter to print
        [System.Windows.Forms.SendKeys]::SendWait("^p~")
        Start-Sleep -Seconds 2
        $npp.CloseMainWindow()
    }}
}}
'''
    try:
        # Simpler approach: open with default app which should handle printing
        result = os.system(f'/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -c "Start-Process \\"{filepath}\\" -Verb PrintTo \\"Microsoft Print to PDF\\""')
        return result == 0
    except Exception as e:
        print(f"Print error: {e}")
        return False

def check_and_print():
    email_addr, password = load_creds()
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_addr, password)
    
    folders = ['INBOX', '[Gmail]/All Mail']
    
    state = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            state = json.load(f)
    
    seen = state.get("seen", [])
    new_invoices = []
    
    init_registry()
    
    for folder in folders:
        try:
            mail.select(folder)
        except:
            continue
            
        status, messages = mail.search(None, 'ALL')
        if not messages[0]:
            continue
        message_ids = messages[0].split()
        
        for msg_id in message_ids:
            msg_id_str = f"{folder}:{msg_id.decode()}"
            if msg_id_str in seen:
                continue
            
            # Get headers
            typ, header_data = mail.fetch(msg_id, '(BODY.PEEK[HEADER])')
            if not header_data or not header_data[0]:
                continue
            header = header_data[0][1].decode('utf-8', errors='ignore')
            
            subject = ""
            sender = ""
            for line in header.split('\n'):
                if line.startswith('Subject:'):
                    subject = line[9:].strip()
                if line.startswith('From:'):
                    sender = line[6:].strip()
            
            subject_lower = subject.lower()
            keyword_found = None
            for kw in KEYWORDS:
                if kw in subject_lower:
                    keyword_found = kw
                    break
            
            if keyword_found:
                # Get full email
                typ, data = mail.fetch(msg_id, '(BODY.PEEK[])')
                if data and data[0]:
                    raw_email = data[0][1]
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    safe_subject = "".join(c for c in subject if c.isalnum())[:30]
                    txt_filename = f"{OUTPUT_DIR}/{timestamp}_{safe_subject}.txt"
                    pdf_filename = f"{OUTPUT_DIR}/{timestamp}_{safe_subject}.pdf"
                    
                    # Save text file
                    with open(txt_filename, 'w', encoding='utf-8') as f:
                        f.write(f"From: {sender}\n")
                        f.write(f"Subject: {subject}\n")
                        f.write(f"Date: {datetime.now()}\n")
                        f.write(f"Folder: {folder}\n")
                        f.write(f"Keyword: {keyword_found}\n")
                        f.write("-" * 50 + "\n\n")
                        f.write(raw_email.decode('utf-8', errors='ignore'))
                    
                    # Try to print to PDF
                    printed = print_to_pdf(txt_filename)
                    
                    entry = {
                        'id': msg_id_str,
                        'timestamp': datetime.now().isoformat(),
                        'folder': folder,
                        'from': sender,
                        'subject': subject,
                        'keyword_found': keyword_found,
                        'file_path': txt_filename,
                        'printed': 'true' if printed else 'false',
                        'date_printed': datetime.now().isoformat() if printed else ''
                    }
                    add_to_registry(entry)
                    
                    new_invoices.append(entry)
                    status_msg = "IMPRESSO & PDF" if printed else "SAVED (PDF failed)"
                    print(f"{status_msg}: {sender} - {subject}")
            
            seen.append(msg_id_str)
    
    state["seen"] = seen
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)
    
    mail.logout()
    return new_invoices

if __name__ == "__main__":
    results = check_and_print()
    if results:
        print(f"✓ {len(results)} email(s) détecté(s) et traité(s)")
    else:
        print("Aucun nouveau email sur factures/paiements")
    
    # Show registry
    if os.path.exists(REGISTRY_FILE):
        print(f"\nRegistre: {REGISTRY_FILE}")