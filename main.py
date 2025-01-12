import rumps
import os
import shutil
import webbrowser

from pynput import keyboard

class MenuApp(rumps.App):
    def __init__(self):
        super(MenuApp, self).__init__("🦠")

        self.menu = [
            "Commands",
            None
        ]
        
        print(os.getcwd())

    @rumps.clicked("Commands")
    def open_commands(self, _):
        window = rumps.Window(
            default_text="",
            title="Enter A Command:",
            ok="Run",
            cancel="Cancel",
            dimensions=(225, 20)
        )
        response = window.run()

        if response.clicked == 1:
            command = response.text
            if "-o " in command:
                c = command.replace("-o ", "")
                os.system(f"""osascript -e 'tell app "{c}" to activate'""")
            if "-c " in command:
                c = command.replace("-c ", "")
                os.system(f"""osascript -e 'tell app "{c}" to quit'""")
            if "-n " in command:
                c = command.replace("-n ", "")
                c2 = c.split()
                if len(c2) == 2:
                    if c2[0] != "" and c2[1] != "":
                        newpath = f'/Users/lawsonhiggins/{c2[0]}/{c2[1]}'
                        if not os.path.exists(newpath):
                            os.mkdir(newpath)
            if "-s " in command:
                c = command.replace("-s ", "")
                if ".com" in c or ".net" in c or ".io" in c or ".gov" in c or ".org" in c:
                    webbrowser.open(f'https://www.{c}')
                elif ".com" not in c or ".net" not in c or ".io" not in c or ".gov" not in c or ".org" not in c:
                    webbrowser.open(f'http://www.google.com/search?q={c}')
            if "-d " in command:
                c = command.replace("-d ", "")
                os.system("open "+f'/Users/lawsonhiggins/{c}')
            if "-v " in command:
                c = command.replace("-v ", "")
                c2 = int(c)
                os.system(f"""osascript -e 'set volume output volume {c2}'""")

            if command == "--rst":
                os.system(f""" osascript -e 'tell app "System Events" to restart' """)
            if command == "--std":
                os.system(f""" osascript -e 'tell app "System Events" to shut down' """)
            if command == "--emt":
                os.system(f""" osascript -e 'tell application "Finder" to empty trash' """)
            if command == "--org":
                directory = os.path.join(os.path.expanduser("~"), "Downloads")
                extensions = {
                    ".jpg": "Images",
                    ".jpeg": "Images",
                    ".png": "Images",
                    ".gif": "Images",
                    ".webp": "Images",
                    ".mp4": "Videos",
                    ".mp3": "Music",
                    ".fbx": "Models",
                    ".obj": "Models",
                    ".wav": "Music",
                    ".pdf": "Documents",
                    ".txt": "Documents",
                    ".doc": "Documents",
                    ".zip": "Folders",
                }

                for filename in os.listdir(directory):
                    file_path = os.path.join(directory, filename)

                    if os.path.isfile(file_path):
                        extension = os.path.splitext(filename)[1].lower()

                        if extension in extensions:
                            folder_name = extensions[extension]

                            folder_path = os.path.join(directory, folder_name)
                            os.makedirs(folder_path, exist_ok=True)

                            destination_path = os.path.join(folder_path, filename)
                            shutil.move(file_path, destination_path)
                        else:
                            folder_name = "Other"

                            folder_path = os.path.join(directory, folder_name)
                            os.makedirs(folder_path, exist_ok=True)

                            destination_path = os.path.join(folder_path, filename)
                            shutil.move(file_path, destination_path)
            
            if command == "help":
                rumps.alert("Commands\n\n-o *name*: Open App\n-c *name*: Close App: \n-v *number*: Volume\n-s *url*: Search\n-n *dir* *name*: New Folder\n-d *dir*: Open Directory\n\n--rst: Restart\n--std: Shutdown\n--emt: Empty Trash\n--org: Organize")
    
if __name__ == "__main__":
    MenuApp().run()