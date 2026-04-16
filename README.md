# ECE 105 Lab 3 Sensor Plots

Standalone Python script for generating reproducible synthetic temperature sensor data as part of a notebook-to-script conversion workflow.

## Installation

Activate the `ece105` conda environment, then install the required packages with `conda` or `mamba`:

```bash
conda activate ece105
mamba install numpy matplotlib
```

If you prefer `conda` instead of `mamba`, use:

```bash
conda activate ece105
conda install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

At the current stage of the conversion, `generate_plots.py` defines the synthetic data generation function and is being built out into the full standalone plotting script.

## Example output

The full script is intended to produce three plot types based on the generated sensor data:

1. A scatter plot of Sensor A and Sensor B temperature readings versus time, using different colors and a legend.
2. A histogram view for comparing the temperature distributions of the two sensors.
3. A box plot summarizing the spread, center, and outliers of the two sensor datasets.

At the current state of `generate_plots.py`, no PNG output files are written yet because the plotting and file-saving portions of the script have not been fully implemented.

## AI tools used and disclosure

_Placeholder: describe any AI tools you used during development, what they were used for, and how you reviewed or validated their output._
