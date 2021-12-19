[![build](https://github.com/oboufous/correlatedpy/workflows/build/badge.svg)](https://github.com/oboufous/correlatedpy/actions?query=workflow%3Abuild)
[![Documentation Status](https://readthedocs.org/projects/correlatedpy/badge/?version=latest)](https://correlatedpy.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://img.shields.io/pypi/dm/correlatedpy)](https://pypi.org/project/correlatedpy/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/63847d9328f64fce9c137b03fcafcc27)](https://app.codacy.com/manual/oboufous/correlatedpy?utm_source=github.com&utm_medium=referral&utm_content=oboufous/correlatedpy&utm_campaign=Badge_Grade_Dashboard)
[![codecov](https://codecov.io/gh/oboufous/correlatedpy/branch/main/graph/badge.svg?token=RW0D49JQE0)](https://codecov.io/gh/oboufous/correlatedpy)
[![GitHub contributors](https://img.shields.io/github/contributors/oboufous/correlatedpy)](https://github.com/oboufous/correlatedpy/graphs/contributors)
[![Games](https://img.shields.io/github/search/oboufous/correlatedpy/import%20filename:*_env%20path:correlatedpy/games?label=games)](#the-games)

# Correlatedpy: a python library for distributed learning of correlated equilibrium in multiplayer strategic games.



  <p align="center">
    <a href="https://github.com/oboufous/correlatedpy">View Demo</a>
    ·
    <a href="https://github.com/oboufous/correlatedpy/issues">Report Bug</a>
    ·
    <a href="https://github.com/oboufous/correlatedpy/issues">Request Feature</a>
  </p>
</p>


The library implements a distributed learning algorithm allowing players to converge towards a correlated equilibrium point. 


## Installation

**Correlatedpy** has a small set of Python dependencies. It is straightforward to install on all operating systems as it only requires the following python packages

* [matplotlib](https://pypi.org/project/matplotlib/)
* [numpy](https://pypi.org/project/numpy/)
* [qe](https://pypi.org/project/qe/)

```bash
$ python -m pip install correlatedpy
```

To install Correlatepy on Fedora, use:

```sh
$ dnf install python3-correlatepy
```

## The Environment

### Parameters
The game has three global parameters that are shared accross all instances of all classes of the game. They can be initialized as follows

```python

history = [(0,0)] # history of action profiles played by players
epsilon = 0.02 # exploration rate
alpha = 0.01 # targetted approximate correlated equilibrium
```

### Players
the Player class has the attributes we list below:

* _number_: object instance unique identifier
* _payoff_: player's payoff matrix 
* _state_: player's state ('syn' or 'asyn')
* _history_: game history
* _epsilon_: exploration rate
* _alpha_: approximate correlated alpha-equilibrium

We can now create the players by setting a value for each one of the parameters.
```python

P1 = Player(number = 1, payoff = np.array([[0, 0], [1, -1]]), state = 'asyn', history = [(0, 0)], epsilon = 0.02, alpha = 0.01)
P2 = Player(number = 2, payoff = np.array([[0, 0], [-1, 1]]), state = 'asyn', history = [(0, 0)], epsilon = 0.02, alpha = 0.01)

```

### Game

After creating players, we can now instanciate a game, define how many rounds to play, and add the players to it.

```python
G = Game(iterations = 100000, history = [(0, 0)], epsilon = 0.02, alpha=0.01)

G.add_player(P1)
G.add_player(P2)

```

## Learning

The game is played repeatedly by calling the instance method _run()_.

```python
G.run()

```
### Simulation Results

```python
G.results()

```

## Diagram


## Examples of Games

See the [documentation](https://correlatedpy.readthedocs.io/en/latest/quickstart.html) for some examples and notebooks.

### [Chicken Game](https://en.wikipedia.org/wiki/Chicken_(game))

This game has two pure Nash equilibria and one mixed Nash equilibrium. 

<div align="center">
    
&nbsp; | <b>D</b> | <b>C</b>  
--- | --- | --- 
<b>D</b> | 0,0 | 7,2 
<b>C</b> | 2,7 | 6,6 

</div>

We show the evolution of the probabilities of play of each profile.


### [Rock-Paper-Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors)

This game has a unique mixed Nash equilibrium point. 

<div align="center">
    
&nbsp; | <b>R</b> | <b>P</b> | <b>S</b>  
--- | --- | --- | --- 
<b>R</b> | 0,0 | -1,1 | 1,-1
<b>P</b> | 1,-1 | 0,0 | -1,1
<b>S</b> | -1,1 | 1,-1 | 0,0

</div>

The simulation results show the probability of play of each profile. 


### A 3x2 game

This game has two mixed Nash equilibria. 

<div align="center">
    
&nbsp; | <b>X</b> | <b>Y</b>   
--- | --- | --- 
<b>A</b> | 2,29 | 16,7 
<b>B</b> | 4,7 | 6,13 
<b>C</b> | 4,4 | 6,6

</div>

We show the empirical distribution of play of each profile. 

### A three-player game


<div align="center">
<table>
<tr><th>X </th><th>Y</th></tr>
<tr><td>

|&nbsp;| <b>C</b> | <b>D</b> |
|--|--|--|
|<b>A</b>| 0,0,0 | 0,0,0 |
|<b>B</b>| 0,0,0 | 0,0,0 |
</td><td>

|&nbsp;|<b>C</b>|<b>D</b>|
|--|--|--|
|<b>A</b>| 0,0,0 | 0,0,0 |
|<b>B</b>| 0,0,0 | 0,0,0|
</td></tr> </table>
</div>

## Usage

<!--alex ignore bi-->

### Payoff matrices 

For an n-player game with action spaces of size <img src="https://render.githubusercontent.com/render/math?math=m_{i} = |\mathcal{A}_i| \forall i \in \mathcal{N}">, a payoff matrix of size <img src="https://render.githubusercontent.com/render/math?math=\prod_{i \in \mathcal{N}}m_{i}"> needs to be created for each player. 

Creating the payoff matrice for player i can be performed in the following manner:

```python
>>> import correlatedpy as correlated
>>> game = correlated.Game(iterations = 100000, history = [(0, 0)], epsilon = 0.02, alpha=0.01)
>>> u1 [[1, 2], [3, 0]]
>>> u2 [[0, 2], [3, 1]]
>>> P1 = correlated.Player(number = 1 payoff = u1 state = 'asyn', history = [(0, 0)], epsilon = 0.02, alpha = 0.01)
>>> P2 = correlated.Player(number = 2 payoff = u2 state = 'asyn', history = [(0, 0)], epsilon = 0.02, alpha = 0.01)
>>> game.add_player(P1)
>>> game.add_player(P2)
>>> game.run()
>>> game.results()
```
## Documentation

Full documentation is available here: http://correlatedpy.readthedocs.io/

## Citing

If you use the project in your work, please consider citing it with:
```bibtex
@misc{correlatedpy,
  author = {Boufous, Omar},
  title = {Correlatedpy: a python library for distributed learning of correlated equilibrium in multiplayer strategic games.},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/oboufous/correlatedpy}},
}
```
## Other game theoretic software

- [Nashpy](http://www.gambit-project.org/) is a python library for the computation of equilibria of 2 player strategic games.
- [Gambit](http://www.gambit-project.org/) is a library with a python api and support for more algorithms and more than 2 player games.
- [Game theory explorer](http://gte.csc.liv.ac.uk/index/) is a web interface to gambit useful for teaching.
- [Axelrod](http://axelrod.readthedocs.io/en/stable/) is a research library aimed at the study of the Iterated Prisoners dilemma.


## Development

Clone the repository and create a virtual environment:

```bash
$ git clone https://github.com/oboufous/correlatedpy.git
$ cd correlatedpy
$ python -m venv env

```

Activate the virtual environment and install [`tox`](https://tox.readthedocs.io/en/latest/):

```bash
$ source env/bin/activate
$ python -m pip install tox

```

Make modifications.

To run the tests:

```bash
$ python -m tox

```

To build the documentation. First install the software which also installs the
documentation build requirements.

```bash
$ python -m pip install flit
$ python -m flit install --symlink
```

Then:

```bash
$ cd docs
$ make html
```

Full contribution documentation is available at
https://correlatedpy.readthedocs.io/en/latest/contributing/index.html 

Pull requests are welcome.

## Code of conduct

In the interest of fostering an open and welcoming environment, all
contributors, maintainers and users are expected to abide by the Python code of
conduct: https://www.python.org/psf/codeofconduct/
