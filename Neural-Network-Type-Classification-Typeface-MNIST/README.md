# Neural Network Typeface Classification using MNIST-like Dataset

## Overview

This project builds a **Neural Network** model to classify handwritten typeface characters using a dataset similar to MNIST. It explores how different typeface styles can be accurately predicted by training a deep learning model on labeled pixel image data.

---

## Objective

Train and evaluate a neural network model to classify grayscale images of handwritten characters or digits from various typeface families.

---

## Techniques Used

- Deep learning with fully connected neural networks
- Image reshaping and normalization
- Label encoding
- Model evaluation using:
  - Accuracy
  - Confusion Matrix
  - Loss/Accuracy curves

---

## Tools & Libraries

- Python
- TensorFlow / Keras
- NumPy, Pandas
- Matplotlib
- Scikit-learn

---

## 🧹 Data Preprocessing

- Normalized image pixel values (0–255 to 0–1)
- Reshaped image data into input vectors
- Encoded categorical labels (typeface names)
- Split dataset into training and test sets

---

## Model Architecture

- Input layer matching flattened image size
- One or more hidden layers with ReLU activation
- Output layer with softmax activation (for multi-class classification)
- Optimizer: Adam
- Loss: Categorical Crossentropy

---

## Results

- Achieved high accuracy on training and validation sets
- Visualized:
  - Training/Validation Loss
  - Accuracy curves
  - Confusion matrix
- Model demonstrates robust classification of different typefaces

---

## Project Structure

```
Neural-Network-Typeface-Classification/
│
├── Neural_Network_Type_Classification_Typeface_MNIST.ipynb  # Main notebook
├── README.md                                                 # Project documentation
├── .gitignore                                                # Git ignore rules
```

---

## Disclaimer

The dataset used in this project may be based on or inspired by MNIST-type handwritten character data. All modeling and visualization are for educational purposes.

---

## Author

**Sathwik Hegde**