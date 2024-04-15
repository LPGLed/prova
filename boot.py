from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

print("Ciao Marco")

firmware_url = "https://github.com/LPGLed/prova/blob/main/"

ota_updater = OTAUpdater(LPGLed WiFi, !lpgled!, firmware_url, "boot.py")

ota_updater.download_and_install_update_if_available()
