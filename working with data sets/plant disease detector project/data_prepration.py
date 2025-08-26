import os
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# Define directories
BASE_DIR = "plantvillage_dataset"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")
TEST_DIR = os.path.join(BASE_DIR, "test")

# Create directories if they don't exist
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VAL_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# Load PlantVillage dataset from TensorFlow Datasets
dataset, info = tfds.load('plant_village', with_info=True, as_supervised=True, split=['train'])
dataset = dataset[0]  # Get the training split

# Parameters
IMG_SIZE = (224, 224)  # For ResNet compatibility
BATCH_SIZE = 32

# Function to save images to directories
def save_images(dataset, split_dir, split_name):
    for i, (image, label) in enumerate(tfds.as_numpy(dataset)):
        label_str = str(label)
        class_dir = os.path.join(split_dir, label_str)
        os.makedirs(class_dir, exist_ok=True)
        image_path = os.path.join(class_dir, f"{split_name}_{i}.jpg")
        tf.keras.preprocessing.image.save_img(image_path, image)

# Split dataset: 80% train, 10% validation, 10% test
total_size = info.splits['train'].num_examples
train_size = int(0.8 * total_size)
val_size = int(0.1 * total_size)

train_dataset = dataset.take(train_size)
val_dataset = dataset.skip(train_size).take(val_size)
test_dataset = dataset.skip(train_size + val_size)

# Save images to respective directories
print("Saving images to directories...")
save_images(train_dataset, TRAIN_DIR, "train")
save_images(val_dataset, VAL_DIR, "val")
save_images(test_dataset, TEST_DIR, "test")

# Data augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Only rescaling for validation/test
val_test_datagen = ImageDataGenerator(rescale=1./255)

# Create data generators
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_generator = val_test_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

test_generator = val_test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Save class labels for later use in Streamlit
class_indices = train_generator.class_indices
with open("class_labels.txt", "w") as f:
    for class_name, index in class_indices.items():
        f.write(f"{index}:{class_name}\n")

print("Dataset preparation complete! Train, validation, and test sets are ready.")