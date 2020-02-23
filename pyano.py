from tkinter import *
import time
import pygame
import pathlib
import os


pygame.init()
root = Tk()
root.title("Pyano")
root.geometry("1470x1000")
root.configure(background="brown")

widget = Frame(root, bg="brown", bd=30, relief=FLAT)
widget.grid()

widget1 = Frame(widget, bg="brown", bd=30, relief=FLAT)
widget1.grid()
widget2 = Frame(widget, bg="black", bd=10, relief=RAISED)
widget2.grid()
widget3 = Frame(widget, bg="white", bd=30, relief=RAISED)
widget3.grid()
widget4 = Frame(widget, bg="brown", bd=30, relief=FLAT)
widget4.grid()

affiche_note = StringVar()
affiche_note.set("Note")

# ========================================================== Titre ============================================================#

Label(
    widget1,
    text="PYANO",
    font=("times", 25, "bold"),
    padx=8,
    pady=8,
    bd=4,
    bg="brown",
    fg="white",
    justify=CENTER,
).grid(row=0, column=0, columnspan=11)

# ======================================================= Liste de notes ======================================================#

notes = []

# ==================================================== Stockage des notes =====================================================#

notes_dict = {
    "Do♯": ["z", "notes/dod.wav"],
    "Re♯": ["e", "notes/red.wav"],
    "Fa♯": ["t", "notes/fad.wav"],
    "Sol♯": ["y", "notes/sold.wav"],
    "Si♭": ["u", "notes/sib.wav"],
    "Do#": ["o", "notes/dod1.wav"],
    "Re#": ["p", "notes/red1.wav"],
    "Do": ["q", "notes/do.wav"],
    "Re": ["s", "notes/re.wav"],
    "Mi": ["d", "notes/mi.wav"],
    "Fa": ["f", "notes/fa.wav"],
    "Sol": ["g", "notes/sol.wav"],
    "La": ["h", "notes/la.wav"],
    "Si": ["j", "notes/si.wav"],
    "Do1": ["k", "notes/do1.wav"],
    "Re1": ["l", "notes/re1.wav"],
    "Mi1": ["m", "notes/mi1.wav"],
    "Fa1": ["n", "notes/fa1.wav"],
}

# =================================================== Fonction principale =====================================================#


def ma_note(note):
    affiche_note.set(note)
    sound = pygame.mixer.Sound(notes_dict[note][1])
    sound.play()
    notes.append(note)
    btnVider.config(state=NORMAL)
    btnVider.config(cursor="hand1")
    btnRejouer.config(state=NORMAL)
    btnRejouer.config(cursor="hand1")
    btnEnregistrer.config(state=NORMAL)
    btnEnregistrer.config(cursor="hand1")


# ======================================================= Key binding =========================================================#

# ==== Noires ====#
root.bind("<z>", lambda x: ma_note("Do♯"))
root.bind("<e>", lambda x: ma_note("Re♯"))
root.bind("<t>", lambda x: ma_note("Fa♯"))
root.bind("<y>", lambda x: ma_note("Sol♯"))
root.bind("<u>", lambda x: ma_note("Si♭"))
root.bind("<o>", lambda x: ma_note("Do#"))
root.bind("<p>", lambda x: ma_note("Re#"))

# ==== Blanches ====#
root.bind("<q>", lambda x: ma_note("Do"))
root.bind("<s>", lambda x: ma_note("Re"))
root.bind("<d>", lambda x: ma_note("Mi"))
root.bind("<f>", lambda x: ma_note("Fa"))
root.bind("<g>", lambda x: ma_note("Sol"))
root.bind("<h>", lambda x: ma_note("La"))
root.bind("<j>", lambda x: ma_note("Si"))
root.bind("<k>", lambda x: ma_note("Do1"))
root.bind("<l>", lambda x: ma_note("Re1"))
root.bind("<m>", lambda x: ma_note("Mi1"))
root.bind("<n>", lambda x: ma_note("Fa1"))

# =============================================== Fonction 20 dernières notes =================================================#


def vingt_dernieres_notes():
    nbNoteAJouer = 20
    if len(notes) == 0:
        print("Aucune note n'a encore été jouée")
    else:
        if len(notes) > nbNoteAJouer:
            i = len(notes) - nbNoteAJouer
        else:
            i = 0
        for note in notes[i:]:
            sound = pygame.mixer.Sound(notes_dict[note][1])
            sound.play()
            time.sleep(0.2)


# =============================================== Fonction vider l'historique =================================================#


