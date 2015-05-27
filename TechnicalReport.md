COMP3330 - Machine Intelligence - HW2 Technical Report
======================================================

* Beau Gibson - C3146845
* Tyler Haigh - C3182929
* Simon Hartcher - C3185790
* Rob Logan - C3165020

# Task #

# System Overview #

# Question 1 - Intelligent Agents Literature Review and Discussion #

## 2048 Artificial Intelligence Implementations ##

For the purposes of this task, a number of implementations of agents for the 2048 game were reviewed and
considered. These implementations used a range of approaches, heuristics and algorithms to train their agents in
recognising the best possible move for a particular board layout at a given point in the game. For this review, 
we have concentrated on and compared the main goals these agents were given and the types of heuristic approaches
which were assigned to reach a conclusion about the positions themselves.
     
### Approach Comparison ###

Thes algorithms of Minimax and Alph-Beta Pruning provide a strong base for the evaluation of two player games. 
They are often utilised by AI in games of Chess, Checkers, Tic-Tac-Toe and other similar games. Even in the 
case of 2048 which on the surface is a one (or zero) player game, these approaches can be applied by visualising 
the player as trying to "maximise" their score or position and the pseudo-random placement of new tiles by the 
program as "minimising". 

Thus for Minimax, the AI's observed would scan the current state of the board and make a decision based on the best 
possible score looking ahead. Even given the fixed number of moves at any given state in the game (up, down, left, right), 
the AI's were faced with an ever-expanding tree of possibilities, the deeper it would search. So a depth of 5 would take 
approximately 1 second, whereas a depth of 7 ply would last up to 30 seconds. This search time was reduced with the use
of Alpha-Beta Pruning, which would significantly reduce the number of nodes to evaluate.The deeper the search though, the 
greater the accuracy, with the deeper searched yielding a 70-80% chance of winning compared to a 3 ply search (20% chance).

### Heuristics ###

In implementing any approach to game solving, an AI must use some heuristics or measurable results in order to evaluate a 
given position in the game state and decide upon a course of action. The 2048 implementations observed used a variety of
heuristics and there is much debate in the development community around which approaches and calculations are best.

Most implementations for the 2048 game use some variation of the actual score on the board at the time. This is often
combined with a calculation of the number of empty tiles on the board (more empty tiles = more likely favourable move 
options). In addition to these calculations, one approach studied used a what was called a "clustering score", which 
returned a figure base on how close or separated values were from each other. This clustering score was calulated for 
each tile from the average of the differences between surrounding tiles. Thus when similar values are clustered, this 
is a favourable position resulting in a lower clustering score and less of a "penalty" to the heuristic calculation. 
An example of a low clustering score can be seen in the position below.

<table>
  <tr>
    <td>8</td>
    <td>16</td> 
    <td>4</td>
  </tr>
  <tr>
    <td>6</td>
    <td>8</td> 
    <td>2</td>
  </tr>
    <tr>
    <td>0</td>
    <td>4</td> 
    <td>0</td>
  </tr>
</table>  

Other heuristics examined include:
 
* **Monotonicity** - involves the AI trying to "ensure that the values of the tiles are all either increasing or decreasing 
along both the left/right and up/down directions" [(Stack Overflow, 2014)](http://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048/22389702#22389702)

* **Weighting Matrix** - creation of a matrix the same size as the board state with higher weightings towards one corner and lower
 diagonally opposite. This tends to force the AI to push larger tiles towards the higher weights and smaller tiles towards the
 lower weights. [(Yiyuan,2014)](https://codemyroad.wordpress.com/2014/05/14/2048-ai-the-intelligent-bot/)  An example can be seen below:  

![Weights](https://s0.wp.com/latex.php?latex=%5Cmathbf%7BW%7D+%3D+%5Cleft%28%5Cbegin%7Bmatrix%7D7%266%265%264%5C%5C6%265%264%263%5C%5C5%264%263%262%5C%5C4%263%262%261%5Cend%7Bmatrix%7D%5Cright%29&bg=ffffff&fg=000&s=0 "Weight Matrix")

These heuristics attempt to mimic the way that a human player would view the board and make value based judgements about
it's state. The judgements allow the AI to look forward during a depth limited search to find the optimum move at any
given point of the game.
      
## Similar Game Implementations ##

It was noted that algorithms such as Minimax, Expectimax and Alpha-Beta Pruning have been used to good effect in many two
player games such as chess, checkers, tic-tac-toe, connect four, etc. These two-player games lend themselves well to 
depth-limited game tree searches and minimising/maximising comparisons. As stated earlier, although 2048 and it's variants
are ostensibly single player games, the placing of new tiles by the program can be seen have a minimising effect on the player.
This is still the case even given the fact that the placement and selection of new tiles (2 or 4) is randomly decided (a two
is placed 90% of the time whereas a four is placed 10% of the time).

Where these algorithms do not necessarily carry weight is in the single-player game space. Games like, Sudoku, crosswords 
and tile puzzles, tend to lend themselves more to search algorithms. Brute force searches such as depth-first, bredth-first
or iterative deepening search all possible avenues. Smarter heuristic searches such as A*, attempt to use a smarter
approach wich is generally faster. Further, local searches such as Hillclimb take an iterative approach, finding a best
local maximum and moving forward.

# Question 2 - 65536 AI #

`TODO`

* Develop 2 solutions to solve 65536. Use techniques covered in lectures
* Clear description of learning or search algorithms (1 mark)
* Discussion of tuning process and developing appropriate representations of environment (1 Mark)
* Explanation of features of problem which make solution appropriate (1 Mark)
* High Level pseudocode of changes to standard algorithms
* Two working agents with execute instructions (3 Marks)
* Conduct comparison of agents and report and discuss their outcome


# References #
1. Nicola Pezzotti, *An Artificial Intelligence for the 2048 Game*, [http://diaryofatinker.blogspot.it/2014/03/an-artificial-intelligence-for-2048-game.html],
Diary of a Tinker, 2014
2. Lee Yiyuan, *2048 AI - The Intelligent Bot*, [https://codemyroad.wordpress.com/2014/05/14/2048-ai-the-intelligent-bot/],
Code My Road, 2014
3. Philip Rodgers & John Levine, *An Investigation into 2048 AI Strategies*, [http://kghost.de/cig_proc/aux/paper_106.pdf],
University of Strathclyde, 2014
4. Vasilis Vryniotis, *Using Artificial Intelligence to Solve The 2048 Game*, [http://blog.datumbox.com/using-artificial-intelligence-to-solve-the-2048-game-java-code/],
DatumBox, 2014
5. Various Contributors, *What is the optimal algorithm for the game 2048?*, [http://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048],
StackOverflow, 2015