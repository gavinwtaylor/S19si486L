import argparse,os

parser=argparse.ArgumentParser()
parser.add_argument("gpu",type=int)
args=parser.parse_args()

gpu=args.gpu
assert gpu>=0 and gpu<4

os.environ["CUDA_VISIBLE_DEVICES"]=str(gpu)
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model 
from keras.layers import Flatten, Dense
from keras import backend as k 
from keras.callbacks import ModelCheckpoint, EarlyStopping

img_width, img_height = 256, 256
train_data_dir = "/home/public/coil100/training"
validation_data_dir = "/home/public/coil100/test"
nb_train_samples = sum([len(files) for r,d,files in os.walk(train_data_dir)])
nb_validation_samples = sum([len(files) for r,d,files in os.walk(validation_data_dir)]) 
batch_size = 16
epochs = 50

model = applications.VGG16(weights = "imagenet", include_top=False, input_shape = (img_width, img_height, 3))

#TODO: How many to freeze? This freeze the first 11
#for layer in model.layers[:11]:
  #layer.trainable=False
  #print(layer)

x=Flatten()(model.output)
#TODO: Add some dense layers here, for example,
#x = Dense(2056, activation="relu")(x)
#adds a dense layer of 2056 neurons.  I might want several dense layers

#must end with this, to have our 100 classes
predictions = Dense(100, activation="softmax")(x)

model_final=Model(inputs = model.input, outputs = predictions)

#TODO: what learning rate?
model_final.compile(loss="categorical_crossentropy",optimizer=optimizers.Adam(),metrics=['acc'])

# Initiate the train and test generators with data Augumentation 
train_datagen = ImageDataGenerator(
    rescale = 1./255,
    horizontal_flip = True,
    fill_mode = "nearest",
    zoom_range = 0.3,
    width_shift_range = 0.3,
    height_shift_range=0.3,
    rotation_range=30)

test_datagen = ImageDataGenerator(
    rescale = 1./255,
    horizontal_flip = True,
    fill_mode = "nearest",
    zoom_range = 0.3,
    width_shift_range = 0.3,
    height_shift_range=0.3,
    rotation_range=30)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size = (img_height, img_width),
    batch_size = batch_size, 
    class_mode = "categorical")

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size = (img_height, img_width),
    class_mode = "categorical")

# Save the model according to the conditions
checkpoint = ModelCheckpoint("vgg16_1.h5", monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
early = EarlyStopping(monitor='val_acc', min_delta=0, patience=10, verbose=1, mode='auto')


# Train the model 
model_final.fit_generator(
    train_generator,
    samples_per_epoch = nb_train_samples,
    epochs = epochs,
    validation_data = validation_generator,
    callbacks = [checkpoint, early])

