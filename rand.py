from flirpy.camera.lepton import Lepton
import cv2
import matplotlib.pyplot as plt
cam = Lepton()
image = cam.grab()
print(image)
plt.imshow(image)

print(image)
print(cam.frame_count)
print(cam.frame_mean)
print(cam.ffc_temp_k)
print(cam.fpa_temp_k)
cam.close()

import cv2
import numpy as np
from flirpy.camera.lepton import Lepton

with Lepton() as camera:
    while True:
        img = camera.grab().astype(np.float32)

        img = 255*(img - img.min())/(img.max()-img.min())

        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)

        rez = cv2.resize(img_col, (700, 500))
        cv2.imshow('Thermal Feed', rez)

        np.savetxt('newtemp.xls', img, fmt = '%.4f', delimiter=' ')
        if cv2.waitKey(1) &0xFF == ord('q'):
            break


        
cv2.destroyAllWindows()

