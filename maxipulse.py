import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data generation (replace with your actual data)
np.random.seed(42)
duration_data = np.random.gamma(shape=2, scale=50, size=1000)
pulse_data = np.random.normal(loc=120, scale=15, size=1000)

# Set up the figure
plt.figure(figsize=(12, 6))

# Duration Distribution plot
plt.subplot(1, 2, 1)
sns.histplot(duration_data, bins=20, color='skyblue', edgecolor='black')
plt.title('Duration Distribution', fontsize=14)
plt.xlabel('Duration (seconds)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', alpha=0.5)

# Add mean and median lines
mean_dur = np.mean(duration_data)
median_dur = np.median(duration_data)
plt.axvline(mean_dur, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_dur:.1f}s')
plt.axvline(median_dur, color='green', linestyle='--', linewidth=1.5, label=f'Median: {median_dur:.1f}s')
plt.legend()

# Pulse Distribution plot
plt.subplot(1, 2, 2)
sns.histplot(pulse_data, bins=15, color='salmon', edgecolor='black')
plt.title('Pulse Distribution', fontsize=14)
plt.xlabel('Pulse (bpm)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', alpha=0.5)

# Add mean and median lines
mean_pulse = np.mean(pulse_data)
median_pulse = np.median(pulse_data)
plt.axvline(mean_pulse, color='red', linestyle='--', linewidth=1.5, label=f'Mean: {mean_pulse:.1f}bpm')
plt.axvline(median_pulse, color='green', linestyle='--', linewidth=1.5, label=f'Median: {median_pulse:.1f}bpm')
plt.legend()

plt.tight_layout()
plt.show()