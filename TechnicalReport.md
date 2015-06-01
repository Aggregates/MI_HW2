COMP3330 - Machine Intelligence - HW2 Technical Report
======================================================

* Beau Gibson - C3146845
* Tyler Haigh - C3182929
* Simon Hartcher - C3185790
* Rob Logan - C3165020

# Question 1 - Intelligent Agents Literature Review and Discussion #

## 2048 Artificial Intelligence Implementations ##

For the purposes of this task, a number of implementations of agents for the 2048 game were reviewed and
considered. These implementations used a range of approaches, heuristics and algorithms to train their agents in
recognising the best possible move for a particular board layout at a given point in the game. For this review, 
we have concentrated on and compared the main goals these agents were given and the types of heuristic approaches
which were assigned to reach a conclusion about the positions themselves.
     
### Approach Comparison ###

These algorithms of Minimax and Alph-Beta Pruning provide a strong base for the evaluation of two player games. 
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

|:--:|:--:|:--:|
| 8 | 16 | 4 |  
| 6 | 8  | 2 |  
| 0 | 4  | 0 |  

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
or iterative deepening search all possible avenues. Heuristic searches such as A*, attempt to use a smarter approach 
which is also generally faster. Further, local searches such as Hillclimb take an iterative approach, finding a best
local maximum and moving forward incrementally.

Though the AI for these games is modelled upon a two-player game, the limited options for the "opponent" (the minimising 
value) mean that there is very little difference between the min and max states. Unlike games such as checkers, chess or
even tic-tac-toe, it would be impossible to utilise something like a transposition table (where game states are "remembered" and looked-up 
rather than calculated anew each time). 

# Question 2 - 65536 AI #

## Explanation Of The Problem ##

The majority of standard AI solution in place for the 2048 version of the game have been discussed in question 1. These
approaches generally tend to model the game play strategies of human players of the game, such as ordering tiles in
anticipation of a future merge or ensuring large valued tiles are kept towards the edge of the game space. It was observed 
that these approaches worked well for 2048, though not necessarily for this larger form of the game. Even with its smaller 
board dimensions (4x4 as opposed to 5x5), the reward or penalty for a less than optimal move is minimised due to the shorter 
overall runtime of the game. In our implementation it was found that bad decisions early on could be magnified once the 
end-game period approached.

In implementing an appropriate solution for the AI to solve the game, it was necessary to focus on two main problems.  
1. Provide some means for the AI to assess a "good" or "bad" position after a move.  
2. Trade off between the speed of the algorithm and its efficiency. This is managed through the depth variable which guides
the AI in how far into the future to look for an optimal solution.  

As discussed when examining previous implementations and solutions, this game lends itself well to modelling as a two-player, 
adversarial game. That being the case, it is most appropriate to use depth search algorithms such as Minimax or Alpha-Beta.
By specifying the depth at the beginning of the search, we can limit how long the AI spends on looking for an answer. By 
contrast, using a Monte Carlo approach, the AI uses a specific number of games (which can be altered by the programmer) 
to effectively try a "brute force" randomised approach to the games. Random moves are attempted for each position 

## Learning and Search Algorithm Pseudocode ##

This section will show pseudocode of the various algorithms used by the agents. The general structure of these algorithms
can be found in various implementations and has also been derived from information in lectures.

### Minimax ###
Treats the game as a two-player adversarial game rather than a one-player puzzle. The max player chooses the best option
to maximise it's score, whereas the min player attempts to place a 2 or 4 in the "worst" position available. This
implementation was found to be too slow to produce any meaningful results.

    def minimax(game, depth, player)
        if depth==0 or game.over
            bestscore = heuristic value of game position
        else
            if player==max
                bestscore = smallest negative number
                newboard = copy board position
                for each possible move
                    currentdirection, currentscore = minimax(newboard, depth-1, min)
                    if currentscore>bestscore
                        bestscore = currentscore
                        bestdirection = move
            else
                bestscore = largest positive number
                newboard = copy board position
                for each available cell in newboard
                    add a new tile (2 or 4)
                    currentdirection, currentscore = minimax(newboard, depth-1, max)
                    if currentscore<bestscore
                        bestscore = currentscore
        
        return bestdirection, bestscore
 
### Minimax with Alpha-Beta Pruning ###
This search algorithm combines the heuristic calculation of a particular game position with alpha-beta pruning top improve
search time in discarding the nodes which will not produce a valid result within the bounds. The alpha and beta bounds are
gradually reduced by examining the heuristic value of the game position at the given depth of the game tree. Obviously a 
greater depth requires more searches and therefore takes longer. A balance must be found between performance and accuracy.
    
    def alphabetarecurs(node, depth, max depth, alpha, beta)
        if depth=0 or node is terminal:
            return heuristic value of game position
        
        if player = max:
            for each child of node:
                alpha = max(alpha, alphabeta(child, depth-1, alpha, beta)
                
                if beta <= alpha:
                    break
            return alpha
        else:
            for each child of node:
                beta = min(beta, alphabeta(child, depth-1, alpha, beta)

                if beta <= alpha:
                    break
            return beta

### Monte Carlo ###
This approach used in this algorithm uses random sampling of moves in order to decide on the best overall approach each.
The AI plays a certain number of games for each opening option (as passed in my the programmer) from the current state.
Moves are then randomly selected and the game played to completion. After all games have been played, the best final scores 
are compared and the opening move with the best final score is passed back to the move function. This is then repeated 
 for each move of the game.  

    def montecarlo(game, numberOfGames)
        for each possible move
            play numberOfGames to completion with random moves and append to list
            
        select bestOutcome from all results
        select the opening move that produced the bestOutcome
    return move
 
### Randomiser ###
This is a simple method which merely uses Python's inbuilt random number generator to choose a direction in which to move.
This method was created as a baseline with little expectation of any real success. Indeed, the Randomiser was only able to
consistently achieve scores of around 256 or 512 and only occasionally reaching the 1024 or 2048 tile.

## Tuning Options Applied to Algorithms ## 


## Comparison of Agents ##
`TODO * Conduct comparison of agents and report and discuss their outcome`


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