def vider():
    global notes
    notes = []
    btnVider.config(state=DISABLED)
    btnVider.config(cursor="")
    btnRejouer.config(state=DISABLED)
    btnRejouer.config(cursor="")
    btnEnregistrer.config(state=DISABLED)
    btnEnregistrer.config(cursor="")
    btnSupprimerEnregistrement.config(state=DISABLED)
    btnSupprimerEnregistrement.config(cursor="")


# ================================================= Fonction enregistrement ===================================================#


def enregistrer():
    if len(notes) == 0:
        print("Aucune note n'a encore été jouée")
    else:
        with open("pyano_partition_recorded.txt", "w") as file:
            for i in range(len(notes) - 1):
                file.write("%s," % notes[i])
            file.write("%s" % notes[-1])
            file.close()
            btnJouerEnregistrement.config(state=NORMAL)
            btnJouerEnregistrement.config(cursor="hand1")
            btnSupprimerEnregistrement.config(state=NORMAL)
            btnSupprimerEnregistrement.config(cursor="hand1")

    # ============================================== Fonction jouer enregistrement ================================================#


def jouer_enregistrement():
    notes_enregistrees = []
    file = pathlib.Path("pyano_partition_recorded.txt")
    if file.exists():
        with open("pyano_partition_recorded.txt", "r") as file:
            contenu = file.read()
            notes_enregistrees = convert(contenu)
            i = 0
            for note in notes_enregistrees[i:]:
                try:
                    notes_dict.get(note)
                    sound = pygame.mixer.Sound(notes_dict[note][1])
                    sound.play()
                    time.sleep(0.2)
                except:
                    print("Partition vide.")
    else:
        btnJouerEnregistrement.config(state=DISABLED)
        btnJouerEnregistrement.config(cursor="")


# ============================================ Fonction supprimer enregistrement ==============================================#


def supprimer_enregistrement():
    file = pathlib.Path("pyano_partition_recorded.txt")
    if file.exists():
        open("pyano_partition_recorded.txt", "w").close()
        global notes
        notes = []
        btnSupprimerEnregistrement.config(state=DISABLED)
        btnJouerEnregistrement.config(state=DISABLED)
        btnVider.config(state=DISABLED)
        btnVider.config(cursor="")
        btnRejouer.config(state=DISABLED)
        btnRejouer.config(cursor="")
        btnEnregistrer.config(state=DISABLED)
        btnEnregistrer.config(cursor="")
    else:
        btnSupprimerEnregistrement.config(state=DISABLED)
        btnSupprimerEnregistrement.config(cursor="")


# ================================================ Fonction jouer un fichier ==================================================#


def convert(string):
    li = list(string.split(","))
    return li


def jouer_fichier():
    notes_enregistrees = []
    file = pathlib.Path("pyano_partition.txt")
    if file.exists():
        with open("pyano_partition.txt", "r") as file:
            contenu = file.read()
            notes_enregistrees = convert(contenu)
            i = 0
            for note in notes_enregistrees[i:]:
                try:
                    notes_dict.get(note)
                    sound = pygame.mixer.Sound(notes_dict[note][1])
                    sound.play()
                    time.sleep(0.2)
                except:
                    print("Partition incorrecte")
    else:
        print("Aucun fichier de partition n'a été trouvé")


# ========================================================== Boutons ==========================================================#

btnVider = Button(
    widget1,
    state=DISABLED,
    text="Vider l'historique",
    width=14,
    bd=16,
    fg="brown",
    justify=CENTER,
    relief=FLAT,
    command=vider,
)
btnVider.grid(row=0, column=0, pady=1)

btnRejouer = Button(
    widget1,
    text="Rejouer",
    width=28,
    bd=34,
    fg="brown",
    justify=CENTER,
    relief=FLAT,
    state=DISABLED,
    command=vingt_dernieres_notes,
)
btnRejouer.grid(row=1, column=0, pady=1)

txtDisplay = Entry(
    widget1,
    textvariable=affiche_note,
    font=("times", 20, "bold"),
    bd=34,
    bg="brown",
    relief=FLAT,
    fg="black",
    width=28,
    justify=CENTER,
).grid(row=1, column=1, pady=1)

btnEnregistrer = Button(
    widget1,
    text="Enregistrer",
    width=28,
    bd=34,
    fg="brown",
    justify=CENTER,
    relief=FLAT,
    state=DISABLED,
    command=enregistrer,
)
btnEnregistrer.grid(row=1, column=2, pady=1)

