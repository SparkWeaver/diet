# barcode.py
import cv2
from pyzbar.pyzbar import decode


def scan_barcode():
    cap = cv2.VideoCapture(0)
    focus = 0
    cap.set(28, focus)

    while True:
        ret, frame = cap.read()
        barcodes = decode(frame)

        if barcodes:
            myData = barcodes[0].data.decode('utf-8')
            break
        else:
            focus += 1
            cap.set(28, focus)

        cv2.imshow("Result", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return myData
