from board import board
class play_1v1:
    # declaring static veriable for counting tht moves and values

    values = [[' ' for _ in range(3)] for _ in range(3)]
    

    def __init__(self, player_name) -> None:
        self.name = player_name
        self.tracking=[]

    def __str__(self):
        return self.name

    def winner(self):
        winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 5, 7), (3, 6, 9)]
        for comb in winning_combinations:
            if (set(sorted(comb)).issubset(sorted(self.tracking))):
                print(f"{self.name} is the winner")
                return True


    def move(self, value):
        try:
            row = (value[1] - 1) // 3
            col = (value[1] - 1) % 3
            play_1v1.values[row][col] = value[0]
            board(play_1v1.values)
            
            self.tracking.append(value[1])
            
            if(self.winner()):
                exit()


        except Exception as e:
            print("error 2")
def main(p1,p2):
    count=1
    try:
        # creating two objects
        player1=play_1v1(p1)
        player2=play_1v1(p2)
        
        players_name={player1:'X',player2:'O'}
        current_player =0
        valid_moves=[]
        

        print("lets start")
        board(play_1v1.values)

        # print(players_name.keys()[0])
        while count<10:
            c_player=list(players_name.keys())[current_player]
            value_input=int(input(f"{c_player} :"))
            if(value_input>0 and value_input<10 and  value_input not in valid_moves):
                valid_moves.append(value_input)
                c_player.move((players_name[c_player],value_input))
                current_player+=1 if current_player==0 else -1
                count+=1
            else:
                print("wronng move enter again")
        print("game draw")

    except Exception as e:
        print("here 1")

if __name__ == "__main__":
    main("sharath","harry")

