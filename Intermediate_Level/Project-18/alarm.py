import time
import datetime
import threading
import os
import winsound


def alarm_sound():
    print("\n🔔 WAKE UP! 🔔")

    base_path = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    sound_path = os.path.join(base_path, "alarm.wav")

    winsound.PlaySound(sound_path, winsound.SND_FILENAME)


def set_alarm(alarm_time):
    print(f"\nAlarm set for {alarm_time}")
    print("Waiting for alarm...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time, end="\r")

        if current_time == alarm_time:
            threading.Thread(target=alarm_sound).start()
            break

        time.sleep(1)


if __name__ == "__main__":
    print("==== Python Alarm Clock ====")
    print("Format: HH:MM:SS (24-hour format)")

    alarm_time = input("Enter alarm time: ")
    set_alarm(alarm_time)
