import numpy as np
import cv2
from objdtect import give_class
from read import look 
import file_utils


def polygon(img, boxes):
    for i, box in enumerate(boxes):
        poly = np.array(box).astype(np.int32).reshape((-1))
        poly = poly.reshape(-1, 2)
        cv2.polylines(img, [poly.reshape((-1, 1, 2))], True, color=(0, 0, 255), thickness=2)
    return img



cap = cv2.VideoCapture('shelf17.avi')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    label = give_class(frame)

    bboxes, polys, score_text = look(frame)


    # print (score_text)
    # frame = file_utils.saveResult("image_path", frame[:,:,::-1], polys)
    frame = polygon(frame, polys)
    # print (frame)
    image = cv2.putText(frame, label, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()