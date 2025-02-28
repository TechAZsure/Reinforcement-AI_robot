import gym
from stable_baselines3 import DQN

# Load the trained model
model = DQN.load("dqn_cartpole")

# Create the environment
env = gym.make("CartPole-v1", render_mode="human")

# Run the model in the environment
obs, _ = env.reset()  # Unpack tuple (obs, info)

for _ in range(1000):  # Run for 1000 time steps
    action, _states = model.predict(obs)  # Get action from the model
    obs, reward, done, _, _ = env.step(action)  # Step through the environment
    env.render()  # Render the environment
    if done:
        obs, _ = env.reset()  # Reset environment correctly

env.close()
print("Simulation Completed!")
