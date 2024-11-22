import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Data Dummy (contoh data resep)
recipes = {
    "Nasi Goreng": {
        "ingredients": "Nasi, Bawang Merah, Bawang Putih, Telur, Kecap, Garam",
        "steps": "1. Tumis bawang merah dan bawang putih.\n2. Masukkan telur dan orak-arik.\n3. Tambahkan nasi dan kecap.\n4. Aduk hingga rata."
    },
    "Mie Goreng": {
        "ingredients": "Mie Instan, Telur, Bawang, Sayur",
        "steps": "1. Rebus mie instan.\n2. Tumis bawang dan telur.\n3. Masukkan mie dan bumbu.\n4. Tambahkan sayur dan aduk rata."
    }
}

# Fungsi untuk menampilkan resep
def show_recipe():
    selected_recipe = recipe_listbox.get(tk.ACTIVE)
    if selected_recipe in recipes:
        recipe = recipes[selected_recipe]
        ingredients_text.set(f"Bahan-bahan:\n{recipe['ingredients']}")
        steps_text.set(f"Cara Memasak:\n{recipe['steps']}")
    else:
        messagebox.showerror("Error", "Resep tidak ditemukan!")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Resep Masakan")
root.geometry("500x500")

# Bagian atas: Judul
title_label = tk.Label(root, text="Resep Masakan Sederhana", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Bagian kiri: Daftar Resep
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=10)

recipe_listbox = tk.Listbox(frame, height=10, width=20, font=("Arial", 12))
recipe_listbox.pack()

for recipe_name in recipes.keys():
    recipe_listbox.insert(tk.END, recipe_name)

# Tombol untuk menampilkan resep
view_button = tk.Button(frame, text="Lihat Resep", command=show_recipe, font=("Arial", 12))
view_button.pack(pady=10)

# Bagian kanan: Detail Resep
details_frame = tk.Frame(root)
details_frame.pack(side=tk.RIGHT, padx=10)

ingredients_text = tk.StringVar()
ingredients_label = tk.Label(details_frame, textvariable=ingredients_text, font=("Arial", 12), justify="left")
ingredients_label.pack(anchor="w")

steps_text = tk.StringVar()
steps_label = tk.Label(details_frame, textvariable=steps_text, font=("Arial", 12), justify="left")
steps_label.pack(anchor="w")

# Menjalankan aplikasi
root.mainloop()
