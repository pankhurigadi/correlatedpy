.. _faq:

=============================
Frequently Asked Questions
=============================


This is a list of Frequently Asked Questions about correlatedpy. Feel free to suggest new entries!

My algorithm does not converge. Why?
    The convergence of the algorithm is guaranteed (see proof in the author's paper). Indeed, for any game you define, there exist at least a correlated equilibrium point, and the expected behaviour of the algorithm is to converege towards it.
    In :cite:`Leurent2019social`, we argued that a possible reason could either be a high exploration rate that does not allow the algorithm to remain at the equilibrium long enough, or a small time horizon. Indeed, a suffcient number of game roubds must be played in order to reach a steady state regime.
    This can be addressed in two ways:

    - Decrease the exploration/experimentation rate *epsilon*, to use a small perturbation, see *e.g.* :cite:`Qi2017pointnet` or :cite:`Leurent2019social` for examples.
    This example is implemented `here (DQN) <https://colab.research.google.com/github/eleurent/highway-env/blob/master/scripts/intersection_social_dqn.ipynb>`_ or `here (SB3's PPO) <https://github.com/eleurent/highway-env/blob/master/scripts/sb3_highway_ppo_transformer.py>`_.

    - Increase the time horizon or number of iterations. A rule of thumb is to play no less than :math:`\frac{2 \times |\max_{a, i}u_i(a)|}{\varepsilon^2}` game rounds.

My videos are too fast / have a low framerate.
    This is because in openai/gym, a single video frame is generated at each call of ``env.step(action)``. However, in highway-env, the policy typically runs at a low-level frequency (e.g. 1 Hz) so that a long action (*e.g.* change lane) actually corresponds to several (typically, 15) simulation frames.
    In order to also render these intermediate simulation frames, the following should be done:

.. code-block:: python

  #import gym
  #import highway_env

  # Wrap the env by a Monitor, which will record videos
  #env = gym.make("highway-v0")
  #env = Monitor(env, directory="run",
                video_callable=lambda e: True)  # record all episodes

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
