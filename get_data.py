import cv2
import pandas as pd
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


#getting colummn names
col_names = []
for lndmrk in mp_pose.PoseLandmark:
    col_names.append(str(lndmrk)[13:]+"_X")
    col_names.append(str(lndmrk)[13:]+"_Y")
    col_names.append(str(lndmrk)[13:]+"_Z")

#selecting only those columns which are required    
col_names = col_names[33:]
# df3 = pd.DataFrame(columns=a)




    
def extract(path):
    """Extracts co-ordinates required to check similarity of helicopter
    shot"""
    def send_data(results):
        try:
            landmarks = results.pose_landmarks.landmark
            row = []
            for i in range(11,33):
                broken = str(landmarks[i]).split("\n")
                for i in range(len(broken)-2):
                    row.append(float(broken[i][3:]))
            
            df3.loc[len(df3)] = row

        except:
                pass

    print("yes")
#     print(df3.shape)
#     global df3
    df3 = pd.DataFrame(columns=col_names)
#     global df3
    cap = cv2.VideoCapture(path)
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == True:

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False  #helps save memory when passing to model

                # Make detection
                results = pose.process(image)
                send_data(results)
    #             data.append(results.pose_landmarks.landmark)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), #color of dots
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) #color of line
                                         )               

                cv2.imshow('Mediapipe Feed', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
    print("done")

    df3.to_csv("main.csv")
    return df3



