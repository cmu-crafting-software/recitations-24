# Recitation 4: classes, objects, and sets

__Wode "Nimo" Ni__

_22/02/11_

In this recitation, we'll continue with our wordle example. This time, we will:

* Provide a list of valid letters to the player.
* Build an automated player that plays the game 100 times.

## Concepts

* Sets
  * Unique members
  * Unordered
  * Set operations: union, difference etc
* Objects and classes
  * Examples:
    * https://docs.python.org/3/library/csv.html#csv.writer
    * https://docs.python-requests.org/en/latest/ 
  * Methods
  * State (aka "field")

```python
class Writer:
   row_count = 0
   file = ??
  # constructor
   def __init__(self, file):
     self.file = file
   def write_row(self):
     self.row_count += 1
writer1 = csv.Writer("egg.csv")
writer1.write_row(["egg", "price", "color"])
writer2 = csv.Writer("chicken.csv")
```

## Task 1: help the human players out

In the desktop version of wordle, the game shows you the characters on a colored keyboard, which is helpful for keeping track of the valid characters to use. Let's try to do that. 

* `play()` is the same old interactive mode we had. 
* It now has an argument that tells it to print out valid characters after each step (`char_hint`).
* Finish `valid_letters` to make it actually work.

## Task 2: play the wordle game programmatically

In addition to a collection of pure functions we wrote before, we now introduce the `WordleGame` __class__, which represents a single game of Wordle. Let's try using it first:

* Instantiate a `WordleGame` __object__ with a predefined answer `apple`.
* Guess 3 times, in which the final guess is `apple`.
* Print out the history of hints and if you indeed won the game using methods defined in the class.

## Task 3: play the wordle game programmatically, many times

If you can play the game once in a program, you can play it many times. 

* In `play_wordle_games`, create a loop that goes through `n` times
* In each step:
  * Instantiate a `WordleGame` __object__ without a predefined answer
  * Take 5 guesses
  * Print out the history
  * Record if we won
* Finally, compute the success rate of your first aRTiFicIAl iNTelLigeNCe.
