import os
import shutil
import tkinter as tk
from tkinter import filedialog

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Select a directory to organize:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Directory", command=self.select_directory)
        self.select_button.pack(pady=10)

        self.organize_button = tk.Button(root, text="Organize Files", command=self.organize_files)
        self.organize_button.pack(pady=10)

    def select_directory(self):
        self.directory_path = filedialog.askdirectory()
        self.label.config(text=f"Selected Directory: {self.directory_path}")

    def organize_files(self):
        if not hasattr(self, 'directory_path'):
            return

        for filename in os.listdir(self.directory_path):
            if os.path.isfile(os.path.join(self.directory_path, filename)):
                # Get the file extension
                _, file_extension = os.path.splitext(filename)

                # Create a folder if it doesn't exist
                folder_path = os.path.join(self.directory_path, file_extension[1:].lower())
                os.makedirs(folder_path, exist_ok=True)

                # Move the file to the corresponding folder
                old_file_path = os.path.join(self.directory_path, filename)
                new_file_path = os.path.join(folder_path, filename)

                shutil.move(old_file_path, new_file_path)

        self.label.config(text="Files organized successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
