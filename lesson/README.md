# Think Like A Programmer Lesson Plan

This README contains the lesson plan for the Think Like A Programmer workshop for beginner python programmers. The workshop is designed to introduce students to the fundamentals of programming and help them build their first program.

## Part 1 - Think Like A Programmer

### Before We Start
-
-
-
-
- everything we do today can be done in pairs. if you would feel more comfortable working with someone else, please raise your hand to let me know. otherwise, you can work alone

### Why You Should Learn to Code
- none of you have existed in a world without computers. neither have I! it is unlikely that you will ever live in a world without computers. learning to code is learning a new way to understand and interact with the world around you
- 
- computers need to be told what to do. they are very fast, but they are not smart. they can only do what they are told to do
- learning to code is learning how to tell a computer what to do
-

### What is Programming?
- 
- programs are most commonly written in a file called a "source file". this file is written in a programming language, which is a set of rules that the computer can understand
-
-
<!-- ### Different Languages
- we will be using Python today. Python is a very popular language for beginners because it is easy to read and write
- Python is the main language of AI and machine learning. it is also used for web development, data analysis, and many other things -->

## Part 2 - Fundamentals

### Types, Variables, and Reserved Words
-
- their value must be one of the data types in the language
- if, and else in this line of code are reserved words

### Control Structures and Operators
- control structures are the building blocks of programs. they allow you to control the flow of the program
- == is used to compare two values, like = in a math equation. Python uses = for assignment, and == for comparison

### Object Oriented Programming
- there are other types of programming, but we will be focusing on object oriented programming today.
- object oriented programming is a way of organizing code. it is based on the idea of objects, which are collections of data and functions that work together.
- a class is a blueprint for an object. it defines the data and functions that the object will have

## Part 3 - Hello World
- Now it's time to get coding!
- I am going to take you through the process of making your first program. This is the classic entrypoint to programming, and it's a great way to get started
- We will be doing setup steps as part of this example, so you can see how to get started with Python on your own computer
- a terminal is the program on your computer that allows you to interact with the computer using text commands. it is also called a command line interface, or CLI
- a text editor is a program that allows you to write and edit text files. we will be using a text editor called Visual Studio Code to write our Python code

## Part 4 - Tic Tac Toe
Now that you have made a program, let's make a game. Tic Tac Toe is a simple game that can be made with a few lines of code. Let's see how it works.

### Conceptualize the Game
- Let's start by thinking about tic tac toe. Just for fun, let's play a couple games on the board to get the hang of it before we talk about it. Can I have two volunteers to play a game of tic tac toe? x2
- Okay, time to think about about how the game of tic tac toe works. We have a board (3x3 grid) and two players. Each player takes turns placing their mark on the board. The first player to get three in a row wins.
- How can we turn this into a recipe? Any ideas?
- Let's break it down into steps:
    1. Create a board
    2. Display the board
    3. Get input from the player
    4. Update the board
    5. Check for a winner
    6. Repeat steps 2-5 until there is a winner or the board is full
- Now that we have a plan, let's start coding!
- Just like with the car, we are going to make a class for the game. This class will have functions for each of the steps in our plan.
- write the class App
    - write init placeholder function
    - write play_game placeholder function
    - print board placeholder function
    - check winner placeholder function
- let's start with the init function. this function is called when a new object of the class is created. it is used to set up the object. in this case, we are going to use it to create the board and set up the players
    - draw tic tac toe board on the board.
    - turn the board into a grid to show them visually how it works
    - draw a list of lists next to the grid showing the indexes of each cell
    - add the board code and players
- now let's implement the print board function. I already wrote this function, so copy what I have written into your code and we'll see how it works
- now we can add the print board function to our play game function. let's test it out
- to run the code, we are going to add a main function. the main function in a program is the entry point - where the program starts running
- now we can run the code. Remember how we did it for hello world? We are going to do the same thing here. and you should see the board printed out
- now that we have the board and can print it out, let's add one more thing before we get to the game loop. let's add the check winner function
    - think about how we can check for a winner. what are the conditions for winning in tic tac toe?
        - full row
        - full column
        - full diagonal
    - let's write the check winner function to check each of these things. I am going to write the code and explain what is happening
        - check rows
        - check columns
        - check diagonals
- great! Now we have the game, we can print the board, and we can check if someone has won the game.
- Now we need to add the game loop. The game loop is the part of the program that runs the game. It repeats the steps of the game until the game is over. We signal that by adding a while True loop.
    - the loop is saying that while True is True, keep running the loop. True is always True, so this loop will run forever until the game is over
- first, we get the move from the player. we will ask for the row first and then the column
- next, we check if the move is valid. First we look at the actual inputs given to make sure they are between 1 and 3. Then we check if the cell is empty and the spot can be taken. once these pass, we can update the board. otherwise, we will ask the player to try again
- now we can check for a winner. if there is a winner, we print the winner and break out of the loop.
- now we can check for a tie. if the board is full and there is no winner, we print that it is a tie and break out of the loop
- if no one has won and there is no tie, we switch players to continue the loop
- now we can run the game and see how it works. try playing a game with your partner

## Part 5 - Hangman - Self Exploration
- if you hadn't had enough yet, the last challenge is going to be to build a hangman game. this is a more complex game than tic tac toe, but it is still a great exercise for practicing your programming skills
- I am going to give you some time to work on this on your own. I will be here to help if you get stuck, but I want you to try to figure it out on your own first