import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_email():
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login("votre_email@example.com", "votre_mot_de_passe")
    
    msg = "Un créneau est disponible !"
    
    server.sendmail("my_email@example.com", "dest_email@example.com", msg)
    server.quit()

def check_availability():
    url = "https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/4408/creneau/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    h2_elements = soup.find_all('h2')
    
    # Chercher le texte spécifique dans chaque <h2>
    for h2 in h2_elements:
        if "Aucun créneau disponible" in h2.text:
            print("Aucun créneau disponible. Vérification dans 5 minutes")
            # Vérification toutes les 5 minutes
            time.sleep(300)  # Attendre 5 minutes avant de vérifier à nouveau
            check_availability()
            return
    
    # Si aucun <h2> ne contient "Aucun créneau disponible", envoyer un e-mail
    send_email()

check_availability()