# **RdvChecker**

RDV-Checker est un script Python conçu pour surveiller la disponibilité des créneaux de rendez-vous sur le site de la préfecture. Le script vérifie régulièrement la page de réservation et envoie une alerte par e-mail dès qu'un créneau devient disponible.


**Fonctionnalités**

Surveillance automatique : Le script vérifie régulièrement la disponibilité des créneaux sur la page web.
Alertes par e-mail : Une notification par e-mail est envoyée dès qu'un créneau devient disponible.
Résilience : Le script est conçu pour être résilient aux changements de structure HTML de la page, en cherchant spécifiquement le texte indiquant la disponibilité.

**Prérequis**

Python 3.x
Bibliothèques Python :
- requests
- beautifulsoup4
- smtplib

Vous pouvez installer les bibliothèques nécessaires avec la commande suivante :

```bash
pip install requests beautifulsoup4
```

**Utilisation**

1. Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/mZasir/RdvChecker
```

2. Modifiez les paramètres de l'e-mail dans le script main.py pour y insérer vos propres informations d'authentification SMTP et les adresses e-mail :

```python
def send_email():
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login("votre_email@example.com", "votre_mot_de_passe")
    
    msg = "Un créneau est disponible !"
    
    server.sendmail("my_email@example.com", "dest_email@example.com", msg)
    server.quit()
```

3. Exécutez le script pour commencer la surveillance :
```bash
python main.py
```

**Remarques**

- Assurez-vous que votre fournisseur de service e-mail permet les connexions SMTP et que vous avez configuré les permissions nécessaires.
- Adaptez l'URL dans le script si l'adresse de la page de réservation de la préfecture change.
- **Note** : Il se peut que le script rencontre des erreurs dues à la présence de captchas sur le site de la préfecture. Cette limitation sera corrigé dans une version ultérieure du script.





