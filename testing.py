import random
import time

wheel = [0,21,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
typenumb = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}

def randnumb():
   return random.randint(0,36)

def printlist():
    return [str(random.randint(0,36)) for i in range(10)]
    
def printgame():
    for i in range(10):
        a = printlist()
        for j in range(len(a)):
            time.sleep(0.05)
            print(a[j])
            
def realisticpositions():
    List = [randnumb()]
    for i in range(75):
        choices = [-4,-3,-2,-1,1,2,3,4]
        ne = choices[random.randint(0,7)]
        if List[-1] + ne > 36:
            List.append(36 - List[-1] - ne + 1)
        elif List[-1] + ne < 0:
            List.append(36 + List[-1] + ne + 1)
        else:
            List.append(List[-1] + ne)
    return List


def printrealistic(L):
    wheel = [" 0","21","15","19"," 4","21"," 2","25","17",
                 "34"," 6","27","13","36","11","30"," 8","23",
                 "10"," 5","24","16","33"," 1","20","14","31",
                 " 9","22","18","29"," 7","28","12","35"," 3","26"]
    for i in range(1):
        for x in range(len(wheel)):
            for _ in range(15):
                print("\n")
            print("|".join(wheel))
            print("|".join(["  " for i in range(0,x)] + ["**"] +  ["  " for i in range(x,37)]))
            time.sleep(0.08)
    
    for j in range(L[0]):
        for _ in range(15):
            print("\n")
        print("|".join(wheel))
        print("|".join(["  " for i in range(0,j)] + ["**"] +  ["  " for i in range(j,37)]))
        time.sleep(0.1)
    
    for i in range(len(L)):
        for _ in range(15):
            print("\n")
        print("|".join(wheel))
        
        print("|".join(["  " for i in range(0,L[i])] + ["**"] +  ["  " for i in range(L[i],36)]))
        time.sleep(0.1)
    

class Board():
    def __init__(self):
        self.what = None


class Player():
    def __init__(self,money):
        self.money = money
        self.turn = {}
      
    def inputturn(self,choice,amount):
        if choice not in self.turn:
            self.turn[choice] = amount
        else:
            self.turn[choice] += amount
    
    def printstatus(self):
        print("You have {} € left".format(self.money))
        print("Your bets are", self.turn)
        
    def printchoices(self):
        print("\n")
        print("What do you want to do, bet:")
        print("'odd', 'even'?")
        print("'black', 'red'")
        print("'1rst': 1-12, '2nd': 13-24, '3rd': 25-36")
        print("Bet on '0'")
        print("Or 'end'")
    
    def choose(self):
        while True:
            self.printstatus()
            self.printchoices()
            x = input()
            choices = ["odd","even","black","red","1rst","2nd","3rd", "0","end"]
            if x in choices:
                if x == "end":
                    break
                y = int(input("Input how much you want to bet for {}: \n".format(x)))
                print("\n")
                if self.money - y > 0:
                    self.inputturn(x,y)
                    self.money -= y
                    for _ in range(15):
                        print("\n")
                elif self.money - y < 0:
                    for _ in range(15):
                        print("\n")
                    print("Your bet exceeds your total money")
                    print("\n")
                else:
                    for _ in range(15):
                        print("\n")
                    self.inputturn(x,y)
                    self.money -= y
                    print("No more money to bet")
                    print("Your bets are", self.turn)
                    break
            else:
                for _ in range(15):
                    print("\n")
                print("\n Please select correct bet \n")
            
                
    def result(self,n):
        moneywon = 0
        colour = typenumb[n]
        print("{} is {}".format(n,colour))
        if "odd" in self.turn:
            if n % 2 != 0:
                moneywon += 2 * self.turn["odd"]
        if "even" in self.turn:
            if n % 2 == 0:
                moneywon += 2 * self.turn["even"]
        if "black" in self.turn:
            if colour == "black":
                moneywon += 2 * self.turn["black"]
        if "red" in self.turn:
            if colour == "red":
                moneywon += 2 * self.turn["red"]
        if "1rst" in self.turn:
            if n in [i for i in range(1,13)]:
                moneywon += 3 * self.turn["1rst"]
        if "2nd" in self.turn:
            if n in [i for i in range(13,25)]:
                moneywon += 3 * self.turn["2nd"]
        if "3rd" in self.turn:
            if n in [i for i in range(25,37)]:
                moneywon += 3 * self.turn["3rd"]
        if "0" in self.turn:
            if n == 0:
                moneywon += 35 * self.turn["0"]
        
        print("Total money won is: {} €".format(moneywon))
        self.money += moneywon
        print("Total money is: {} €".format(self.money))
        
        
#printgame()
#a = [random.randint(-4,4) for i in range(1000)]
#dic = {}
#for i in a:
#    el = str(i)
#    if el in dic:
#        dic[el] += 1
#    else:
#        dic[el] = 1
#print(dic)
        
def __main__():
    a = Player(100)
    while a.money != 0:
        b = Board()
        a.choose()
        play = realisticpositions()
        b.what = wheel[play[-1]]
        print("The wheel will turn in: ")
        time.sleep(0.5)
        for i in [3,2,1]:
            print(i)
            time.sleep(1) 
        print("\n")
        printrealistic(play)
        print("\n")
        a.result(b.what)
        print("\n")
        a.turn = {}

__main__()

