.. _faq:

=============================
Frequently Asked Questions
=============================


This is a list of Frequently Asked Questions about correlatedpy. Feel free to suggest new entries!

My algorithm does not converge. Why?
    The convergence of the algorithm is guaranteed (see proof in the author's paper). Indeed, for any game you define, there exist at least a correlated equilibrium point, and the expected behaviour of the algorithm is to converege towards it.
    In :cite:`Leurent2019social`, we argued that a possible reason could either be a high exploration rate that does not allow the algorithm to remain at the equilibrium long enough, or a small time horizon. Indeed, a suffcient number of game rounds must be played in order to reach a steady state regime.
    This can be addressed in two ways:

    - Decrease the exploration/experimentation rate *epsilon*, to use a small perturbation, see *e.g.* :cite:`Qi2017pointnet` or :cite:`Leurent2019social` for examples.

    - Increase the time horizon or number of iterations. A rule of thumb is to play no less than :math:`\frac{2 \times |\max_{a, i}u_i(a)|}{\varepsilon^2}` game rounds.

The algorithm is too slow. It takes over 20 hours to terminate for a 3-player game over 10 hours to complete 150000 rounds.
    This is not surprising. In fact, the main reason is the size of the lists that keeps increasing with time, and the time consuming oprations performed at each iteration, namely a search of elements in the increasingly large lists.
    
.. code-block:: python

  #import gym
  #import highway_env

  # Wrap the env by a Monitor, which will record videos
  #env = gym.make("highway-v0")
  #env = Monitor(env, directory="run", video_callable=lambda e: True)  # record all episodes

  # Feed the monitor to the wrapped environment, so it has access to the video recorder
  # and can send it intermediate simulation frames.
  #env.unwrapped.set_monitor(env)

  # Record a video as usual
  #obs = env.reset()
  #done = False:
  #while not done:
  #    action = env.action_space.sample()
  #    obs, reward, done, info = env.step(action)
  #    env.render()
  #env.close()
