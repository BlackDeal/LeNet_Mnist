LENET_INPUT_H = 32
LENET_INPUT_W = 32

BATCH_SIZE = 100

IMAGE_W = 28
IMAGE_H = 28
LABEL_SIZE = 10

DATASET_PATH = "mnist_dataset"

# training config
LEARNING_RATE_BASE = 0.01
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 20000
MOVING_AVERAGE_DECAY = 0.99