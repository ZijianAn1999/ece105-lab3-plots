"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.


def generate_data(seed):
    """Generate synthetic temperature data for two sensors.

    Parameters
    ----------
    seed : int
        Seed passed to ``np.random.default_rng`` for reproducible data.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape ``(200,)`` containing Sensor A temperatures in
        degrees Celsius, sampled from a normal distribution with mean 25
        and standard deviation 3.
    sensor_b : numpy.ndarray
        Array of shape ``(200,)`` containing Sensor B temperatures in
        degrees Celsius, sampled from a normal distribution with mean 27
        and standard deviation 4.5.
    timestamps : numpy.ndarray
        Array of shape ``(200,)`` containing timestamps in seconds drawn
        uniformly from 0 to 10 and sorted in ascending order.
    """
    n_readings = 200
    rng = np.random.default_rng(seed)

    sensor_a = rng.normal(loc=25, scale=3, size=n_readings)
    sensor_b = rng.normal(loc=27, scale=4.5, size=n_readings)
    timestamps = np.sort(rng.uniform(0, 10, size=n_readings))

    return sensor_a, sensor_b, timestamps
