# Import the turtle module
import turtle

# Set up the game window
wind = turtle.Screen()  # Create a window for the game
wind.title("Ping Pong By Shoman")  # Set the title of the window
wind.bgcolor("black")  # Set the background color to black
wind.setup(width=800, height=600)  # Set the dimensions of the window
wind.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create the first paddle (madrab1)
madrab1 = turtle.Turtle()  # Create a turtle object for the first paddle
madrab1.speed(0)  # Set the speed of the paddle animation to the maximum
madrab1.shape("square")  # Set the shape of the paddle to a square
madrab1.color("blue")  # Set the color of the paddle to blue
madrab1.shapesize(stretch_len=1, stretch_wid=5)  # Stretch the shape to form a rectangle
madrab1.penup()  # Lift the pen to avoid drawing on the screen
madrab1.goto(-350, 0)  # Position the paddle on the left side of the screen

# Create the second paddle (madrab2)
madrab2 = turtle.Turtle()  # Create a turtle object for the second paddle
madrab2.speed(0)  # Set the speed of the paddle animation to the maximum
madrab2.shape("square")  # Set the shape of the paddle to a square
madrab2.color("orange")  # Set the color of the paddle to orange
madrab2.shapesize(stretch_len=1, stretch_wid=5)  # Stretch the shape to form a rectangle
madrab2.penup()  # Lift the pen to avoid drawing on the screen
madrab2.goto(350, 0)  # Position the paddle on the right side of the screen

# Create the ball
ball = turtle.Turtle()  # Create a turtle object for the ball
ball.speed(0)  # Set the speed of the ball animation to the maximum
ball.shape("circle")  # Set the shape of the ball to a circle
ball.color("white")  # Set the color of the ball to white
ball.penup()  # Lift the pen to avoid drawing on the screen
ball.goto(0, 0)  # Position the ball in the center of the screen
ball.dx = 0.2  # Set the horizontal movement speed of the ball
ball.dy = 0.2  # Set the vertical movement speed of the ball

# Initialize the scores
score1 = 0  # Initialize the score for Player 1
score2 = 0  # Initialize the score for Player 2
score = turtle.Turtle()  # Create a turtle object for displaying the score
score.speed(0)  # Set the speed of the score animation to the maximum
score.color("white")  # Set the color of the score text to white
score.penup()  # Lift the pen to avoid drawing on the screen
score.hideturtle()  # Hide the turtle object (we only want the text)
score.goto(0, 260)  # Position the score text near the top of the screen
score.write("Player 1: 0 ___ Player 2: 0", align="center", font=("Courier", 24, "normal"))  # Display the initial score

# Define functions to move the paddles
def madrab1_up():
    y = madrab1.ycor()  # Get the current y-coordinate of madrab1
    y += 40  # Increase the y-coordinate by 40
    madrab1.sety(y)  # Set the new y-coordinate for madrab1

def madrab1_down():
    y = madrab1.ycor()  # Get the current y-coordinate of madrab1
    y -= 40  # Decrease the y-coordinate by 40
    madrab1.sety(y)  # Set the new y-coordinate for madrab1

def madrab2_up():
    y = madrab2.ycor()  # Get the current y-coordinate of madrab2
    y += 40  # Increase the y-coordinate by 40
    madrab2.sety(y)  # Set the new y-coordinate for madrab2

def madrab2_down():
    y = madrab2.ycor()  # Get the current y-coordinate of madrab2
    y -= 40  # Decrease the y-coordinate by 40
    madrab2.sety(y)  # Set the new y-coordinate for madrab2

# Set up keyboard bindings
wind.listen()  # Listen for keyboard input
wind.onkeypress(madrab1_up, "w")  # Move madrab1 up when 'w' is pressed
wind.onkeypress(madrab1_down, "s")  # Move madrab1 down when 's' is pressed
wind.onkeypress(madrab2_up, "Up")  # Move madrab2 up when 'Up' arrow is pressed
wind.onkeypress(madrab2_down, "Down")  # Move madrab2 down when 'Down' arrow is pressed

# Main game loop
while True:
    wind.update()  # Update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Update the ball's x-coordinate
    ball.sety(ball.ycor() + ball.dy)  # Update the ball's y-coordinate

    # Check for collision with the top border
    if ball.ycor() > 290:
        ball.sety(290)  # Set the y-coordinate to the top border
        ball.dy *= -1  # Reverse the vertical direction

    # Check for collision with the bottom border
    if ball.ycor() < -290:
        ball.sety(-290)  # Set the y-coordinate to the bottom border
        ball.dy *= -1  # Reverse the vertical direction

    # Check for collision with the right border
    if ball.xcor() > 390:
        ball.goto(0, 0)  # Reset the ball to the center
        ball.dx *= -1  # Reverse the horizontal direction
        score1 += 1  # Increment the score for Player 1
        score.clear()  # Clear the previous score
        score.write(f"Player 1: {score1} ___ Player 2: {score2}", align="center", font=("Courier", 24, "normal"))  # Update the score display

    # Check for collision with the left border
    if ball.xcor() < -390:
        ball.goto(0, 0)  # Reset the ball to the center
        ball.dx *= -1  # Reverse the horizontal direction
        score2 += 1  # Increment the score for Player 2
        score.clear()  # Clear the previous score
        score.write(f"Player 1: {score1} ___ Player 2: {score2}", align="center", font=("Courier", 24, "normal"))  # Update the score display

    # Check for collision with madrab2 (right paddle)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)  # Set the x-coordinate to avoid passing the paddle
        ball.dx *= -1  # Reverse the horizontal direction

    # Check for collision with madrab1 (left paddle)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)  # Set the x-coordinate to avoid passing the paddle
        ball.dx *= -1  # Reverse the horizontal direction
