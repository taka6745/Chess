# Design Document for the text-based Chess portion for Sentinel 

## Tips for each other
The greatest line of python shell code in existence:
exec(open("filename").read())
You might have used this before but if not, once typing python3 in terminal to open the python shell, this line of code will somehow initialise the file "filename" in the shell and allow you to access the classes and function in the file. So for example. exec(open("sentinalChess.py").read()) would allow you to then create an instance of sentinalGame() and call its methods and access its class variables and everything which is so good for debugging issues.

## Overall Design
This is for the local version of chess stored on the Raspberry Pi Zero W that will handle every game to check moves / validate moves in order to send them to chess.com / LiChess.com And will be used for offline games. This will be used to make sure that if a move is illegal that the board notifies the player and moves the piece back (Possibly with a buzzer)

I grabbed these headers from GPT because it was easy

## File Architecture

We'll follow a Java type file system where each class needs to be in its own file, this is just to make everything easier to visualise and to change. We'll keep every file in the same folder and won't put python files in other folders, however if we have assets such as pictures or text files or something like that we can put them in a folder called assets.

We'll have a folder called logs where we can log games just in a text file with each move and possibly a score attached or information like "**VALID**" or something like that

we'll have a folder with a CSV of moves made in games played on chess.com this will be for testing all the rules of chess without having to play full games, it's important for, checks, checkmates, stalemates, stalemates due to pieces on the board, promotions, run out of time, en Passant, castling, these take time to do manually so why not just use chess.com games that take seconds to load in, and every move on the chess.com games will be legal so any errors will need to be looked into

we can have a seperate python file for helpful functions such as converting "A3" to the location in the array to make it cleaner call the file helper.py and use ``from helper import *``

## User Interface Design

We shouldn't print out the board in the terminal, just take input moves in a loop just for speed in future, and have a function that brings up the GUI to display what the board is looking like, when we either step through moves, looking at the GUI or run the game in seconds and if we're outputting the moves to the log, see where it failed. 

### Environment Variables 
> Setting them in CMD

It will be useful to use Environment Variables, if you've never used them before they're just variables that get stored by your computer and python can grab them. So we have a Environment Variable called "TESTING" and in the python code write 
`` if testing == True: gui(board_array)``
the way to set a Environment Variable in windows is 
``set NEWVAR=SOMETHING``  use NEWVAR as "testing" and SOMETHING as "True" or False depending. Write that in CMD, this should only last only in that terminal until you close that terminal, if you want it set globally use 
``setx NEWVAR SOMETHING`` in CMD
>Getting them from Python file

```
import os
os.getenv('NEWVAR')
```
make sure NEWVAR is in quotes 
## Testing and Quality Assurance
We'll have the chess games to test with and the GUI for assurance that everything is working fine, we can delay the input from the chess games and load the gui each move and watch to make sure everything is fine,


## Issue of storing objects in array
So doing a bit of looking, there is no way to save an object in an array and move it without deleting it and putting in a new one, and this is a problem because we cannot do this for every piece, say in the code
```
board = [    
[r", "n", "b", "q", "k", "b", "n", "r"],
[p", "p", "p", "p", "p", "p", "p", "p"],
[" ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " "],
["P", "P", "P", "P", "P", "P", "P", "P"],
["R", "N", "B", "Q", "K", "B", "N", "R"]
]
```
**and** **then**
```
board = [    
["r", "n", "b", "q", "k", "b", "n", "r"],
["p", "p", "p", "", "p", "p", "p", "p"],
[" ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", "p", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " ", " "],
["P", "P", "P", "P", "P", "P", "P", "P"],
["R", "N", "B", "Q", "K", "B", "N", "R"]
]
```
say we went about this by going ``board.pop[1[3]]`` to delete the object (and it wouldn't be a string it'd be called fifthBlackPawn or whatever when we declared it using ``fifthBlackPawn = Pawn("Black")`` 
so when we go to put it back into the array at ``board[3[3]]`` we can't go ``fifthBlackPawn = Pawn("Black")`` because we wouldn't know what to name the piece or what kind of object it was **HOWEVER** while writing this I found something called ``exec`` in python that does let you create lines of python from strings and here's an example
```
class Pawn:
  colour = "Black"
  
foo = "fifthBlackPawn"
colour = "Black"
exec(foo + " = Pawn")
print(fifthBlackPawn.colour)
```
and the response is ``Black``
so if we use this to change the board we can save information like what colour it was, what the name of the variable was and what object it was, this would mean we would need to make a new field in the piece's class that was called ``name`` so we could go ``temp_name = board[3[3]].name`` so we could use that as the variable name in ``exec``

and using ``fifthBlackPawn.__class__.__name__`` you should get back the name of the object ``Pawn`` as a string (Or convert it to a string) then we can save that the same way as before (as temp_object) and use it in ``exec``

## En Passant
We're using classes for each piece controlled by a superclass,
Each piece should have it's own moving function that has it's move set
the move set should be able to get cross checked with the min an max when checking it's legal (this is just where the piece must stop because it's the edge or taking a piece however taking a piece as a min/max only applies to Queens, Bishops, and Rooks.) the move set should be an attribute of the class
for pawns, we need to store if En Passant is possible, maybe just a variable in python with the current square that a pawn is able to move to for En Passant, like ``if move legal and piece landing on EN_PASSANT mark as legal and take`` and have EN_PASSANT be a variable with the location "E3" and have En Passant as a legal move in the move sets for pawns and if the square doesn't align just return invalid automatically, AFTER checking if it was a diagonal move and there was no piece on that square already

