import psutil
from plyer import notification
import time

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    
    notification.notify(
        title = "Battery Percentage",
        message = str(percent) + "% Battery remaining",
        timeout = 10
    )
    time.sleep(60 * 60)
    