import gym
from stable_baselines3 import DQN

# Create the CartPole-v1 environment
env = gym.make("CartPole-v1")

# Initialize the DQN model
model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.001, batch_size=64, buffer_size=10000)

# Train the model for 50,000 timesteps
model.learn(total_timesteps=50000)

# Save the trained model
model.save("dqn_cartpole")
env.close()

print("Model training completed and saved successfully!")
