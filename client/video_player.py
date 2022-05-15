import cv2

def play_video(filename):
    cap = cv2.VideoCapture(filename)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q') or ret==False :
            cap.release()
            cv2.destroyAllWindows()
        cv2.imshow('frame',frame)

if __name__=='__main__':
    play_video("media/scheduled_video.mp4")