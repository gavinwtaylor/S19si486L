import argparse,os

parser=argparse.ArgumentParser()
parser.add_argument("gpu",type=int)
parser.add_argument("image",)
args=parser.parse_args()

gpu=args.gpu
image_fn=args.image
assert gpu>=0 and gpu<4

os.environ["CUDA_VISIBLE_DEVICES"]=str(gpu)

# Import Libraries
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
# Process Model
model = VGG16()
print(model.summary())
image = load_img(image_fn, target_size=(224, 224))
image = img_to_array(image)
gs_image=np.mean(image,axis=2)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)
# Generate predictions
pred = model.predict(image)
print('Predicted:', decode_predictions(pred, top=3)[0])
np.argmax(pred[0])

specoutput=model.output[:, 668]
chosen_layer = model.get_layer('block5_pool')
grads = K.gradients(specoutput, chosen_layer.output)[0]
pooled_grads = K.mean(grads, axis=(0, 1, 2))
iterate = K.function([model.input], [pooled_grads, chosen_layer.output[0]])
pooled_grads_value, conv_layer_output_value = iterate([image])
for i in range(chosen_layer.output_shape[-1]):
  conv_layer_output_value[:, :, i] *= pooled_grads_value[i]
heatmap=np.mean(conv_layer_output_value, axis=-1)
# Heatmap post processing
heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap)
fig=plt.figure(frameon=False)
extent=0,255,0,255
plt.imshow(gs_image,cmap=plt.cm.gray,extent=extent)
plt.imshow(heatmap,alpha=.75,extent=extent,interpolation='bilinear')
plt.show()
