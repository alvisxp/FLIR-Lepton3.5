from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

def get_ir_image():
    
    return Image.open("/tmp/ir.png")

def ktoc(val):
    return (val - 27315) / 100.0
    
ir = get_ir_image()
ir_arr = np.array(ir) 
ir_arr = ir_arr[:-2, :] # trim the 2 bottom lines (telemetry)
ir_arr = ktoc(ir_arr) # Convert to Celsius
ir_arr_big = cv2.resize(ir_arr, (1024, 768))

plt.figure(figsize=(10,10))
plt.imshow(ir_arr_big, cmap='bone')
print(ir_arr)
    