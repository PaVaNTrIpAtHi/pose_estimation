from get_data_32 import extract
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_angle2(a1,a2,b1,b2,c1,c2): 
    radians = np.arctan2(c2-b2, c1-b1) - np.arctan2(a2-b2, a1-b1)
    angle = np.abs(radians*180.0/np.pi)    
    return angle 

def find_angles(df):
    mf = pd.DataFrame()
    rig_shou= []
    rig_elbow= []
    rig_wrist= []
    rig_hip= []
    rig_knee= []
    rig_heel= []
    left_shou= []
    left_elbow= []
    left_wrist= []
    left_hip= []
    left_knee= []
    left_heel= []
    for i in range(df.shape[0]):
        rig_shou.append(calculate_angle2(df.RIGHT_HIP_X.iloc[i],df.RIGHT_HIP_Y.iloc[i],df.RIGHT_SHOULDER_X.iloc[i],
                                         df.RIGHT_SHOULDER_Y.iloc[i],df.RIGHT_ELBOW_X.iloc[i],df.RIGHT_ELBOW_Y.iloc[i]))

        rig_elbow.append(calculate_angle2(df.RIGHT_SHOULDER_X.iloc[i],df.RIGHT_SHOULDER_Y.iloc[i],df.RIGHT_ELBOW_X.iloc[i],
                                          df.RIGHT_ELBOW_Y.iloc[i],df.RIGHT_WRIST_X.iloc[i],df.RIGHT_WRIST_Y.iloc[i],))

        rig_wrist.append(calculate_angle2(df.RIGHT_INDEX_X.iloc[i],df.RIGHT_INDEX_Y.iloc[i],df.RIGHT_WRIST_X.iloc[i],
                                          df.RIGHT_WRIST_Y.iloc[i],df.RIGHT_THUMB_X.iloc[i],df.RIGHT_THUMB_Y.iloc[i]))

        rig_hip.append(calculate_angle2(df.RIGHT_SHOULDER_X.iloc[i],df.RIGHT_SHOULDER_Y.iloc[i],df.RIGHT_HIP_X.iloc[i],
                                          df.RIGHT_HIP_Y.iloc[i],df.RIGHT_KNEE_X.iloc[i],df.RIGHT_KNEE_Y.iloc[i]))

        rig_knee.append(calculate_angle2(df.RIGHT_HIP_X.iloc[i],df.RIGHT_HIP_Y.iloc[i],df.RIGHT_KNEE_X.iloc[i],
                                         df.RIGHT_KNEE_Y.iloc[i],df.RIGHT_HEEL_X.iloc[i],df.RIGHT_HEEL_Y.iloc[i]))

        rig_heel.append(calculate_angle2(df.RIGHT_KNEE_X.iloc[i],df.RIGHT_KNEE_Y.iloc[i],df.RIGHT_HEEL_X.iloc[i],
                                         df.RIGHT_HEEL_Y.iloc[i],df.RIGHT_FOOT_INDEX_X.iloc[i],df.RIGHT_FOOT_INDEX_Y.iloc[i]))

        left_shou.append(calculate_angle2(df.LEFT_HIP_X.iloc[i],df.LEFT_HIP_Y.iloc[i],df.LEFT_SHOULDER_X.iloc[i],
                                          df.LEFT_SHOULDER_Y.iloc[i],df.LEFT_ELBOW_X.iloc[i],df.LEFT_ELBOW_Y.iloc[i]))

        left_elbow.append(calculate_angle2(df.LEFT_SHOULDER_X.iloc[i],df.LEFT_SHOULDER_Y.iloc[i],df.LEFT_ELBOW_X.iloc[i],
                                          df.LEFT_ELBOW_Y.iloc[i],df.LEFT_WRIST_X.iloc[i],df.LEFT_WRIST_Y.iloc[i],))

        left_wrist.append(calculate_angle2(df.LEFT_INDEX_X.iloc[i],df.LEFT_INDEX_Y.iloc[i],df.LEFT_WRIST_X.iloc[i],
                                          df.LEFT_WRIST_Y.iloc[i],df.LEFT_THUMB_X.iloc[i],df.LEFT_THUMB_Y.iloc[i]))

        left_hip.append(calculate_angle2(df.LEFT_SHOULDER_X.iloc[i],df.LEFT_SHOULDER_Y.iloc[i],df.LEFT_HIP_X.iloc[i],
                                          df.LEFT_HIP_Y.iloc[i],df.LEFT_KNEE_X.iloc[i],df.LEFT_KNEE_Y.iloc[i]))

        left_knee.append(calculate_angle2(df.LEFT_HIP_X.iloc[i],df.LEFT_HIP_Y.iloc[i],df.LEFT_KNEE_X.iloc[i],
                                         df.LEFT_KNEE_Y.iloc[i],df.LEFT_HEEL_X.iloc[i],df.LEFT_HEEL_Y.iloc[i]))

        left_heel.append(calculate_angle2(df.LEFT_KNEE_X.iloc[i],df.LEFT_KNEE_Y.iloc[i],df.LEFT_HEEL_X.iloc[i],
                                         df.LEFT_HEEL_Y.iloc[i],df.LEFT_FOOT_INDEX_X.iloc[i],df.LEFT_FOOT_INDEX_Y.iloc[i]))
        
    mf["rig_shou"] = rig_shou
    mf["rig_elbow"] =rig_elbow 
#     mf["rig_wrist"] = rig_wrist
    mf["rig_hip"] =rig_hip
    mf["rig_knee"] = rig_knee 
    mf["rig_heel"] = rig_heel
    mf["left_shou"] = left_shou
    mf["left_elbow"] = left_elbow
#     mf["left_wrist"] = left_wrist
    mf["left_hip"] = left_hip 
    mf["left_knee"] = left_knee
    mf["left_heel"] = left_heel
    
    return mf
#     return rig_shou,rig_elbow,rig_wrist,rig_hip,rig_knee,rig_heel,left_shou,left_elbow,left_wrist,left_hip,left_knee,left_heel



def get_points(vid2):
#     da = extract(vid1)
    da = pd.read_csv("msd_main_32.csv")
    js = extract(vid2)
    if js.shape[0]>da.shape[0]:
        js = js[:da.shape[0]]
    elif js.shape[0]<da.shape[0]:
        da = da[:js.shape[0]]
        
    da2 = find_angles(da)
    pa2 = find_angles(js)
    return da,js,da2,pa2
        
    