## Code Architecture 
All the classes will have there move sets and functions that validate them, returning valid or invalid
and in the main python file when passing 
```
move = input("Your move: ") # A1,A3
convert to array location
and figure out min and maxes
board[location[location]].move((1,0)(3,0),0,4,0,0)) # move(start,finish,negy,posy,negx,posx)
if move valid:
	(update the board)
elif move invalid
	(tell player and get another input)
	# when we have this set up to the actual machine this will do more, 
	# like pulling the piece back to it's original position 	
```
the negy is 0 because the pawn can't move backwards any spaces because there is a piece behind, posy is 4 because there is the other pawn on the other side 4 spaces away, and same go for the neg/pos x because pieces are next to it

we could rewrite this instead of dynamically saying you can move 4 spaces forward we could instead write it as you can move up to maximum 6th place on the board. depends what's easier to conceptualise especially when determining if it's moved to the edge

it's important to figure min and max in the main code because objects won't be able to get information from the board array because it's outside it's scope.
and even tho a pawn can't move back it's important we use all the mins because the same .move function will be used for all objects
and we'll need to check for check's and checkmates and stalemates every move
we could put a function after a move is made that calculates the min and max's again for x and y, and what piece is on the min and max / if there is a piece (if theres a max that isn't the edge of the board theres gonna be a piece and if it's the edge check the array)

using the min and max will strange for bishops but the min x will correlate to how far it can go diagonally, it just will need to be calculated differently 

and this way of using min and max's may be troublesome for the queen **UNLESS** we add another min/max to the move function

```
board[location[location]].move((1,0)(3,0),1,4,0,7,4,0,0,2) # move(start,finish,negy,posy,negx,posx,negleftdiag,negrightdiag,posleftdiag,posrightdiag)
```
and if we do it like this we don't have to worry about any problems when queens and bishops are around
and for knights it'll be irrelevant but for the values we can use the edge of the board bc pieces can't stop it, this is where using the space on the board rather than how many spaces you can move may be useful, and in the class's function we can get how many spaces you can move from current space - destination space = 4 spaces possible to move in the x direction or whatever so we can use it with the set moves

for the main code use a function to convert "A3" to [0[4]] put in helper.py using
``convert(move)``
returns array with INT's
``[0,4]``

for negx and negy... use a function and put in helper.py using (board being the array of the board so the function can loop through) 
``minMax(board,location)``
and return array with a bunch of Ints
``[,1,4,0,7,4,0,0,2]``

when writing the ``.move`` functions for the classes it may be easier to do the move and have it return ``True`` or ``False`` if the move is valid and possible and then having another function in helper.py that manipulates the array using
``movePiece(board,startLocation,endLocation)``
and have the return be the new array board so we can update the board in the main code
``board = movePiece(board,startLocation,endLocation)``
this'll be easier because you won't have to pass the board array to the class and will save writing the manipulating of the array in each class and keep the main code clean



### Each Move
each move return the board if TESTING is enabled so it can be passed to the gui
each move check for checks and checkmates and stalemates
