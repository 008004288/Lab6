#Cory Luba#
#Lab 6#

#Imports#
import os

#Variables#
total = 0

#Functions#

#Code#
def display_seat_map(aA, aB, aC, aD, aE, aF, aG, aH, aI, aJ, aK, aL, aM, aN, aO, aP, aQ, aR, aS, aT, aU, aV, aW, aX, aY, aZ, aAA, aAB, aAC, aAD):
    for r in range (1, 8):
        print("   ", r, " ", aA[r],"", aB[r], "", aC[r], "", aD[r], "", aE[r], "", aF[r], "", aG[r], "", aH[r], "", aI[r], "", aJ[r], "", aK[r], "", aL[r], "", aM[r], "", aN[r], "", aO[r], "", aP[r], "", aQ[r], "", aR[r], "", aS[r], "", aT[r], "", aU[r], "", aV[r], "", aW[r], "", aX[r], "", aY[r], "", aZ[r], "", aAA[r], "", aAB[r], "", aAC[r], "", aAD[r])

aisleA = ["","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"]
aisleB = ["","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"]
aisleC = ["","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C"]
aisleD = ["","D","D","D","D","D","D","D"]
aisleE = ["","E","E","E","E","E","E","E"]
aisleF = ["","F","F","F","F","F","F","F"]
aisleG = ["","G","G","G","G","G","G","G"]
aisleH = ["","H","H","H","H","H","H","H"]
aisleI = ["","I","I","I","I","I","I","I"]
aisleJ = ["","J","J","J","J","J","J","J"]
aisleK = ["","K","K","K","K","K","K","K"]
aisleL = ["","L","L","L","L","L","L","L"]
aisleM = ["","M","M","M","M","M","M","M"]
aisleN = ["","N","N","N","N","N","N","N"]
aisleO = ["","O","O","O","O","O","O","O"]
aisleP = ["","P","P","P","P","P","P","P"]
aisleQ = ["","Q","Q","Q","Q","Q","Q","Q"]
aisleR = ["","R","R","R","R","R","R","R"]
aisleS = ["","S","S","S","S","S","S","S"]
aisleT = ["","T","T","T","T","T","T","T"]
aisleU = ["","U","U","U","U","U","U","U"]
aisleV = ["","V","V","V","V","V","V","V"]
aisleW = ["","W","W","W","W","W","W","W"]
aisleX = ["","X","X","X","X","X","X","X"]
aisleY = ["","Y","Y","Y","Y","Y","Y","Y"]
aisleZ = ["","Z","Z","Z","Z","Z","Z","Z"]
aisleAA = ["","AA","AA","AA","AA","AA","AA","AA"]
aisleAB = ["","AB","AB","AB","AB","AB","AB","AB"]
aisleAC = ["","AC","AC","AC","AC","AC","AC","AC"]
aisleAD = ["","AD","AD","AD","AD","AD","AD","AD"]

def seats():
    data = input("Enter another seat? (y/n): ").lower()
    while(data != "y" and data != "n"):
        data = input("Enter another seat? (y/n): ").lower()
    return data

more_data = "y"
while(more_data == "y"):
    os.system('cls')
    display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    row = int(input("Row number: ").upper())
    seat=input("Seat number: ")
    if seat=="A":
        if aisleA[row]=="X":
            print("That seat is already assigned.")
        else:
            aisleA[row]="X"
            os.system('cls')
            display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="B":
            if aisleB[row]=="X":
                print("That seat is already assigned.")
            else:
                aisleB[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="C":
            if aisleC[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleC[row]="X"
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="D":
            if aisleD[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleD[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="E":
            if aisleE[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleE[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="F":
            if aisleF[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleF[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="G":
            if aisleG[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleG[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="H":
            if aisleH[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleH[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="I":
            if aisleI[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleI[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="J":
            if aisleJ[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleJ[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="K":
            if aisleK[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleK[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="L":
            if aisleL[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleL[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="M":
            if aisleM[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleM[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="N":
            if aisleN[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleN[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="O":
            if aisleO[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleO[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="P":
            if aisleP[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleP[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="Q":
            if aisleQ[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleQ[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="R":
            if aisleR[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleR[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="S":
            if aisleS[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleS[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="T":
            if aisleT[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleT[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="U":
            if aisleU[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleU[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="V":
            if aisleV[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleV[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="E":
            if aisleD[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleD[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="W":
            if aisleW[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleW[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="X":
            if aisleX[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleX[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="Y":
            if aisleY[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleY[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="Z":
            if aisleZ[row]=="X":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleZ[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="AA":
            if aisleAA[row]=="XX":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleAA[row]="XX"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="AB":
            if aisleAB[row]=="XX":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleAB[row]="XX"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="AC":
            if aisleAC[row]=="XX":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleAC[row]="XX"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    elif seat=="AD":
            if aisleAD[row]=="XX":
                os.system('cls')
                print("That seat is already assigned.")
            else:
                aisleAD[row]="X"
                os.system('cls')
                display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
    else:
            print("Incorrect seat selection.")
            os.system('cls')
            display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
            print(total)
    more_data = seats()
    print(total)
    if row=="A":
        total = total + 200
os.system('cls')
print("Airplane Seating Chart: ")
display_seat_map(aisleA, aisleB, aisleC, aisleD, aisleE, aisleF, aisleG, aisleH, aisleI, aisleJ, aisleK, aisleL, aisleM, aisleN, aisleO, aisleP, aisleQ, aisleR, aisleS, aisleT, aisleU, aisleV, aisleW, aisleX, aisleY, aisleZ, aisleAA, aisleAB, aisleAC, aisleAD)
print(total)
