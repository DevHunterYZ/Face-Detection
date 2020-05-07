import cv2
yuzCascade = cv2.CascadeClassifier('C:/Users/.../opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
gozCascade = cv2.CascadeClassifier('C:/Users/.../opencv/build/etc/haarcascades/haarcascade_eye.xml')
gulusCascade = cv2.CascadeClassifier('C:/Users/.../opencv/build/etc/haarcascades/haarcascade_smile.xml')

kamera = cv2.VideoCapture(0)
kamera.set(3,1280)
kamera.set(4,720)
dosyaad = None
kaydedici = None
while True:
    ret, kare = kamera.read()
    # kare = cv2.flip(kare, -1)
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    yuzler = yuzCascade.detectMultiScale(
            gri,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (20,20)
            )
    for (x,y,w,h) in yuzler:
        cv2.ellipse(kare, (int(x+w/2), int(y+h/2)),
                    (w//2 , h//2), 5, 0, 360,(255,0,0),2)
        gri_kutu = gri[y:y+h, x:x+w]
        renkli_kutu = kare[y:y+h, x:x+w]
        
        gozler = gozCascade.detectMultiScale(
            gri_kutu,
            scaleFactor = 1.05,
            minNeighbors = 5,
            minSize = (40,40)
        )
        for (ex, ey, ew, eh) in gozler:
            cv2.ellipse(renkli_kutu, (int(ex+ew/2), int(ey+eh/2)), 
            (int(ew/2), int(eh/2)), 5,0,360,(0,255,0),2)
        gulusler = gulusCascade.detectMultiScale(
            gri_kutu,
            scaleFactor = 1.5,
            minNeighbors = 20,
            minSize = (60,60)
                    
        )
        for (sx, sy, sw, sh) in gulusler:
                cv2.rectangle(renkli_kutu, (sx, sy),
                              (sx + sw, sy + sh), (0, 0, 255),2)
    cv2.imshow('kare',kare)
    if kaydedici is None and dosyaad is not None:
        fourcc = cv2.VideoWriter_fourcc(*"mpv")
        kaydedici = cv2.VideoWriter(dosyaad, fourcc, 24.0,
                                 (kare.shape[1], kare.
shape[0]), True)
    if kaydedici is not None:
        kaydedici.write(kare)
        k=cv2.waitKey(10) & 0xff
        if k == 27 or k == ord('q'):
            break
kamera.release()
if kaydedici:
    kaydedici.release()
cv2.destroyAllWindows()
