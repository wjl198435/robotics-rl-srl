from __future__ import division, absolute_import, print_function

import time

import environments.kuka_button_gym_env as kuka_env

kuka_env.RECORD_DATA = False
# Reduce max distance to have more negative rewards for srl
kuka_env.MAX_DISTANCE = 0.65
env = kuka_env.KukaButtonGymEnv(renders=True, is_discrete=True, name="kuka_test")

i = 0
start_time = time.time()
for i_episode in range(50):
    observation = env.reset()
    for t in range(501):
        env.render()
        # print(observation.shape)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        i += 1
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

print("{:.2f} FPS".format(i / (time.time() - start_time)))