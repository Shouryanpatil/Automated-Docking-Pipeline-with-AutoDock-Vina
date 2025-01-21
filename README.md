# Automated-Docking-Pipeline-with-AutoDock-Vina
This repository provides a Python-based automation script for molecular docking using AutoDock Vina. If you have a large number of ligands (e.g., 50, 100, or even 500) and need to perform docking with a single protein efficiently, this tool is for you. The script automates the docking process, extracts binding affinities, and ranks the ligands based on their binding scores—all in just a few clicks. At the end of the process, you'll know which ligand is the best among all tested.

Whether you're working on drug discovery, structural biology, or any computational docking project, this tool simplifies and speeds up your workflow.
# Features
- Automates the docking process for multiple ligands.
- Generates configuration files for AutoDock Vina dynamically.
- Extracts Mode 1 binding affinities from log files.
- Produces ranked results in a docking_results.csv file.
- Outputs the docking results (.pdbqt) and log files for each ligand.

# Files in this Repository
1. automation_script.py
- A Python script that automates the molecular docking process using AutoDock Vina.
2. vina.exe
- The AutoDock Vina executable file used to perform molecular docking.
3. vina_license.rtf
- The official license file for AutoDock Vina.
4. vina_split.exe
- An auxiliary executable provided with AutoDock Vina.

# Requirements
Software
- Python 3.x
- AutoDock Vina
- Python Libraries

Ensure the following Python libraries are installed:
- os
- re
- subprocess
- pandas

# How to Use
1. Place Required Files
- Add your protein.pdbqt file to the project folder.
- Add all ligand files (.pdbqt) to the project folder.
- Ensure the vina.exe file is present in the same folder.
2. Run the Script
- Open a terminal or command prompt.
- Navigate to the project folder.
- Run the script:
- In bash
 "python automation_script.py"
- Enter the binding site coordinates when prompted (e.g., 16.42 -20.65 10.93).

# Outputs
1. Docking Results:
- .pdbqt files for each ligand in the output/ folder.
- Log files (_log.txt) for each ligand in the output/ folder.
2. Ranked Results:
- A docking_results.csv file in the output/ folder, containing:
- Rank: The rank of the ligand based on binding affinity.
- Ligand Name: The name of the ligand (e.g., ligand1, ligand2).
- Mode 1 Affinity: The binding affinity (in kcal/mol).

# Notes
- Ensure your protein and ligand files are prepared and in .pdbqt format before running the script.
- If the script does not run, verify that:
- vina.exe is correctly configured and in the project folder.
- The protein.pdbqt file and ligand files are formatted correctly.
- You have Python 3.x installed with the required libraries.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
