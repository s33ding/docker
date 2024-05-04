import numpy as np
import pandas as pd
import os
from shared_func import  * 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Input  # Make sure to import Input from the correct module
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve

df = read_file()

#checking missing values
checking_missing_values(df)

# Inicializar o scaler
scaler = MinMaxScaler()

# Normalizar as colunas numéricas
lst_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
df = normalizing_num_data(df=df, numeric_columns=lst_cols)

df.drop(columns=["Surname","RowNumber"], inplace=True)

df1 = df.copy()
# Realizar one-hot encoding para variáveis categóricas
lst_cols = ['Geography', 'Gender']
df = one_hot_encoding(df,lst_cols)

correlation_matrix = create_correlation_matrix(df)
ploting_correlation_matrix(correlation_matrix)
features = analysing_features(df=correlation_matrix, target_col="Exited")
selected_features = features.index[:3].tolist()

y = df['Exited']  # Target variable
for col in df.columns:
    if col not in selected_features:
        df.drop(columns=[col], inplace=True)  

# Convert df to numpy array
X = df.values

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check data types
print("X_train dtype:", X_train.dtype)
print("y_train dtype:", y_train.dtype)

# Preprocess data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
y_train_reshaped = y_train.values.reshape(-1, 1)  # Reshape y_train to column vector if needed

# Convert to tensors
X_train_tensor = tf.convert_to_tensor(X_train_scaled, dtype=tf.float32)
X_test_tensor = tf.convert_to_tensor(X_test_scaled, dtype=tf.float32)
y_train_tensor = tf.convert_to_tensor(y_train_reshaped, dtype=tf.float32)

# Model construction
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_tensor, y_train_tensor, epochs=50, batch_size=32, validation_split=0.2, callbacks=[EarlyStopping(patience=3)])

# Train the model (assuming 'model' is already defined and compiled)
history = model.fit(X_train_tensor, y_train_tensor, epochs=50, batch_size=32, validation_split=0.2, callbacks=[EarlyStopping(patience=3)])

# Evaluate the model on test data
y_pred_proba = model.predict(X_test_tensor)
y_pred = (y_pred_proba > 0.5).astype(int)  # Convert probabilities to binary predictions

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("ROC AUC:", roc_auc)

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
