from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
        

    def update_score(self):
        self.write(f"score:{self.score}",align ="center",font=("Arial",24,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def getting_name(self):
        self.name = self.screen.textinput(title="snake Game", prompt="enter a name of the player: ")
    
    def filetext(self):
        self.file=open("sample.csv","a")
        self.a=self.file.write(f"\n{str(self.name)},{self.score}")


    def game_over(self):
        self.filetext()
        self.goto(0,0)
        self.write(f"GAMEOVER",align="center",font=("Arial",24,"normal"))