import pandas as pd
# DP = DataPoint

def load_accelerometer():
    return pd.read_csv('data/accelerometer.csv', dtype={"time [ms]": int})

def load_magnetometer():
    return pd.read_csv('data/magnetometer.csv', dtype={"time [ms]": int})

def load_gyroscope():
    return pd.read_csv('data/gyroscope.csv', dtype={"time [ms]": int})

def load_barometer():
    return pd.read_csv('data/barometer.csv', dtype={"time [ms]": int})

def load_reference_orientation():
    return pd.read_csv('data/referenceOrientation.csv', dtype={"time [ms]": int})

def load_ground_truth():
    return pd.read_csv('data/groundTruth.csv', dtype={"time [ms]": int})