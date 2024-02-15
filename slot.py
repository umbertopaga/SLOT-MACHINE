import tkinter as tk
from tkinter import messagebox
import random


class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine")
        self.master.geometry("500x400")

        # Saldo iniziale
        self.saldo = 0
        self.puntata = 0

        # Simboli della slot machine
        self.symbols = ['7', '🍒', '🍋', '🍊', '🍉']

        # Impostazioni grafiche
        self.slot_height = 100
        self.slot_width = 150

        # Creazione dei widget
        self.create_widgets()

    def create_widgets(self):
        # Etichetta e campo di inserimento per il saldo iniziale
        saldo_label = tk.Label(self.master, text="Saldo iniziale:", font=('Arial', 12))
        saldo_label.grid(row=0, column=0)

        self.saldo_entry = tk.Entry(self.master)
        self.saldo_entry.grid(row=0, column=1)

        # Pulsante per confermare il saldo iniziale e iniziare il gioco
        start_button = tk.Button(self.master, text="Inizia", command=self.start_game)
        start_button.grid(row=0, column=2)

        # Etichetta e campo di inserimento per la puntata
        puntata_label = tk.Label(self.master, text="Puntata:", font=('Arial', 12))
        puntata_label.grid(row=1, column=0)

        self.puntata_entry = tk.Entry(self.master)
        self.puntata_entry.grid(row=1, column=1)

        # Pulsante per effettuare una puntata
        spin_button = tk.Button(self.master, text="Spin", command=self.spin)
        spin_button.grid(row=1, column=2)

        # Creazione della slot machine grafica
        self.slot_canvases = []
        for i in range(3):
            slot_canvas = tk.Canvas(self.master, width=self.slot_width, height=self.slot_height, bg='white')
            slot_canvas.grid(row=2, column=i, padx=10, pady=10)
            self.slot_canvases.append(slot_canvas)

    def start_game(self):
        # Ottenere il saldo iniziale inserito dall'utente
        saldo_iniziale = self.saldo_entry.get()
        if not saldo_iniziale.isdigit():
            messagebox.showerror("Errore", "Inserire un saldo iniziale valido!")
            return

        self.saldo = int(saldo_iniziale)
        self.update_saldo()

    def spin(self):
        # Ottenere la puntata inserita dall'utente
        puntata_inserita = self.puntata_entry.get()
        if not puntata_inserita.isdigit():
            messagebox.showerror("Errore", "Inserire una puntata valida!")
            return

        # Convertire la puntata in un numero intero
        self.puntata = int(puntata_inserita)

        # Controllo se il saldo è sufficiente per effettuare la puntata
        if self.puntata > self.saldo:
            messagebox.showerror("Errore", "Non hai abbastanza saldo!")
            return

        # Aggiornare il saldo dopo aver effettuato la puntata
        self.saldo -= self.puntata
        self.update_saldo()

        # Eseguire lo spinning della slot machine
        result = [random.choice(self.symbols) for _ in range(3)]
        self.show_result(result)

    def show_result(self, result):
        # Mostrare il risultato dello spin nella slot machine grafica
        for i, symbol in enumerate(result):
            x = self.slot_width // 2
            y = (i + 1) * (self.slot_height // 4)
            self.slot_canvases[i].delete("symbol")
            self.slot_canvases[i].create_text(x, y, text=symbol, font=('Arial', 50), tags="symbol")

    def update_saldo(self):
        # Aggiornare l'etichetta del saldo
        self.saldo_entry.delete(0, tk.END)
        self.saldo_entry.insert(0, str(self.saldo))


def main():
    root = tk.Tk()
    app = SlotMachine(root)
    root.mainloop()


if __name__ == "__main__":
    main()
