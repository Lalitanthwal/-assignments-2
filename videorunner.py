import cv2

def play_videoFile(filePath,mirror=False):

    cap = cv2.VideoCapture(filePath)
    cv2.namedWindow('Love Me Thoda Aur - Yaariyan_FHD-(HDvideo9).mp4',cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()

        if mirror:
            frame = cv2.flip(frame, 1)

        cv2.imshow('Love Me Thoda Aur - Yaariyan_FHD-(HDvideo9).mp4', frame)

        if cv2.waitKey(1) == 27:
            break  # esc to quit

    cv2.destroyAllWindows()

def main():
    play_videoFile('Love Me Thoda Aur - Yaariyan_FHD-(HDvideo9).mp4',mirror=False)

if __name__ == '__main__':
    main()
