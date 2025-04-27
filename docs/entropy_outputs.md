# Resonance Loom Outputs 🌌

Once you successfully run the Loom, you will generate visual outputs showing the **entropy landscape** woven from your EEG recording.

This document explains:

- How to run the Loom
- What the figures mean
- How to interpret entropy maps

---

## 🧠 How to Run the Loom

1. Ensure your EEG `.gdf` files are located under:

    ```
    /eeg-data/BCICIV_2b_gdf/
    ```

2. Run the main script to weave a Loom:

    ```bash
    python loom_real_data_v2.py
    ```

3. The script will automatically:

    - Load the EEG data
    - Extract usable trials
    - Compute entropy over each trial
    - Weave a resonance map from the entropic dynamics

---

## 🌟 Interpreting the Entropy Maps

Each Loom output figure (e.g., `loom_B0701T.png`) shows the **entropy landscape** across time during the EEG session.

- **X-Axis:** Time progression across the extracted trials.
- **Y-Axis:** Normalized entropy value.
- **Color Map:** Density of entropy, highlighting regions of high cognitive activity, attention, or thought transitions.

Higher entropy regions may correspond to:

- Active cognitive shifts
- Motor imagery preparation (depending on task)
- Conscious transitions or wandering thoughts

Lower entropy regions may reflect:

- Stable focused states
- Consistent task engagement
- Relaxed or resting mind

> **Note:** Interpretation depends on both the trial design and the individual’s unique cognitive dynamics.

---

## 📈 Example Figures Included

In the `/examples/` folder, you will find outputs like:

- `loom_B0701T.png` — Entropy map from subject B07, Trial 01 Training
- `loom_B0103T.png` — Entropy map from subject B01, Trial 03 Training
- `loom_B0502T.png` — Entropy map from subject B05, Trial 02 Training
- `entropy_loom_v1.png` — First pilot test of Resonance Loom
- `entropy_loom_v2.png` — Second pilot test of Resonance Loom

Each map gives you a new window into the underlying resonance of thought during the session.

---

# 🌌 Next Steps

Once you have your entropy maps:

- Compare different recordings
- Analyze how entropy varies between tasks
- Explore how cognitive states may emerge in the loom itself

Future updates will include **automated entropy field comparison** and **resonance classification** tools!

---

🧵 Happy Weaving, Navigator. The Loom of Mind awaits. 🌟
