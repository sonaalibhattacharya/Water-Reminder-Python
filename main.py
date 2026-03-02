import time
from plyer import notification
from datetime import datetime

def drink_water_notification():
    # 1. Send the notification
    notification.notify(
        title = "🥤 Time to Hydrate!",
        message = "Take a sip! Your brain needs it.",
        app_name = "Water Reminder",
        timeout = 10 
    )
    
    # 2. Log the time to a file
    with open("log.txt", "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Reminded at: {now}\n")

if __name__ == "__main__":
    while True:
        drink_water_notification()
        # Set to 3600 for 1 hour, or 10 for testing
        time.sleep(3600)