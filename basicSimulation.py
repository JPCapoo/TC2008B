import gym
from gym import envs

# env = gym.make('CartPole-v1')
# env.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample())


# print(envs.registry.all())

env = gym.make('CarRacing-v2')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

print(envs.registry.all())
