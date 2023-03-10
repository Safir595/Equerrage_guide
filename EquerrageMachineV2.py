# -*- coding: iso-8859-1 -*-
import math
import tkinter as tk

def calculate():
    try:
        diagonal1 = float(diagonal1_entry.get())
        diagonal2 = float(diagonal2_entry.get())
        angle1 = float(angle1_entry.get())
        angle2 = float(angle2_entry.get())
        angle3 = float(angle3_entry.get())
        angle4 = float(angle4_entry.get())
        shortest_diagonal = min(diagonal1, diagonal2)
        longest_diagonal = max(diagonal1, diagonal2)
        difference = abs(longest_diagonal - shortest_diagonal)
        adjustment_distance = difference / 2 * math.sin(math.radians((180 - angle1 - angle2 - angle3 - angle4) / 2))
        if diagonal1 > diagonal2:
            adjustment_direction = "reculer"
        else:
            adjustment_direction = "avancer"
        result_label.config(text=f"Pour obtenir un panneau parfaitement d'équerre, veuillez {adjustment_direction} votre guide de {adjustment_distance:.2f} mm.")
    except ValueError:
        result_label.config(text="Veuillez entrer des valeurs numériques.")

window = tk.Tk()
window.title("Ajustement du guide d'équerre d'une scie à format")
window.geometry("400x350")

diagonal1_label = tk.Label(window, text="Entrez la mesure de la première diagonale en mm :")
diagonal1_label.pack()
diagonal1_entry = tk.Entry(window)
diagonal1_entry.pack()

diagonal2_label = tk.Label(window, text="Entrez la mesure de la deuxième diagonale en mm :")
diagonal2_label.pack()
diagonal2_entry = tk.Entry(window)
diagonal2_entry.pack()

angle1_label = tk.Label(window, text="Entrez la mesure de l'angle 1 en degrés :")
angle1_label.pack()
angle1_entry = tk.Entry(window)
angle1_entry.pack()

angle2_label = tk.Label(window, text="Entrez la mesure de l'angle 2 en degrés :")
angle2_label.pack()
angle2_entry = tk.Entry(window)
angle2_entry.pack()

angle3_label = tk.Label(window, text="Entrez la mesure de l'angle 3 en degrés :")
angle3_label.pack()
angle3_entry = tk.Entry(window)
angle3_entry.pack()

angle4_label = tk.Label(window, text="Entrez la mesure de l'angle 4 en degrés :")
angle4_label.pack()
angle4_entry = tk.Entry(window)
angle4_entry.pack()

calculate_button = tk.Button(window, text="Calculer", command=calculate)
calculate_button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()

