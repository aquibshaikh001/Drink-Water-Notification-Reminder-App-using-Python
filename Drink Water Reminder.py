import time
from plyer import notification
if __name__ == '__main__':
  while True:
    notification.notify(
        title="Its time to Drink Water",
        message="Facts : About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon="C:/Users/Flywings/Downloads/water.ico",
        timeout=20 #this show the notification till 20 seconds
    )
    time.sleep(15) #this will show the notification after every 15 second
    #to make this program run in background you can type pythonw .\main.py in terminal or you add this script in taskscheduler in windows