import numpy as np
import matplotlib.pyplot as plt

# --- Simulate Time Series Entropy Data --- #
np.random.seed(42)  # for reproducibility

time_steps = 100  # 100 time points

# Simulate Resting Phase (first 40 steps)
rest_entropy = np.random.normal(loc=0.9, scale=0.05, size=40)

# Simulate Transition Phase (next 20 steps)
transition_entropy = np.linspace(0.9, 0.4, 20) + np.random.normal(0, 0.02, 20)

# Simulate Task Phase (final 40 steps)
task_entropy = np.random.normal(loc=0.4, scale=0.03, size=40)

# Combine into full entropy timeline
entropy_timeline = np.concatenate([rest_entropy, transition_entropy, task_entropy])

# --- Compute ECQ --- #
E_raw = np.mean(rest_entropy)
E_collapsed = np.mean(task_entropy)
T_collapse = 5  # assume 5 seconds to stabilize (mock value)

ECQ = (E_raw - E_collapsed) / T_collapse

print(f"E_raw (rest entropy): {E_raw:.3f}")
print(f"E_collapsed (task entropy): {E_collapsed:.3f}")
print(f"T_collapse (seconds): {T_collapse}")
print(f"\nCalculated ECQ: {ECQ:.4f}")

# --- Plot Entropy Over Time --- #
plt.figure(figsize=(10,6))
plt.plot(entropy_timeline, label='Simulated Brain Entropy', color='blue')
plt.axhline(E_raw, color='green', linestyle='--', label=f'Rest Avg Entropy ({E_raw:.2f})')
plt.axhline(E_collapsed, color='red', linestyle='--', label=f'Task Avg Entropy ({E_collapsed:.2f})')
plt.axvline(40, color='gray', linestyle=':', label='Task Start')
plt.axvline(60, color='gray', linestyle=':', label='Collapse Complete')
plt.title('Mock Loom Compression Demo: Entropy Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Entropy')
plt.legend()
plt.grid(True)
plt.show()
