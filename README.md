# webhook.py

Webhook.py is an easy Python Service, with this can you easy use webhook in your Python Script

## Instruction

Import:
```python
import webhook
```
Easy Script (Definations in the Script)

```python
from webhook import send_webhook

def main():
    # Definiere die URL des Webhooks und die Nachricht
    webhook_url = "https://example.com/webhook"
    message = "Hallo von meinem Python-Skript!"

    # Sende die Nachricht über den Webhook
    success = send_webhook(webhook_url, message)

    if success:
        print("Die Nachricht wurde erfolgreich über den Webhook gesendet.")
    else:
        print("Beim Senden der Nachricht über den Webhook ist ein Fehler aufgetreten.")

if __name__ == "__main__":
    main()
```

Terminal Instruction

```python
from webhook import send_webhook

def main():
    # Frage den Benutzer nach der URL des Webhooks
    webhook_url = input("Bitte geben Sie die URL des Webhooks ein: ")

    # Frage den Benutzer nach der Nachricht
    message = input("Bitte geben Sie die Nachricht ein, die Sie senden möchten: ")

    # Sende die Nachricht über den Webhook
    success = send_webhook(webhook_url, message)

    if success:
        print("Die Nachricht wurde erfolgreich über den Webhook gesendet.")
    else:
        print("Beim Senden der Nachricht über den Webhook ist ein Fehler aufgetreten.")

if __name__ == "__main__":
    main()
```

### Install

Download the tar.gz from the Artefact and Install this with pip

### pip

Comming soon

#### LICENSE

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
