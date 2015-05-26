COMP3330 - Machine Intelligence - HW2 Technical Report
======================================================

* Beau Gibson - C3146845
* Tyler Haigh - C3182929
* Simon Hartcher - C3185790
* Rob Logan - C3165020

# Task #

# System Overview #

# Question 1 - Intelligent Agents Literature Review and Discussion #

`TODO - Heuristics analysis and `

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
`TODO - Ways to evaluate a position in addition to raw score`

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

     8  16 4
    16  8  2
     0  4  0

Other heuristics examined include:
 
* Monotonicity - involves the AI trying to "ensure that the values of the tiles are all either increasing or decreasing 
along both the left/right and up/down directions" [(Stack Overflow)](http://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048/22389702#22389702)

        
## Similar Game Implementations ##
`TODO - Checkers, etc`

# Question 2 - 65536 AI #

`TODO`

* Develop 2 solutions to solve 65536. Use techniques covered in lectures
* Clear description of learning or search algorithms (1 mark)
* Discussion of tuning process and developing appropriate representations of environment (1 Mark)
* Explanation of features of problem which make solution appropriate (1 Mark)
* High Level pseudocode of changes to standard algorithms
* Two working agents with execute instructions (3 Marks)
* Conduct comparison of agents and report and discuss their outcome
