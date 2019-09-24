#! bin/bash

# Pyttleship v0.0.1
# Scripted on Linux Ubuntu with VSCode by Michele Guidetti (Miggu4n) on 24/09/2019
# Feel free to use this code as you wish.
# This is just a basic project I made, but I'm planning to finish it, adding a COM vs PLAYER (actually this is a PLAYER vs COM, unidirectional) and, maybe, a multiplayer.
# Change os.system("clear") with os.system("cls") if you are using this code on NT. 
# Bye!

from random import *
import time
import os

lettere = ["a",
           "b",
           "c",
           "d",
           "e",
           "f",
           "g",
           "h",
           "i",
           "j",
           ]

navi = [
        [True, True],
        [True, True],
        [True, True],
        [True, True],
        [True, True, True],
        [True, True, True],
        [True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True, True]
    ]

direzioni = [0,1,2,3]


def nuovoCampo():
    field = []
    for l in lettere:
        riga = []
        for n in range(1,len(lettere)+1):
            casella = "{}{}".format(l,n)
            riga.append(casella)
        field.append(riga)
    return field

def nuovaPartita():

    # genero il campo nemico
    campo = nuovoCampo()
    campo_confronto = nuovoCampo()
    
    flotta = 0
    for n in navi:
        # calcolo e ricavo dimensioni di nave e flotta
        lun = len(n)
        flotta = flotta + lun
        
        # prelevo indici della casella
        posTrovata = False
        
        
        while posTrovata == False:
            # ad ogni giro scelgo una casella e direzione diversa. 
            casella = (choice(choice(campo)))
            found = False
            
            
            for r in campo:
                for c in r:
                    if c == casella:
                        indexC = r.index(c)
                        found = True
                       
                        
                if found == True:
                    indexR = campo.index(r)
                    break
                
                
            # primo check
            libero = True
            if casella == "||" or casella == "==":
                libero = False
                
                
            direzione = choice(direzioni)
            if direzione == 0:
                # vado in alto, quindi calcolo sulle righe ovvero il primo indice
                if indexR < lun:
                    pass
                
                else:
                    # prima controllo che sia tutto libero. Assumo che sia libero fino a prova contraria.
                    for p in range(indexR - lun, indexR):
                        if campo[p][indexC] == "||" or campo[p][indexC] == "==":
                            libero = False
                            break
                        
                        
                    if libero == True:
                        for p in range(indexR - lun, indexR):
                            campo[p][indexC] = "||"
                        posTrovata = True
                    
                    
            if direzione == 1:
                # vado a destra, quindi calcolo sulle colonne ovvero secondo indice
                if indexC > (lun - 1):
                    pass     
                
                else:
                    # prima controllo che sia tutto libero. Assumo che sia libero fino a prova contraria.
                    for p in range(indexC, indexC + lun):
                        if campo[indexR][p] == "||" or campo[indexR][p] == "==":
                            libero = False
                            break
                         
                            
                    if libero == True:
                        for p in range(indexC, indexC + lun):
                            campo[indexR][p] = "=="

                        posTrovata = True
            
            if direzione == 2:
                # vado in basso, quindi calcolo sulle righe ovvero il primo indice
                if indexR > (lun - 1):
                    pass
                else:
                    # prima controllo che sia tutto libero. Assumo che sia libero fino a prova contraria.
                    for p in range(indexR, indexR + lun):
                        if campo[p][indexC] == "||" or campo[p][indexC] == "==":
                            libero = False
                            break
                            
                    if libero == True:
                        for p in range(indexR, indexR + lun):
                            campo[p][indexC] = "||"
                        
                        posTrovata = True
                    
                    
            if direzione == 3:
                # vado a sinistra, quindi calcolo sulle c ovvero il secondo indice
                if indexC < (lun - 1):
                    pass
                else:
                    # prima controllo che sia tutto libero. Assumo che sia libero fino a prova contraria.
                    for p in range((indexC - lun), indexC):
                        if campo[indexR][p] == "||" or campo[indexR][p] == "==":
                            libero = False
                            break
                            
                    if libero == True:
                        for p in range((indexC - lun), indexC):
                            campo[indexR][p] = "=="
                        posTrovata = True
                    
    
    a_segno = 0
    for shot in range(60):
        os.system("clear")
        
        for r in campo_confronto:
            print(r)
        
        
        colpo = raw_input("Casella da attaccare: ")
        
        #ricavo indici dal campo di confronto
        print(colpo)
        for r in campo_confronto:
            for c in r: 
                if colpo == c:
                    print("La casella esiste: {} \t {}".format(colpo, c))
                    cColpo = r.index(colpo)
                    rColpo = campo_confronto.index(r)
                    
                    if campo[rColpo][cColpo] == "||" or campo[rColpo][cColpo] == "==":
                        a_segno +=1
                        print("Colpito!")
                        campo_confronto[rColpo][cColpo] = "XX"
                        
                    else:
                        print("Mancato!")
        
        
        if a_segno >= flotta:
            break
        else:
            pass
        
    if a_segno >= flotta:
        print("Hai vinto!")
    else:
        print("Hai perso!")
    
    

    
    
    
def main():
    nuovaPartita()
    

if __name__ == "__main__":
    main()
