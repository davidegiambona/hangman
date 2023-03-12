import random

ditionary = [
    "abba",
    "abbi",
    "abel",
    "acca",
    "acme",
    "acne",
    "acre",
    "acri",
    "acro",
    "acta",
    "adda",
    "addì",
    "aden",
    "adro",
    "adsl",
    "aedo",
    "affi",
    "afta",
    "agio",
    "agna",
    "agra",
    "agro",
    "aida",
    "aido",
    "aids",
    "aire",
    "alba",
    "albo",
    "alca",
    "alce",
    "alda",
    "aldo",
    "alea",
    "ales",
    "beta",
    "beve",
    "bice",
    "bide",
    "blue",
    "bore",
    "boxe",
    "brez",
    "bure",
    "byte",
    "cale",
    "cane",
    "cave",
    "cebo",
    "cece",
    "ceco",
    "cena",
    "cene",
    "cere",
    "cero",
    "ceto",
    "chef",
    "ciel",
]

print("[**REGOLE DEL GIOCO**]\n",
      "1 regola = Hai a disposizione 5 tentativi per sbagliare (Non di piu!!)\n",
      "2 regola = I caratteri delle parole sono tutti in MINUSCOLO (Non inserire caratteri maiuscoli!!)\n",
      "3 regola = Non inserire caratteri gia inseriti in precedenza (eccetto caso necessario), saresti ripetitivo :( !\n",
      "4 regola = LE REGOLE SONO FINITE :) !!! Divertiti e non fare storie, gioco mio regole mie hihihihihi!\n")

tentativi = 5
indovino = 0

char_corretti = ['', '', '', '']

random_string = random.choice(ditionary)

print("\nparola da indovinare: ", random_string[0], "* *", random_string[3])

while tentativi != 0 and indovino != 4:
    lettera = input(
        "inserisci una lettera che corrisponda ad una della parola: ")
    if lettera in char_corretti:
        print("\nerrore carattere gia' inserito!")
        tentativi = tentativi-1

    if lettera in random_string and lettera not in char_corretti:
        char_corretti = lettera
        print("\nlettera corretta: ", lettera)
        indovino = indovino+1

    elif lettera not in random_string:
        tentativi = tentativi-1
        print("\nscusa, prova di nuovo")


if indovino == 4:
    print("\n\t [ hai vinto parola da indovinare: ", random_string, " ]")
    print("\n")
elif tentativi == 0:
    print("\n\thai perso cambia gioco", "\n\t",
          "[ parola da indovinare: ", random_string, " ]")
    print("\n")


exit = input("Vuoi uscire dal gioco? ")
if exit in "yes":
    print("Uscita in corso...\nUscita completata")
elif exit in "no":
    print("Esci lo stesso!")
