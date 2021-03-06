Tutorial: building and finding the equilibrium for  a game
==========================================================

Introduction to game theory
---------------------------

Game theory is the study of strategic interactions between rational agents.
This means that it is the study of interactions when the involved parties try and do what is best from their point of view.

As an example let us consider `Rock Paper Scissors <https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors>`_. This is a common game where two players choose one of 3 options (in game theory we call these *strategies*):

- Rock
- Paper
- Scissors

The winner is decided according to the following:

- Rock crushes scissors
- Paper covers Rock
- Scissors cuts paper


We can represent this mathematically using a 3 by 3 matrix:

+------+------+------+------+
| X    |    R |    P |    S |
+======+======+======+======+
| R    |  0,0 | -1,1 | 1,-1 |
+------+------+------+------+
| P    | 1,-1 | 0,0  | -1,1 |
+------+------+------+------+
| S    | -1,1 | 1,-1 | 0,0  |
+------+------+------+------+

The matrix shows the utility to the player controlling the rows when they play the XXX  and their opponent (the column player) plays the YYY column. For example, if the row player played Scissors (the 3rd strategy) and the column player played Paper (the 2nd strategy) then the row player gets 1 because Scissors cuts Paper.


A recommend text book on Game Theory is [Maschler2013].

Installing CorrelatedPy
-----------------

We are going to study this game using correlatedpy, first though we need to install it. CorrelatedPy requires the following things to be on your computer:

- Python 3.5 or greater;
- `matplotlib <https://pypi.org/project/matplotlib/>`_
- `numpy <https://pypi.org/project/numpy/>`_
- `qe <https://pypi.org/project/qe/>`_
- `tqdm <https://pypi.org/project/tqdm/>`_    

Assuming you have those installed, to install correlatepy:

- On Mac OSX or linux open a terminal;
- On Windows open the Command prompt or similar

and type::

    $ python -m pip install correlatedpy

If this does not work, you might not have Python or one of the other dependencies. You might also have problems due to :code:`pip` not being recognised. To overcome these, using the `Anaconda <https://www.continuum.io/downloads>`_ distribution of Python is recommended as it installs straightforwardly on all operating systems and also includes the libraries needed to run :code:`correlatedpy`.

Creating a game
---------------

We can create the Rock-Paper-Scissors game using Correlatedpy::

    >>> import correlatedpy 
    >>> import numpy as np
    >>> u1 = np.array([[0, -1, 1],
                [1, 0, -1],
                [-1, 1, 0]])
    >>> u2 = np.array([[0, 1, 1],
                [-1, 0, 1],
                [1, -1, 0]])
    >>> P1 = Player(number = 1, payoff = u1, history = [(0, 0)], epsilon = 0.02)
    >>> P2 = Player(number = 2, payoff = u2, history = [(0, 0)], epsilon = 0.02)
    >>> G = Game(history = [(0, 0)], epsilon = 0.02)
    >>> G.add_player(P1)
    >>> G.add_player(P2)


Learning in games
-----------------

Computing a correlatd equilibrium is not possible when the game parameters are not fully known to all players. Therefore, we resort to learning
a *correlated* equilibria is an important concept as it allows to gain an initial understanding of emergent behaviour in complex systems, similarly to Nash equilibrium.

A correalted equilibrium corresponds to strategies at which no play has an incentive to move but that does not necessarily imply that players can arrive at that equilibria naturally.

Over time we can see a rational behaviour emerge, as players implements certain heurstics (regret minimisation in our case). Note that a regret minimizing strategy guarantees convergence only to the *set* of correlated equilibria.


    >>> G.runGame() 
    >>> G.getResults()
    
