import os
import re
import subprocess
import pandas as pd

# Input folder setup
input_folder = os.getcwd()  # Current working directory
output_folder = os.path.join(input_folder, "output")
os.makedirs(output_folder, exist_ok=True)

# User inputs
protein_file = "protein.pdbqt"  # Protein file
vina_executable = "vina.exe"  # Ensure vina.exe is present in the folder
ligand_files = [f for f in os.listdir(input_folder) if f.endswith(".pdbqt") and "protein" not in f]

# Check for required files
if not os.path.exists(protein_file):
    raise FileNotFoundError(f"Protein file '{protein_file}' not found in the folder!")
if not os.path.exists(vina_executable):
    raise FileNotFoundError(f"AutoDock Vina executable '{vina_executable}' not found in the folder!")
if not ligand_files:
    raise FileNotFoundError("No ligand files (.pdbqt) found in the folder!")

# Get binding site coordinates from user
center_x, center_y, center_z = map(
    float, input("Enter binding site coordinates (x, y, z separated by spaces): ").split()
)

# Grid box size
size_x, size_y, size_z = 30, 30, 30

# Function to write config file
def write_config_file(receptor, ligand, config_filename):
    with open(config_filename, "w") as config_file:
        config_file.write(f"""receptor = {receptor}
ligand = {ligand}
center_x = {center_x}
center_y = {center_y}
center_z = {center_z}
size_x = {size_x}
size_y = {size_y}
size_z = {size_z}
""")

# Function to extract Mode 1 affinity from a log file
def extract_mode1_affinity(log_file):
    with open(log_file, "r") as file:
        for line in file:
            if re.match(r"^\s*1\s+-?\d+\.\d+", line):  # Look for Mode 1 line
                return float(line.split()[1])  # Extract affinity value (2nd column)
    return None  # Return None if no Mode 1 line is found

# Docking and extraction process
results = []

for ligand in ligand_files:
    config_file = os.path.join(output_folder, "config.txt")
    log_file = os.path.join(output_folder, f"{os.path.splitext(ligand)[0]}_log.txt")
    output_file = os.path.join(output_folder, f"{os.path.splitext(ligand)[0]}_output.pdbqt")

    # Write the config file
    write_config_file(protein_file, ligand, config_file)

    # Run AutoDock Vina
    vina_command = [
        vina_executable,
        f"--receptor {protein_file}",
        f"--ligand {ligand}",
        f"--config {config_file}",
        f"--log {log_file}",
        f"--out {output_file}",
    ]
    subprocess.run(" ".join(vina_command), shell=True)

    # Extract Mode 1 affinity from the log file
    affinity = extract_mode1_affinity(log_file)
    ligand_name = os.path.splitext(os.path.basename(log_file))[0].replace("_log", "")  # Extract ligand name
    results.append({"Ligand Name": ligand_name, "Mode 1 Affinity (kcal/mol)": affinity})

# Rank results and save to CSV
df = pd.DataFrame(results)
df = df.sort_values(by="Mode 1 Affinity (kcal/mol)", ascending=True)  # Smaller values come first
df["Rank"] = range(1, len(df) + 1)  # Add rank column
df = df[["Rank", "Ligand Name", "Mode 1 Affinity (kcal/mol)"]]  # Reorder columns

# Save the ranked results to CSV
output_csv = os.path.join(output_folder, "docking_results.csv")
df.to_csv(output_csv, index=False)

print(f"Docking completed. Check the output folder for log and output files.")
print(f"Ranked results saved to {output_csv}")
