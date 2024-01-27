from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.goto(0, 270)
		self.penup()
		self.color("white")
		self.update_score()
		self.hideturtle()

	def update_score(self):
		self.clear()
		self.write(f"Home = {self.score}", align=ALIGNMENT, font=FONT)


	def increase_score(self):
		self.score += 1
		self.update_score()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)