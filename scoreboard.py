from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		with open("data.txt") as score_file:
			self.high_score = int(score_file.read())
		self.goto(0, 270)
		self.penup()
		self.color("white")
		self.update_score()
		self.hideturtle()

	def update_score(self):
		self.clear()
		self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.update_score()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", mode="w") as score_file:
				score_file.write(str(self.score))
		self.score = 0
		self.update_score()
