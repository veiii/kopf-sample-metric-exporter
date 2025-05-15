import matplotlib.pyplot as plt
from datetime import datetime

# Parse memory_profile.log
timestamps = []
memory_usage = []

with open('/home/rob/PycharmProjects/kopf-smaple-metric-exporter/tests/memory_profile.log', 'r') as file:
    for line in file:
        if "MiB" in line:
            parts = line.split()
            timestamps.append(len(timestamps))  # Use line index as a timestamp
            memory_usage.append(float(parts[1]))  # Extract memory usage

# Plot memory usage
plt.figure(figsize=(10, 6))
plt.plot(timestamps, memory_usage, marker='o', label='Memory Usage (MiB)')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Memory Usage (MiB)')
plt.title('Memory Usage Over Time')
plt.legend()
plt.grid()
plt.show()

if __name__ == "__main__":
    # This block is only for running the script directly
    plt.savefig(f'memory_usage_plot{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')
    print("Memory usage plot saved as 'memory_usage_plot.png'")