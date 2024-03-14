import pandas as pd
import random
from colorama import Fore, Style, init
init()

def main():
    print("enumerate name of countries:\n\n")
    df=pd.read_csv("xml.csv")

    print("1-Africa")
    print("2-Europe")
    print("3-Oceania")
    print("4-Asia")
    print("5-Antarctic")
    print("6-Americas")
    intContinent=int(input("input the # that corresponds to the continent of your choice:\n"))
    strContinent=""
    match intContinent:
        case 1: 
            strContinent = "AFRICA"
        case 2: 
            strContinent = "EUROPE"
        case 3: 
            strContinent = "OCEANIA"
        case 4: 
            strContinent = "ASIA"
        case 5: 
            strContinent = "ANTARCTIC"
        case 6: 
            strContinent = "AMERICAS"


    # continentList = [item[1] for item in df.values.tolist()]
    # continentList =list((set(continentList)))
    completeList = df.values.tolist()
    chosenList = [item[0] for item in completeList if item[1].upper()==strContinent]
    givenList =[]
    strCountry = input(Fore.WHITE+"input country in "+strContinent+":")
    score = 0
    wrong = 0
    clueCount = 0
    x=""
    if(clueCount==0 and strCountry.upper()=="C"):
         print("wow ah clue kagad? bobo")

    while True:
        if validate(chosenList,strCountry,givenList):
            score = score + 1
            print(Fore.GREEN + "correct!",end="")
            print("there are",len(chosenList),"countries left") 
            if len(chosenList)==0:
                game_ended(chosenList,score,clueCount)
                break
        elif(strCountry.upper() in givenList):
            print(Fore.LIGHTRED_EX + "you already gave that country")
        else:
            print(Fore.RED + "wrong country") 
            wrong=wrong+1       
        
        while True:
            strCountry = input(Fore.WHITE+"input country in " + strContinent + " ('c' for clue or 'x' to end the game)")
            if strCountry.upper()=="X":
                game_ended(chosenList,score,clueCount,wrong)
                return
            elif strCountry.upper() == "C":
                clueCount+=1
                print(Fore.MAGENTA+"clue:",clue(chosenList))
            else:
                break


def validate(chosenList,strCountry,givenList):
        for i, item in enumerate(chosenList):
            if(item.upper()==strCountry.upper()):
                chosenList.pop(i)
                givenList.append(item.upper())
                return True
        return False

def clue(chosenList):
        chosenCountry = chosenList[random.randint(0,len(chosenList))-1]
        clueCountry = ""
        for i in chosenCountry:
            if(random.randint(0,1))==0:
                clueCountry+='_'
            else:
                clueCountry+=i
        return clueCountry
def game_ended(chosenList,score,clueCount,wrong):
                print(Fore.CYAN + "\n\ngame ended - your score is",score)
                print(Fore.MAGENTA+"clue was used",clueCount,"time/s")
                print(Fore.RED+"you answered wrong",wrong,"time/s")
                print(Fore.YELLOW+"the remaining countries are:\n", Fore.LIGHTWHITE_EX,chosenList)
                x=input(Fore.WHITE+"press any key to exit")
           

main()



    


