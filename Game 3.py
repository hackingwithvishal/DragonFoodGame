import turtle
import random
import winsound

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.bgpic("Bg image.png")
wn.setup(width = 800, height = 600)
wn.tracer(0)

wn.addshape("Player left.gif")
wn.addshape("Player right.gif")
wn.addshape("good.gif")
wn.addshape("bad.gif")

# Add the Player
player = turtle.Turtle()
player.speed(0)
player.shape("Player right.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Create a List of good guys
good_guys = []


# Add the good_guy
for _ in range (20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("good.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)



# Create a List of bad guys
bad_guys = []


# Add the bad_guys
for _ in range (5):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("bad.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)


# Make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Score : {} Lives : {}".format(score, lives), align = "center", font=font)

  
#Function
def go_left():
    player.direction = "left"
    player.shape("Player left.gif")
    

def go_right():
    player.direction = "right"
    player.shape("Player right.gif")

#Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

    
# Main Game Loop
while True:

    # Update scree
    wn.update()
    
    # Move The Player

    if player.direction == "left":
        x = player.xcor()
        x -= 2
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 2
        player.setx(x)    

    # Move the good_guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
        # good_guy.sety(good_guy.ycor() -1) that is Combaind Mode

        #Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(-300, 400)
            good_guy.goto(x, y)

        # Check for a collision with the player
        if good_guy.distance(player) < 40:
            winsound.PlaySound("good.mp3", winsound.SND_ASYNC)
            x = random.randint(-380, 380)
            y = random.randint(-300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score : {} Lives : {}".format(score, lives), align = "center", font=font)
            

    # Move the bad_guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
        # bad_guy.sety(bad_guy.ycor() -1) that is Combaind Mode

        #Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(-300, 400)
            bad_guy.goto(x, y)

        # Check for a collision with the player
        if bad_guy.distance(player) < 40:
            winsound.PlaySound("bad.mp3", winsound.SND_ASYNC)
            x = random.randint(-380, 380)
            y = random.randint(-300, 400)
            bad_guy.goto(x, y)
            score -= 10
            pen.clear()
            lives -=1 
            pen.write("Score : {} Lives : {}".format(score, lives), align = "center", font=font)
            
wn.mainloop()
