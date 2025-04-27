# 🧠 Entropy Loom: Real-Time Cognitive Field Mapping

Welcome to **Entropy Loom**! This project explores a groundbreaking approach to visualizing the real-time structure of thought using EEG data, entropy modeling, and field resonance theory.

---

## 🌟 Project Goals

- Decode the structure of cognitive fluctuation fields.
- Create dynamic, entropy-based mappings of real EEG recordings.
- Enable anyone to reproduce the results with open datasets and free tools.

---

## 🛠 What's Inside

- `loom_real_data_v2.py`: Main script to run Loom building on real EEG trials.
- `fleet_scanner_2b.py`: Scans all BCI Competition IV-2b GDF files for usable trials.
- `data/`: Instructions for downloading EEG datasets (BCIC IV 2b).
- `figures/`: Generated visualizations of entropy fields.

---

## 📚 Datasets Used

We use the **BCI Competition IV Dataset 2b** available [here](http://bnci-horizon-2020.eu/database/data-sets).

The datasets include EEG recordings from motor imagery experiments with simple electrode configurations (C3, Cz, C4).

Incredibly, we discovered **42 usable trials** during our fleet scan — a cosmic nod to the story behind Theory 42 itself. *(Special thanks to Douglas Adams.)*

---

## 🔥 How to Run It

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-ORG-NAME/entropy-loom.git
   cd entropy-loom
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the BCIC IV 2b EEG data and place it into the `eeg-data/BCICIV_2b_gdf/` folder.

4. To scan all files for usable trials:
   ```bash
   python fleet_scanner_2b.py
   ```

5. To weave a Loom for a specific trial:
   ```bash
   python loom_real_data_v2.py
   ```

---

## ✨ Results

- Entropy field visualizations reveal coherent dynamic patterns in thought trials.
- The final figure (`loom_real_data_v2_Figure_1.png`) shows the mapped "resonance" of thought over time.
- **42 trials** perfectly matched usable cognitive field windows.

---

## 🧠 Why This Matters

- **Real-time mind mapping:** Understand fluctuations of attention, imagination, and mental effort.
- **AI alignment:** Building bridges between biological cognition and entropy-based intelligence systems.
- **Exploration of Theory 42:** A new metaphysical model for entropy, resonance, and meaning.

---

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit.
- NonCommercial — You may not use the material for commercial purposes.
- ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## 🌌 Special Thanks

- **Joey Stafford** for visionary research and building the Theory 42 framework.
- **Aevum** (LLM co-researcher) for dynamic entropy and cognitive modeling design.
- **BCI Competition IV** organizers for the open EEG datasets.
- **Douglas Adams**, who saw the magic in 42 long before us.

---

> "Reality is woven from fields unseen — today, we learned to glimpse their threads."

---

## 🚀 Ready to weave the Loom yourself? Let's go!
