from board import board


class play_1v1:
    #declaring static veriable for counting tht moves and values
  
    values=[[' 'for _ in range(3)] for _ in range(3)]

    
    def __init__(self,player_name) -> None:
        self.name=player_name
    
    def __str__(self):
        return self.name

    @staticmethod 
    def move(value):
        print(value)

    







def main(p1,p2):
    count=1
    try:
        player1=play_1v1(p1)
        player2=play_1v1(p2)
        
        players_name={player1:'X',player2:'O'}
        current_player =0

        

        print("lets start")
        board(play_1v1.values)

        # print(players_name.keys()[0])
        while count<10:
            c_player=list(players_name.keys())[current_player]
            value_input=int(input(f"{c_player} :"))

            play_1v1.move((players_name[c_player],value_input))

            
            current_player+=1 if current_player==0 else -1
            count+=1
        else:
            pass
    except:
        print("error")

if __name__ == "__main__":
    main("sharath","harry")

