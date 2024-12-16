from data import *
import matplotlib.pyplot as plt


def main():
    acc_data = load_accelerometer()
    mag_data = load_magnetometer()
    gyro_data = load_gyroscope()
    baro_data = load_barometer()
    ref_data = load_reference_orientation()
    ground_data = load_ground_truth()


if __name__ == "__main__":
    main()