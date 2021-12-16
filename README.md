[![build](https://github.com/oboufous/correlatedpy/workflows/build/badge.svg)](https://github.com/oboufous/correlatedpy/actions?query=workflow%3Abuild)
[![Documentation Status](https://readthedocs.org/projects/correlatedpy/badge/?version=latest)](https://correlatedpy.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://img.shields.io/pypi/dm/correlatedpy)](https://pypi.org/project/correlatedpy/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/63847d9328f64fce9c137b03fcafcc27)](https://app.codacy.com/manual/oboufous/correlatedpy?utm_source=github.com&utm_medium=referral&utm_content=oboufous/correlatedpy&utm_campaign=Badge_Grade_Dashboard)
[![Coverage](https://codecov.io/gh/oboufous/correlatedpy/branch/master/graph/badge.svg)](https://codecov.io/gh/oboufous/correlatepy)
[![GitHub contributors](https://img.shields.io/github/contributors/oboufous/correlatedpy)](https://github.com/oboufous/correlatedpy/graphs/contributors)
[![Games](https://img.shields.io/github/search/oboufous/correlatedpy/import%20filename:*_env%20path:correlatedpy/envs?label=environments)](#the-environments)

# Correlatedpy: a python library for distributed learning of correlated equilibrium in multiplayer strategic games.

The library implements a distributed learning algorithm allowing players to converge towards a correlated equilibrium point. 

**Correlatedpy** has a small set of Python dependencies. It is straightforward to install on all operating systems as it only requires the following python packages

* [matplotlib](https://pypi.org/project/matplotlib/)
* [numpy](https://pypi.org/project/numpy/)
* [qe](https://pypi.org/project/qe/)


## The environments

### Highway

```python
env = gym.make("highway-v0")
```

In this task, the ego-vehicle is driving on a multilane highway populated with other vehicles.
The agent's objective is to reach a high speed while avoiding collisions with neighbouring vehicles. Driving on the right side of the road is also rewarded.

A faster variant, `highway-fast-v0` is also available, with a degraded simulation accuracy to improve speed for large-scale training.

### Merge

```python
env = gym.make("merge-v0")
```

In this task, the ego-vehicle starts on a main highway but soon approaches a road junction with incoming vehicles on the access ramp. The agent's objective is now to maintain a high speed while making room for the vehicles so that they can safely merge in the traffic.

### Roundabout

```python
env = gym.make("roundabout-v0")
```

In this task, the ego-vehicle if approaching a roundabout with flowing traffic. It will follow its planned route automatically, but has to handle lane changes and longitudinal control to pass the roundabout as fast as possible while avoiding collisions.

### Parking

```python
env = gym.make("parking-v0")
```

A goal-conditioned continuous control task in which the ego-vehicle must park in a given space with the appropriate heading.


### Intersection

```python
env = gym.make("intersection-v0")
```

An intersection negotiation task with dense traffic.

### Racetrack

```python
env = gym.make("racetrack-v0")
```

A continuous control task involving lane-keeping and obstacle avoidance.

## Examples of agents

Agents solving the `highway-env` environments are available in the [eleurent/rl-agents](https://github.com/eleurent/rl-agents) and [DLR-RM/stable-baselines3](https://github.com/DLR-RM/stable-baselines3) repositories.

See the [documentation](https://highway-env.readthedocs.io/en/latest/quickstart.html#training-an-agent) for some examples and notebooks.

### [Deep Q-Network](https://github.com/eleurent/rl-agents/tree/master/rl_agents/agents/deep_q_network)

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/dqn.gif?raw=true"><br/>
    <em>The DQN agent solving highway-v0.</em>
</p>

This model-free value-based reinforcement learning agent performs Q-learning with function approximation, using a neural network to represent the state-action value function Q.

### [Deep Deterministic Policy Gradient](https://github.com/openai/baselines/tree/master/baselines/her)

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/ddpg.gif?raw=true"><br/>
    <em>The DDPG agent solving parking-v0.</em>
</p>

This model-free policy-based reinforcement learning agent is optimized directly by gradient ascent. It uses Hindsight Experience Replay to efficiently learn how to solve a goal-conditioned task.

### [Value Iteration](https://github.com/eleurent/rl-agents/blob/master/rl_agents/agents/dynamic_programming/value_iteration.py)

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/ttcvi.gif?raw=true"><br/>
    <em>The Value Iteration agent solving highway-v0.</em>
</p>

The Value Iteration is only compatible with finite discrete MDPs, so the environment is first approximated by a [finite-mdp environment](https://github.com/eleurent/finite-mdp) using `env.to_finite_mdp()`. This simplified state representation describes the nearby traffic in terms of predicted Time-To-Collision (TTC) on each lane of the road. The transition model is simplistic and assumes that each vehicle will keep driving at a constant speed without changing lanes. This model bias can be a source of mistakes.

The agent then performs a Value Iteration to compute the corresponding optimal state-value function.

### [Monte-Carlo Tree Search](https://github.com/eleurent/rl-agents/blob/master/rl_agents/agents/tree_search/mcts.py)

This agent leverages a transition and reward models to perform a stochastic tree search [(Coulom, 2006)](https://hal.inria.fr/inria-00116992/document) of the optimal trajectory. No particular assumption is required on the state representation or transition model.

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/mcts.gif?raw=true"><br/>
    <em>The MCTS agent solving highway-v0.</em>
</p>



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
