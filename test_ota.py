from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://github.com/LPGLed/prova"

ota_updater = OTAUpdater(LPGLed WiFi, !lpgled!, firmware_url, "test_ota.py")

ota_updater.download_and_install_update_if_available()
