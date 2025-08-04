import mne
import os

# --- CONFIGURATION --- #
gdf_folder = '/Users/joeystafford/Repos/resonance-loom/eeg-data/BCICIV_2b_gdf/'  # <-- Your actual folder
sfreq_target = 250  # BCI 2b is usually recorded at 250 Hz

# --- SCANNER --- #
gdf_files = [f for f in os.listdir(gdf_folder) if f.endswith('.gdf')]

print(f"🌌 Found {len(gdf_files)} GDF files to scan.\n")

for gdf_file in sorted(gdf_files):
    file_path = os.path.join(gdf_folder, gdf_file)
    print(f"🌟 Scanning {gdf_file}...")

    try:
        raw = mne.io.read_raw_gdf(file_path, preload=True)
        raw.pick_types(eeg=True)
        raw.resample(sfreq_target)

        events, event_id = mne.events_from_annotations(raw)
        events[:, 0] = (events[:, 0] * raw.info['sfreq']).astype(int)

        # Find usable trials (trial start '768' == event_id '6')
        trial_starts = []
        for onset_sample, _, code in events:
            if code == 6:  # Trial start
                rest_end = onset_sample + int(2 * sfreq_target)
                task_end = onset_sample + int(6 * sfreq_target)
                if task_end <= raw.n_times:
                    trial_starts.append(onset_sample)

        if trial_starts:
            print(f"✅ {gdf_file}: {len(trial_starts)} usable trials found!\n")
        else:
            print(f"❌ {gdf_file}: No usable trials in EEG recording.\n")

    except Exception as e:
        print(f"⚠️ {gdf_file}: Failed to scan due to error: {e}\n")

print("🌟 Fleet scan complete!")
