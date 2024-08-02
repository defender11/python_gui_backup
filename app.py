import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import json


def get_file_list_from_server(server_address, remote_path, output_file="file_list.txt"):
    try:
        command = ["rsync", "-av", "--list-only", f"{server_address}:{remote_path}"]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        with open(output_file, "w") as file:
            file.write(result.stdout)

        print(f"Список файлов успешно обновлен и сохранен в {output_file}")
        messagebox.showinfo("Успех", "Список файлов успешно обновлен.")
        load_address_list(output_file)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Ошибка при выполнении rsync: {e}")


def load_address_list(file_path):
    address_listbox.delete(0, tk.END)
    with open(file_path, "r") as file:
        for line in file:
            address_listbox.insert(tk.END, line.strip())


def download_backups():
    selected_addresses = address_listbox.curselection()
    if selected_addresses:
        for index in selected_addresses:
            address = address_listbox.get(index)
            print(f"Скачиваю бэкап для: {address}")
    else:
        messagebox.showwarning("Внимание", "Выберите хотя бы один адрес.")

 # Функции для работы с JSON
def load_settings(filename="settings.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_settings_to_file(settings, filename="settings.json"):
    with open(filename, 'w') as file:
        json.dump(settings, file, indent=4)

# Функции для управления настройками
def open_settings():
    global file_config_name
    settings = load_settings(file_config_name)


    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    settings_window.geometry("300x200")

    tk.Label(settings_window, text="Адрес сервера:").pack(pady=5)
    server_entry = tk.Entry(settings_window)
    server_entry.pack(pady=5)
    server_entry.insert(0, settings.get('server_address', ''))

    tk.Label(settings_window, text="Удаленный путь:").pack(pady=5)
    path_entry = tk.Entry(settings_window)
    path_entry.pack(pady=5)
    path_entry.insert(0, settings.get('remote_path', ''))

    tk.Button(settings_window, text="Сохранить",
              command=lambda: save_settings(server_entry.get(), path_entry.get(), settings_window)).pack(pady=10)

def save_settings(server, path, window):
    settings = {
        "server_address": server,
        "remote_path": path
    }
    save_settings_to_file(settings)
    messagebox.showinfo("Настройки", "Настройки сохранены.")
    window.destroy()


def update_file_list():
    if server_address and remote_path:
        get_file_list_from_server(server_address, remote_path)
    else:
        messagebox.showwarning("Ошибка", "Сначала настройте адрес сервера и путь.")


root = tk.Tk()
root.title("Программа для скачивания бэкапов")
root.geometry("400x400")

tk.Label(root, text="Список файлов:").pack(pady=10)

address_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
address_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

download_button = tk.Button(root, text="Скачать бэкапы", command=download_backups)
download_button.pack(pady=10)

update_button = tk.Button(root, text="Обновить список файлов", command=update_file_list)
update_button.pack(pady=10)

settings_button = tk.Button(root, text="Настройки", command=open_settings)
settings_button.pack(pady=10)

server_address = ""
remote_path = ""
file_config_name = 'config.json'

root.mainloop()
