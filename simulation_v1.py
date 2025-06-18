import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Parameters
num_hours = 24 * 30  # 30 days hourly data
time_index = pd.date_range(start='2024-01-01', periods=num_hours, freq='H')

# Simulate normal operation signals
temperature = 70 + 5 * np.sin(np.linspace(0, 3*np.pi, num_hours)) + np.random.normal(0, 0.5, num_hours)
load_current = 100 + 20 * np.sin(np.linspace(0, 10*np.pi, num_hours)) + np.random.normal(0, 5, num_hours)
voltage = 240 + np.random.normal(0, 1, num_hours)

# Inject anomaly events for failures
anomalies_idx = np.random.choice(num_hours, size=5, replace=False)

for idx in anomalies_idx:
    # Simulate temperature spike and current spike
    temperature[idx:idx+3] += 15  # sudden temp increase for 3 hours
    load_current[idx:idx+3] += 40

# Create DataFrame
df = pd.DataFrame({
    'timestamp': time_index,
    'temperature': temperature,
    'load_current': load_current,
    'voltage': voltage
})
df.set_index('timestamp', inplace=True)

# Plot data for visualization
plt.figure(figsize=(12,6))
plt.plot(df.index, df['temperature'], label='Temperature')
plt.plot(df.index, df['load_current'], label='Load Current')
plt.scatter(df.index[anomalies_idx], df['temperature'].iloc[anomalies_idx], color='red', label='Anomaly', zorder=5)
plt.legend()
plt.title('Simulated SCADA Data with Anomalies')
plt.show()
