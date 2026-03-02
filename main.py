#water reminder

import time
from plyer import notification

# The "Workhorse" function
def drink_water_notification():
    notification.notify(
        title = "🥤 Time to Hydrate!",
        message = "Drinking water keeps your brain sharp and your body healthy. Take a glass now!",
        app_name = "Water Reminder",
        # You can add a path to an .ico file here for a custom icon
        timeout = 10 # This is how many seconds the alert stays on screen
    )

if __name__ == "__main__":
    while True:
        drink_water_notification()
        
        # Set the reminder frequency (in seconds)
        # 60 * 60 = 3600 seconds (1 hour)
        time.sleep(3600)