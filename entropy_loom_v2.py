import numpy as np
import matplotlib.pyplot as plt

# --- Simulate Time Series Entropy Data for Two Profiles --- #
np.random.seed(42)  # for reproducibility

time_steps = 100  # 100 time points

# Slow Weaver (gradual collapse)
rest_entropy_slow = np.random.normal(loc=0.9, scale=0.05, size=40)
transition_entropy_slow = np.linspace(0.9, 0.4, 20) + np.random.normal(0, 0.02, 20)
task_entropy_slow = np.random.normal(loc=0.4, scale=0.03, size=40)
entropy_slow = np.concatenate([rest_entropy_slow, transition_entropy_slow, task_entropy_slow])

# Fast Snapper (sharp collapse)
rest_entropy_fast = np.random.normal(loc=0.9, scale=0.05, size=40)
transition_entropy_fast = np.linspace(0.9, 0.4, 5) + np.random.normal(0, 0.02, 5)
task_entropy_fast = np.random.normal(loc=0.4, scale=0.03, size=55)
entropy_fast = np.concatenate([rest_entropy_fast, transition_entropy_fast, task_entropy_fast])

# --- Compute ECQ for both profiles --- #
E_raw_slow = np.mean(rest_entropy_slow)
E_collapsed_slow = np.mean(task_entropy_slow)
T_collapse_slow = 10  # mock slow collapse time

E_raw_fast = np.mean(rest_entropy_fast)
E_collapsed_fast = np.mean(task_entropy_fast)
T_collapse_fast = 2  # mock fast collapse time

ECQ_slow = (E_raw_slow - E_collapsed_slow) / T_collapse_slow
ECQ_fast = (E_raw_fast - E_collapsed_fast) / T_collapse_fast

print("=== Slow Weaver ===")
print(f"E_raw: {E_raw_slow:.3f}")
print(f"E_collapsed: {E_collapsed_slow:.3f}")
print(f"T_collapse: {T_collapse_slow}")
print(f"ECQ: {ECQ_slow:.4f}\n")

print("=== Fast Snapper ===")
print(f"E_raw: {E_raw_fast:.3f}")
print(f"E_collapsed: {E_collapsed_fast:.3f}")
print(f"T_collapse: {T_collapse_fast}")
print(f"ECQ: {ECQ_fast:.4f}")

# --- Plot Entropy Over Time for Both Profiles --- #
plt.figure(figsize=(12,6))
plt.plot(entropy_slow, label='Slow Weaver', color='blue')
plt.plot(entropy_fast, label='Fast Snapper', color='red', linestyle='--')
plt.axhline(E_raw_slow, color='green', linestyle='--', label=f'Slow Rest Avg ({E_raw_slow:.2f})')
plt.axhline(E_collapsed_slow, color='blue', linestyle=':', label=f'Slow Task Avg ({E_collapsed_slow:.2f})')
plt.axhline(E_raw_fast, color='orange', linestyle='--', label=f'Fast Rest Avg ({E_raw_fast:.2f})')
plt.axhline(E_collapsed_fast, color='red', linestyle=':', label=f'Fast Task Avg ({E_collapsed_fast:.2f})')
plt.title('Mock Loom Compression Demo: Slow Weaver vs Fast Snapper')
plt.xlabel('Time Steps')
plt.ylabel('Entropy')
plt.legend()
plt.grid(True)
plt.show()
