[![build](https://github.com/oboufous/correlatedpy/workflows/build/badge.svg)](https://github.com/oboufous/correlatedpy/actions?query=workflow%3Abuild)
[![Documentation Status](https://readthedocs.org/projects/correlatedpy/badge/?version=latest)](https://correlatedpy.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://img.shields.io/pypi/dm/correlatedpy)](https://pypi.org/project/correlatedpy/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/63847d9328f64fce9c137b03fcafcc27)](https://app.codacy.com/manual/oboufous/correlatedpy?utm_source=github.com&utm_medium=referral&utm_content=oboufous/correlatedpy&utm_campaign=Badge_Grade_Dashboard)
[![Coverage](https://codecov.io/gh/oboufous/correlatedpy/branch/master/graph/badge.svg)](https://codecov.io/gh/oboufous/correlatepy)
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


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">The Environment</a></li>
        <li><a href="#installation">Execution</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


The library implements a distributed learning algorithm allowing players to converge towards a correlated equilibrium point. 

**Correlatedpy** has a small set of Python dependencies. It is straightforward to install on all operating systems as it only requires the following python packages

* [matplotlib](https://pypi.org/project/matplotlib/)
* [numpy](https://pypi.org/project/numpy/)
* [qe](https://pypi.org/project/qe/)


## The Environment

### Parameters
The game has global parameters that are shared accross all instances of all classes of the game.

```python

history = [(0,0)]
gamma = 1
epsilon = 0.02 
alpha = 0.01
```

### Players

```python

P1 = Player(number = 1, actions = [0, 1], payoff = np.array([[0, 0], [1, -1]]), state = 'asyn', history = [(0, 0)], gamma = 1, epsilon = 0.02, alpha = 0.01)
P2 = Player(number = 2, actions = [0, 1], payoff = np.array([[0, 0], [-1, 1]]), state = 'asyn', history = [(0, 0)], gamma = 1, epsilon = 0.02, alpha = 0.01)

```

In this task, the ego-vehicle is driving on a multilane highway populated with other vehicles.
The agent's objective is to reach a high speed while avoiding collisions with neighbouring vehicles. Driving on the right side of the road is also rewarded.

A faster variant, `highway-fast-v0` is also available, with a degraded simulation accuracy to improve speed for large-scale training.

### Game

After creating players, we can now instanciate a game, define how many rounds to play, and add the players to it.

```python
T = 100000

G = Game(iterations = 100000, history = [(0, 0)], gamma = 1, epsilon = 0.02, alpha=0.01)

G.add_player(P1)
G.add_player(P2)

```

In this task, the ego-vehicle starts on a main highway but soon approaches a road junction with incoming vehicles on the access ramp. The agent's objective is now to maintain a high speed while making room for the vehicles so that they can safely merge in the traffic.

## Examples of Games

See the [documentation](https://correlatedpy.readthedocs.io/en/latest/quickstart.html) for some examples and notebooks.

### [Chicken Game](https://en.wikipedia.org/wiki/Chicken_(game))


<div align="center">
    
&nbsp; | <b>D</b> | <b>C</b>  
--- | --- | --- 
<b>D</b> | 0,0 | 7,2 
<b>C</b> | 2,7 | 6,6 

</div>

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/ddpg.gif?raw=true"><br/>
    <em>The DDPG agent solving parking-v0.</em>
</p>

This model-free value-based reinforcement learning agent performs Q-learning with function approximation, using a neural network to represent the state-action value function Q.

### [Rock-Paper-Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors)


<div align="center">
    
&nbsp; | <b>R</b> | <b>P</b> | <b>S</b>  
--- | --- | --- | --- 
<b>R</b> | 0,0 | -1,1 | 1,-1
<b>P</b> | 1,-1 | 0,0 | -1,1
<b>S</b> | -1,1 | 1,-1 | 0,0

</div>

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/ddpg.gif?raw=true"><br/>
    <em>The DDPG agent solving parking-v0.</em>
</p>

This model-free policy-based reinforcement learning agent is optimized directly by gradient ascent. It uses Hindsight Experience Replay to efficiently learn how to solve a goal-conditioned task.


### A 3x2 game

<div align="center">
    
&nbsp; | <b>X</b> | <b>Y</b>   
--- | --- | --- 
<b>A</b> | 2,29 | 16,7 
<b>B</b> | 4,7 | 6,13 
<b>C</b> | 4,4 | 6,6

</div>

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/ddpg.gif?raw=true"><br/>
    <em>The DDPG agent solving parking-v0.</em>
</p>

This model-free policy-based reinforcement learning agent is optimized directly by gradient ascent. It uses Hindsight Experience Replay to efficiently learn how to solve a goal-conditioned task.

## Installation

```bash
$ python -m pip install correlatedpy
```

To install Correlatepy on Fedora, use:

```sh
$ dnf install python3-correlatepy
```

## Usage

<!--alex ignore bi-->

Create bi matrix games by passing two 2 dimensional arrays/lists:

```python
>>> import correlatedpy as correlated
>>> A = [[1, 2], [3, 0]]
>>> B = [[0, 2], [3, 1]]
>>> game = correlated.Game(A, B)
>>> for eq in game.support_enumeration():
...     print(eq)
(array([1., 0.]), array([0., 1.]))
(array([0., 1.]), array([1., 0.]))
(array([0.5, 0.5]), array([0.5, 0.5]))
>>> game[[0, 1], [1, 0]]
array([3, 3])

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
