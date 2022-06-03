def tictactoe():
    name= input("player 1 please enter your x or o ")
    while name!="x" and name!="o":
        name = input("pls enter x or o you dumbass")
        from IPython.display import clear_output
        clear_output()
    if name== "x":
        player1=name
        player2="o"
    else:
        player1="o"
        player2="x"
    print("Player 1 you are "+player1+ " Player 2 your are " + player2)
    from IPython.display import clear_output
    clear_output()
    
    cheblist=[" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 ","   "]
    shitlist=["|"]
    print(cheblist[0]+shitlist[0]+cheblist[1]+shitlist[0]+cheblist[2])
    print(cheblist[3]+shitlist[0]+cheblist[4]+shitlist[0]+cheblist[5])
    print(cheblist[6]+shitlist[0]+cheblist[7]+shitlist[0]+cheblist[8])
    while "x"=="x":
        shie=""
        bit=""
        if player1=="x":
            shie = "player 1"
            bit="player 2"

        if player1=="o":
            shie = "player 2"
            bit="player 1"
        points=input("please choose your point "+shie)
        while int(points)>9 or cheblist[int(points)-1]==" x " or cheblist[int(points)-1]==" o ":
            points=input("please choose your point properly")
            from IPython.display import clear_output
            clear_output()
            print(cheblist[0]+shitlist[0]+cheblist[1]+shitlist[0]+cheblist[2])
            print(cheblist[3]+shitlist[0]+cheblist[4]+shitlist[0]+cheblist[5])
            print(cheblist[6]+shitlist[0]+cheblist[7]+shitlist[0]+cheblist[8])
        else:
            cheblist[int(points)-1]=" x "  
            from IPython.display import clear_output
            clear_output()
            print(cheblist[0]+shitlist[0]+cheblist[1]+shitlist[0]+cheblist[2])
            print(cheblist[3]+shitlist[0]+cheblist[4]+shitlist[0]+cheblist[5])
            print(cheblist[6]+shitlist[0]+cheblist[7]+shitlist[0]+cheblist[8])
            if cheblist[0]== " x " and cheblist[1]== " x " and cheblist[2]== " x ":
                return "Good job"
            if cheblist[3]== " x " and cheblist[4]== " x " and cheblist[5]== " x ":
                return "Good job"
            if cheblist[6]== " x " and cheblist[7]== " x " and cheblist[8]== " x ":
                return "Good job"
            if cheblist[0]== " x " and cheblist[4]== " x " and cheblist[8]== " x ":
                return "Good job "
            if cheblist[2]== " x " and cheblist[4]== " x " and cheblist[6]== " x ":
                return "Good job "
            if cheblist[0]== " x " and cheblist[3]== " x " and cheblist[6]== " x ":
                return "Good job "
            if cheblist[1]== " x " and cheblist[4]== " x " and cheblist[7]== " x ":
                return "Good job "
            if cheblist[2]== " x " and cheblist[5]== " x " and cheblist[8]== " x ":
                return "Good job "

        points=input("please choose your point "+ bit)
        while int(points)>9 or cheblist[int(points)-1]==" x " or cheblist[int(points)-1]==" o ":
            points=input("please choose your point ")
            from IPython.display import clear_output
            clear_output()
        else: 
            cheblist[int(points)-1]=" o "  
            from IPython.display import clear_output
            clear_output()
            print(cheblist[0]+shitlist[0]+cheblist[1]+shitlist[0]+cheblist[2])
            print(cheblist[3]+shitlist[0]+cheblist[4]+shitlist[0]+cheblist[5])
            print(cheblist[6]+shitlist[0]+cheblist[7]+shitlist[0]+cheblist[8])
            if cheblist[0]== " o " and cheblist[1]== " o " and cheblist[2]== " o ":
                return "Good job"
            if cheblist[3]== " o " and cheblist[4]== " o " and cheblist[5]== " o ":
                return "Good job"
            if cheblist[6]== " o " and cheblist[7]== " o " and cheblist[8]== " o ":
                return "Good job"
            if cheblist[0]== " o " and cheblist[4]== " o " and cheblist[8]== " o ":
                return "Good job"
            if cheblist[2]== " o " and cheblist[4]== " o " and cheblist[6]== " o ":
                return "Good job"
            if cheblist[0]== " o" and cheblist[3]== " o " and cheblist[6]== " o ":
                return "Good job"
            if cheblist[1]== " o " and cheblist[4]== " o " and cheblist[7]== " o ":
                return "Good job"
            if cheblist[2]== " o " and cheblist[5]== " o " and cheblist[8]== " o ":
                return "Good job"
            

if __name__ == "__main__":
    tictactoe()
            