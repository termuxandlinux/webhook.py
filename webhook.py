import requests
import json

def send_webhook(url, message):
    """
    Sendet eine HTTP POST-Anfrage mit requests an die angegebene URL.

    Args:
        url (str): Die URL des Webhooks.
        message (str): Die Nachricht, die an den Webhook gesendet werden soll.

    Returns:
        bool: True, wenn die Anfrage erfolgreich gesendet wurde, ansonsten False.
    """
    try:
        # Überprüfe, ob die URL und die Nachricht gültig sind
        if not url or not message:
            raise ValueError("Ungültige URL oder Nachricht")

        # Konvertiere die Nachricht in ein JSON-Format
        payload = json.dumps({"message": message})

        # Führe die POST-Anfrage mit requests durch
        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=payload)
        
        # Überprüfe den Statuscode der Antwort
        if response.status_code == 200:
            return True
        else:
            print(f"Fehler beim Senden des Webhooks: Statuscode {response.status_code}")
            return False
    except Exception as e:
        # Bei einem Fehler die Ausnahme abfangen und False zurückgeben
        print(f"Fehler beim Senden des Webhooks: {e}")
        return False