btnJouerEnregistrement = Button(
    widget1,
    text="Jouer l'enregistrement",
    width=13,
    bd=16,
    fg="brown",
    justify=CENTER,
    relief=FLAT,
    cursor="hand1",
    command=jouer_enregistrement,
)
btnJouerEnregistrement.grid(row=0, column=2, pady=1)

btnSupprimerEnregistrement = Button(
    widget1,
    text="Supprimer l'enregistrement",
    width=16,
    bd=16,
    fg="brown",
    justify=CENTER,
    relief=FLAT,
    state=DISABLED,
    command=supprimer_enregistrement,
)
btnSupprimerEnregistrement.grid(row=2, column=2, pady=1)

if os.stat("pyano_partition_recorded.txt").st_size == 0:
    btnJouerEnregistrement.config(state=DISABLED)
    btnJouerEnregistrement.config(cursor="")
else:
    btnJouerEnregistrement.config(state=NORMAL)
    btnJouerEnregistrement.config(cursor="hand1")
    btnSupprimerEnregistrement.config(state=NORMAL)
    btnSupprimerEnregistrement.config(state=NORMAL)

btnJouerFichier = Button(
    widget4,
    text="Jouer une partition",
    width=50,
    bd=34,
    fg="brown",
    justify=CENTER,
    relief=FLAT,
    cursor="hand1",
    command=jouer_fichier,
)
btnJouerFichier.grid(row=3, column=1, pady=1)

if os.stat("pyano_partition.txt").st_size == 0:
    btnJouerFichier.config(state=DISABLED)
    btnJouerFichier.config(cursor="")
else:
    btnJouerFichier.config(state=NORMAL)
    btnJouerFichier.config(cursor="hand1")

# ========================================================== Noires ===========================================================#

btnDod = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Do#",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Do♯"),
)
btnDod.grid(row=0, column=0, padx=5, pady=5)

btnRed = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Re#",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Re♯"),
)
btnRed.grid(row=0, column=2, padx=5, pady=5)

btnVide3 = Button(
    widget2, state=DISABLED, height=6, width=2, bg="black", highlightthickness=0, bd=0
)
btnVide3.grid(row=0, column=3, padx=0, pady=0)

btnFad = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Fa#",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Fa♯"),
)
btnFad.grid(row=0, column=4, padx=5, pady=5)

btnSold = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Sol#",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Sol♯"),
)
btnSold.grid(row=0, column=6, padx=5, pady=5)

btnSib = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Sib",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Si♭"),
)
btnSib.grid(row=0, column=8, padx=5, pady=5)

btnVide4 = Button(
    widget2, state=DISABLED, height=6, width=2, bg="black", highlightthickness=0, bd=0
)
btnVide4.grid(row=0, column=9, padx=0, pady=0)

btnDod1 = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Do#",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Do#"),
)
btnDod1.grid(row=0, column=10, padx=5, pady=5)

btnRed1 = Button(
    widget2,
    height=6,
    width=6,
    bd=4,
    text="Re#",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    command=lambda: ma_note("Re#"),
)
btnRed1.grid(row=0, column=12, padx=5, pady=5)

# ==================================================== Blanches ===============================================================#

btnDo = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Do",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Do"),
)
btnDo.grid(row=0, column=0, padx=5, pady=5)

btnRe = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Re",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Re"),
)
btnRe.grid(row=0, column=1, padx=5, pady=5)

btnMi = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Mi",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Mi"),
)
btnMi.grid(row=0, column=2, padx=5, pady=5)

btnFa = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Fa",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Fa"),
)
btnFa.grid(row=0, column=3, padx=5, pady=5)

btnSol = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Sol",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Sol"),
)
btnSol.grid(row=0, column=4, padx=5, pady=5)

btnLa = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="La",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("La"),
)
btnLa.grid(row=0, column=5, padx=5, pady=5)

btnSi = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Si",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Si"),
)
btnSi.grid(row=0, column=6, padx=5, pady=5)

btnDo1 = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Do",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Do1"),
)
btnDo1.grid(row=0, column=7, padx=5, pady=5)

btnRe1 = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Re",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Re1"),
)
btnRe1.grid(row=0, column=8, padx=5, pady=5)

btnMi1 = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Mi",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Mi1"),
)
btnMi1.grid(row=0, column=9, padx=5, pady=5)

btnFa1 = Button(
    widget3,
    height=8,
    width=6,
    bd=4,
    text="Fa",
    font=("arial", 18, "bold"),
    bg="white",
    fg="black",
    command=lambda: ma_note("Fa1"),
)
btnFa1.grid(row=0, column=10, padx=5, pady=5)

# =============================================================================================================================#

root.mainloop()
