import socket
import sys
import cv2 as cv
import time
import os
def main():
    s = socket.socket()
    mydir = '/home/jayraj/Jayraj/VBA/6CEB/'
    print('Socket successfully created')
    port = 12345
    s.bind(('',port))
    s.listen(5)      
    print ("socket is listening" )
    while True: 
        c, addr = s.accept()
        print ('Got connection from', addr )
        message = c.recv(1024).decode('utf-8')
        print(message)
        if not message == '':
            filelist = [ f for f in os.listdir(mydir) if f.endswith(".jpg") ]
            for f in filelist:
                os.remove(os.path.join(mydir, f))
            video_capture = cv.VideoCapture(0)
            
            # if message.split('_')[0] == 't':
            while True:
                ret, frame = video_capture.read()
                cv.imshow('Video', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    filename = '/home/jayraj/Jayraj/VBA/6CEB/'+message
                    cv.imwrite(filename+'.jpg',frame)
                    break
            # else:
            #     maxFrames = 10
            #     cpt = 0

            #     while cpt < maxFrames:
            #         ret, frame = video_capture.read()
            #         if not ret: 
            #             sys.exit(0)
            #         filename = '/home/jayraj/Jayraj/VBA/6CEB/'+message + '_'+str(cpt+1) + '.jpg'
            #         cv.imshow("Move your head in towards left.. Pause.. Now towards right...", frame)
            #         cv.imwrite(filename, frame)
            #         time.sleep(0.8)
            #         cpt += 1

        video_capture.release()
        cv.destroyAllWindows()
        c.send('ok'.encode('utf-8'))

       
if __name__ == '__main__':
    main()