# -*- coding: utf-8 -*-
"""
Set up gym environment
"""


import gym
import dqn_agent as ag 
import numpy as np
import time

# Generate an environment
env = gym.make('Pong-v0')

# Generate an agent
agent = ag.DQN_Agent(env)
agent.load()

eval_interval = 5
num_episode = 5
total_score = []
eval_steps = []
for i_episode in range(num_episode):
    observation  = env.reset()
    terminal = False
    total_score_ = 0
    reward = 0.0  # initial reward is assumed to be zero
    step_in_episode = 0

    if np.mod(i_episode, eval_interval) == 0:
        # Learnin OFF evaluation
        agent.policyFrozen = True
    else:
        # Learning ON
        agent.policyFrozen = False

    while True:
        print(str(i_episode) + "-th episode")
        #env.render() # Render the game

        if step_in_episode == 0:
            observation, reward, terminal, info = env.step(agent.start(observation)) # take an action
        else:
            observation, reward, terminal, info = env.step(agent.act(observation, reward)) # take an action

        total_score_ += reward
        step_in_episode += 1

        if terminal is True:
            agent.end(reward)
            break

    if np.mod(i_episode, eval_interval) == 0:
        total_score.append(total_score_)
        eval_steps.append(i_episode)
        print("REWARD@" + str(i_episode) + "-th episode : " + str(total_score_))

        # Save the current agent parameters
        agent.save()
