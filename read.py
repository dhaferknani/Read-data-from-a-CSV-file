import pandas as pd
import numpy as np
# Read CSV
data = pd.read_csv("data.csv", encoding='latin1', sep=';', skiprows=12)
def angle_diff(angle1, angle2):
    """Calculate the minimum difference between two angles"""
    d = angle1 - angle2
    return (d + 180) % 360 - 180

for index, row in data.iterrows():
    Ax = row['Ax(g)']
    Ay = row['Ay(g)']
    Az = row['Az(g)']
    Gx = row['Gx(r/s)']
    Gy = row['Gy(r/s)']
    Gz = row['Gz(r/s)']
    Mx = row['Mx(uT)']
    My = row['My(uT)']
    Mz = row['Mz(uT)']

    # Reference Euler angles from CSV
    roll_csv  = row['r_est(d)']
    pitch_csv = row['p_est(d)']
    yaw_csv   = row['y_est(d)']

    print(f"Line {index}: Roll={roll_csv:.2f}°, Pitch={pitch_csv:.2f}°, Yaw={yaw_csv:.2f}°")