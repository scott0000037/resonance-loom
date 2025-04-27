# loom_real_data_v2.py

import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

# ---------------------
# Configurations
# ---------------------
# data_path = './eeg-data/BCICIV_2b_gdf/B0701T.gdf'

data_path = './eeg-data/path-to/file.gdf' # Set your .gdf file path here
selected_channel = 'EEG:C3'
rest_duration = 2  # seconds (rest window before movement cue)
task_duration = 3  # seconds (after movement cue)
sampling_rate = 250  # Hz

# ---------------------
# Load Data
# ---------------------
print("\n🌌 Loading EEG data...")
raw = mne.io.read_raw_gdf(data_path, preload=True)
raw.pick_types(eeg=True)

# Channel checking
print(f"Available channels: {raw.ch_names}")
if selected_channel not in raw.ch_names:
    raise ValueError(f"Selected channel {selected_channel} not found!")
raw.pick_channels([selected_channel])

# ---------------------
# Parse Events
# ---------------------
print("\n🧠 Parsing events...")
events, event_id = mne.events_from_annotations(raw)
print(f"Detected Event IDs: {event_id}")

# Map useful event codes
START_TRIAL = event_id.get('768', None)
LEFT_HAND = event_id.get('769', None)
RIGHT_HAND = event_id.get('770', None)
REJECT = event_id.get('1023', None)

if None in (START_TRIAL, LEFT_HAND, RIGHT_HAND):
    raise ValueError("Necessary event codes not found!")

# ---------------------
# Collect Windows
# ---------------------
rest_windows = []
task_windows = []

for i, (onset_sample, _, code) in enumerate(events):
    if code == START_TRIAL:
        # Find the next event
        if i+1 < len(events):
            next_onset, _, next_code = events[i+1]
            if next_code in [LEFT_HAND, RIGHT_HAND]:
                rest_start = onset_sample - int(rest_duration * sampling_rate)
                task_start = next_onset
                task_end = task_start + int(task_duration * sampling_rate)
                
                # Make sure windows are within data bounds
                if rest_start >= 0 and task_end <= len(raw.times):
                    rest = raw.get_data(start=rest_start, stop=onset_sample).flatten()
                    task = raw.get_data(start=task_start, stop=task_end).flatten()
                    rest_windows.append(rest)
                    task_windows.append(task)
                else:
                    print(f"⚠️ Skipping window around sample {onset_sample} (out of bounds)")

print(f"\n✅ Extracted {len(rest_windows)} usable trials!")

if len(rest_windows) == 0:
    raise ValueError("No usable trials were extracted! Check event structure.")

# ---------------------
# Compute Entropies
# ---------------------
print("\n📈 Computing entropies...")
rest_entropies = []
task_entropies = []

for rest, task in zip(rest_windows, task_windows):
    rest_hist, _ = np.histogram(rest, bins=50, density=True)
    task_hist, _ = np.histogram(task, bins=50, density=True)
    rest_entropies.append(entropy(rest_hist + 1e-10))  # Add epsilon to avoid log(0)
    task_entropies.append(entropy(task_hist + 1e-10))

# ---------------------
# Plot Results
# ---------------------
plt.figure(figsize=(10, 6))
plt.plot(rest_entropies, label='Rest Entropy', marker='o')
plt.plot(task_entropies, label='Task Entropy', marker='x')
plt.title('Entropy over Trials (C3 Channel)')
plt.xlabel('Trial Number')
plt.ylabel('Entropy')
plt.legend()
plt.grid(True)
plt.show()

print("\n🌟 Loom weaving complete. Ready for Resonance Analysis!")
