import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_url = "https://example.com/path/to/your/image.jpg"


response = requests.get(image_url)
img = Image.open(io.BytesIO(response.content)).convert('L')  


I = np.array(img)


Hist = np.zeros(256)


h, w = I.shape


for v in range(h):
    for u in range(w):
        
        intensity = I[v, u]

       
        Hist[intensity] += 1


plt.bar(range(256), Hist, color='gray', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
