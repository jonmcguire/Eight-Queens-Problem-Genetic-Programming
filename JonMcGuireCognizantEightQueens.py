'''
Code by Jon McGuire
Description

The eight queens puzzle is the problem of placing:
    eight chess queens on an 8×8 chessboard 
    so that no two queens threaten each other
    
thus, a solution requires that 
no two queens share:
    same row,
    column,
    or diagonal. 


Challenge

The challenge is to generate one right sequence through Genetic Programming. 
The sequence has to be 8 numbers between 0 to 7.
Each number represents the positions the Queens can be placed. 
Each number refers to the row number in the specific column

0 3 4 5 6 1 2 4

0 is the row number in the column 0 where the Queen can be placed

3 is the row number in the column 1 where the Queen can be placed


Sample Codebase
The following is a sample code base for solving text generation using Genetic Computing 
https://github.com/datasigntist/deeplearning/blob/master/Introduction_to_Genetic_Computing_2.ipynb

'''

import random


class board:
    setup=[7,1,3,0,6,4,2,5]
    fitness=1.0
    
    def set_board(self,x):
        self.setup=x
    
    #initial population
    def generate_board(self):
        self.setup = random.sample(range(0, 8), 8)
    
    #ratio of the number of nonattacking pairs of queens
    #total number of different pairs that can be formed among n queens.
    
    def fit_score(self):
        bad=0
        total=28
        #row
        bad+=8-(len(set(self.setup)))        
        index=0
        for q in self.setup:
            local_index=index+1
            neg=1
            while(local_index<8):
                if((q+neg)==(self.setup[local_index])):
                    bad+=1
                if((q-neg)==(self.setup[local_index])):
                    bad+=1
                neg+=1
                local_index+=1
            index+=1
        self.fitness=((total-bad)/total)
            


def create_boardlist():
    boardlist = list()
    for i in range(4):
        i=board()
        i.generate_board()
        i.fit_score()
        boardlist.append(i)
    
    return boardlist
    

def crossovermutate(boardlist):
    newlist=[]
    alt=1
    split=random.randint(1,6)
    
    for i in boardlist:
        if alt%2==1:
            firststart=i.setup[:split]
            firstend=i.setup[split:]
        elif alt%2==0:
            secondstart=i.setup[:split]
            secondend=i.setup[split:]
            
            b1mutate=firststart+secondend
            b2mutate=secondstart+firstend
            
            b1mutate[random.randint(0,7)]=random.randint(0,7)
            b2mutate[random.randint(0,7)]=random.randint(0,7)
            
            board1=board()
            board1.set_board(b1mutate)
            board1.fit_score()
            
            board2=board()
            board2.set_board(b2mutate)
            board2.fit_score()
            
            newlist.append(board1)
            newlist.append(board2)
            
            split=random.randint(1,6)
        alt+=1
    return newlist

def checksolution(boardlist):
    average=0
    for x in boardlist:
        if(x.fitness==1.0):
            return [True, x.setup]
        else:
            average+=x.fitness
    return [False, (average/4)]

def start():
    fit=False
    gencount=1
    while(fit==False):
        print("Generation ",gencount)
        blist=create_boardlist()
        blist.sort(key = lambda x: x.fitness)
        
        if(checksolution(blist)[0]==False):
            print("Average Fitness", checksolution(blist)[1] )
        else:
            fit=True
            print('Found Solution: ', checksolution(blist)[1])
            
        blist=crossovermutate(blist)
        blist.sort(key = lambda x: x.fitness)
        gencount+=1
        print()

if __name__ == '__main__':
    start()

