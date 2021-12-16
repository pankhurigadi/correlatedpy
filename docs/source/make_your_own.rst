.. _make_your_own:

Make your own game
==========================

Here are the steps required to create a new game.

.. note::
    Pull requests are welcome!

Set up files
------------

1. Create a new ``your_game.py`` file in ``correlatedpy/games/``
2. Define a class YourGame, that must inherit from :py:class:`~correlatedpy.games.common.abstract.AbstractEnv`

This class provides several useful functions:

* A :py:meth:`~correlatedpy.envs.common.abstract.AbstractEnv.default_config` method, that provides a default configuration dictionary that can be overloaded.
* A :py:meth:`~correlatedpy.envs.common.abstract.AbstractEnv.define_spaces` method, that gives access to a choice of observation and action types, set from the game configuration
* A :py:meth:`~correlatedpy.envs.common.abstract.AbstractEnv.step` method, which executes the desired actions (at policy frequency) and simulate the environment (at simulation frequency)
* A :py:meth:`~correlatedpy.envs.common.abstract.AbstractEnv.render` method, which renders the game.

Create the Players
------------------

The first step is to create a :py:class:`~correlatedpy.player.player.Player` that describes the players in the game.
This should be achieved in a ``YourGame._make_player()`` method, called from ``YourGame.reset()`` to set the ``self.Player`` field.

See :ref:`Players <player_player>` for reference, and existing games as examples.

Create the vehicles
------------------

The second step is to populate your road network with vehicles. This should be achieved in a ``YourEnv._make_road()``
method, called from ``YourEnv.reset()`` to set the ``self.road.vehicles`` list of :py:class:`~highway_env.vehicle.kinematics.Vehicle`.

First, define the controlled ego-vehicle by setting ``self.vehicle``. The class of controlled vehicle depends on the
choice of action type, and can be accessed as ``self.action_type.vehicle_class``.
Other vehicles can be created more freely, and added to the ``self.road.vehicles`` list.

See :ref:`vehicle behaviors <vehicle_behavior>` for reference, and existing environments as examples.

Make the game configurable
------------------------------------

To make a part of your environment configurable, overload the :py:meth:`~highway_env.envs.common.abstract.AbstractEnv.default_config`
method to define new ``{"config_key": value}`` pairs with default values. These configurations then be accessed in your
environment implementation with ``self.config["config_key"]``, and once the environment is created, it can be configured with
``env.configure({"config_key": other_value})`` followed by ``env.reset()``.

Register the game
---------------------------

In ``correlatepy/games/your_game.py``, add the following line:

.. code-block:: python

    #register(
        id='your-game-v0',
        entry_point='correlatedpy.games:YourGame',
    )

and import it from ``correlatedpy/games/__init__.py``:

.. code-block:: python

    #from correlatedpy.games.your_game import *


Profit
--------
That's it!
You should now be able to run the environment:

.. code-block:: python

    #import gym
    #import highway_env

    #env = gym.make('your-env-v0')
    #obs = env.reset()
    #obs, reward, done, info = env.step(env.action_space.sample())
    #env.render()

API
-------


.. automodule:: highway_env.envs.common.abstract
    :members:
    :private-members:

