import matplotlib.pyplot as plt

# Example Reward History (Replace with actual log)
reward_history = [100, 150, 200, 180, 250, 300, 350, 400, 450, 500]

# Plot rewards over episodes
plt.plot(range(len(reward_history)), reward_history)
plt.xlabel("Episodes")
plt.ylabel("Total Reward")
plt.title("DQN Training Performance")
plt.show()
