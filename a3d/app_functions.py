import datetime


class AppFunctions:
    def __init__(self):
        pass

    # Maak een unieke ID voor de chat    
    def maakUniekeId(self, client_id):
        # Haal de huidige datum en tijd op
        now = datetime.datetime.now()
        # Formatteer de datum en tijd zoals gewenst
        formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")
        # Combineer user_id met de geformatteerde datum en tijd
        unieke_id = f"{formatted_time}-{client_id}"
        return unieke_id
    
