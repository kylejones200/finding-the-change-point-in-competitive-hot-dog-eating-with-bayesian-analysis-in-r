"""Generated from Jupyter notebook: Safety Change Point Detection Analysis

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

# Required imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Install and import ruptures for change point detection
try:
    import ruptures as rpt
except ImportError:
    print("Installing ruptures...")
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "ruptures"])
    import ruptures as rpt

    print("Installation complete.")


# --- code cell ---


# Prepare the safety data
def load_safety_data():
    """
    Load RIFR (Recordable Injury Frequency Rate) data per 200k hours worked.
    Data covers the period from 1986 to 2020.
    """
    data = {
        "Year": list(range(1986, 2021)),
        "RIFR_per_200k": [
            4.22,
            8.32,
            4.68,
            8.77,
            2.09,
            0.74,
            0.00,
            0.00,
            0.00,
            2.76,
            7.60,
            2.05,
            3.45,
            2.42,
            2.03,
            1.90,
            1.61,
            2.29,
            0.87,
            1.20,
            1.32,
            1.31,
            1.70,
            1.62,
            0.86,
            1.06,
            1.08,
            0.67,
            0.64,
            0.88,
            0.98,
            0.76,
            0.34,
            0.54,
            0.35,
        ],
    }

    df = pd.DataFrame(data)
    return df


# Load data
df = load_safety_data()
print(
    f"Data loaded: {len(df)} years of safety data from {df['Year'].min()} to {df['Year'].max()}"
)
print(f"RIFR range: {df['RIFR_per_200k'].min():.2f} to {df['RIFR_per_200k'].max():.2f}")


# --- code cell ---


# Perform change point detection
def detect_change_points(signal, n_bkps=5, model="l2"):
    """
    Detect change points in the safety data using Binary Segmentation.

    Parameters:
    - signal: array-like, the time series data
    - n_bkps: int, maximum number of change points to detect
    - model: str, cost function to use ('l2' for least squares)

    Returns:
    - change_points: list of change point indices
    """
    try:
        algo = rpt.Binseg(model=model).fit(signal)
        change_points = algo.predict(n_bkps=n_bkps)
        return change_points
    except Exception as e:
        print(f"Error in change point detection: {e}")
        return []


# Extract signal and detect change points
signal = df["RIFR_per_200k"].values
change_points = detect_change_points(signal, n_bkps=5)

print(
    f"Detected {len(change_points) - 1} change points at indices: {change_points[:-1]}"
)


# --- code cell ---


# Visualize results
def plot_change_points(df, signal, change_points, save_fig=True):
    """
    Plot the time series with detected change points.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the signal with change points
    rpt.display(signal, change_points, ax=ax)

    # Customize the plot
    ax.set_title(
        "Change Point Detection in RIFR per 200k Hours (1986–2020)",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("RIFR per 200k Hours", fontsize=12)

    # Set x-axis labels to show years
    ax.set_xticks(np.arange(0, len(df), 5))
    ax.set_xticklabels(df["Year"].iloc[::5])

    # Add grid for better readability
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_fig:
        plt.savefig("change_point_rifr.png", dpi=300, bbox_inches="tight")
        print("Plot saved as 'change_point_rifr.png'")

    plt.show()


# Create the visualization
if change_points:
    plot_change_points(df, signal, change_points)
else:
    print("No change points detected to plot.")


# --- code cell ---


# Analyze change points
def analyze_change_points(df, change_points):
    """
    Analyze the detected change points and provide insights.
    """
    if not change_points or len(change_points) <= 1:
        print("No change points detected for analysis.")
        return

    # Convert indices to years (excluding the last point which is the end of series)
    change_years = [df["Year"].iloc[i - 1] for i in change_points[:-1]]

    print("\n=== Change Point Analysis ===")
    print(f"Detected change points at years: {change_years}")

    # Analyze periods between change points
    periods = [0] + change_points

    print("\n=== Period Analysis ===")
    for i in range(len(periods) - 1):
        start_idx = periods[i]
        end_idx = periods[i + 1]

        period_data = df.iloc[start_idx:end_idx]
        start_year = period_data["Year"].iloc[0]
        end_year = period_data["Year"].iloc[-1]
        mean_rifr = period_data["RIFR_per_200k"].mean()
        std_rifr = period_data["RIFR_per_200k"].std()

        print(f"Period {i + 1}: {start_year}-{end_year}")
        print(f"  Mean RIFR: {mean_rifr:.2f} ± {std_rifr:.2f}")
        print(f"  Duration: {len(period_data)} years")
        print()


# Perform analysis
analyze_change_points(df, change_points)


# --- code cell ---


# Summary statistics
def print_summary(df):
    """
    Print summary statistics of the safety data.
    """
    print("\n=== Data Summary ===")
    print(f"Time period: {df['Year'].min()} - {df['Year'].max()}")
    print(f"Total years: {len(df)}")
    print(f"Mean RIFR: {df['RIFR_per_200k'].mean():.2f}")
    print(f"Median RIFR: {df['RIFR_per_200k'].median():.2f}")
    print(f"Standard deviation: {df['RIFR_per_200k'].std():.2f}")
    print(
        f"Min RIFR: {df['RIFR_per_200k'].min():.2f} (Year: {df.loc[df['RIFR_per_200k'].idxmin(), 'Year']})"
    )
    print(
        f"Max RIFR: {df['RIFR_per_200k'].max():.2f} (Year: {df.loc[df['RIFR_per_200k'].idxmax(), 'Year']})"
    )

    # Count zero injury years
    zero_years = (df["RIFR_per_200k"] == 0).sum()
    print(f"Years with zero injuries: {zero_years}")


print_summary(df)
