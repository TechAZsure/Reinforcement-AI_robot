import numpy as np
import gym
from stable_baselines3 import DQN

def evaluate_model(model, env, num_episodes=10):
    rewards_list = []
    
    for episode in range(num_episodes):
        obs, _ = env.reset()  # Unpack tuple (obs, info) for Gym v26+
        total_rewards = 0
        done = False
        
        while not done:
            action, _ = model.predict(obs)  # Predict action
            obs, reward, done, _, _ = env.step(action)  # Unpack all returned values
            total_rewards += reward
        
        rewards_list.append(total_rewards)
        print(f"Episode {episode+1}: Reward = {total_rewards}")
    
    avg_reward = np.mean(rewards_list)
    print(f"Average Reward over {num_episodes} episodes: {avg_reward}")

# Load the trained model
model = DQN.load("dqn_cartpole")

# Create environment
env = gym.make("CartPole-v1")

# Evaluate the trained model
evaluate_model(model, env)
