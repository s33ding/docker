# Function to perform linear regression prediction
def linear_regression_model(intercept, slope, features):
    return intercept + features * slope

# Function to calculate the Mean Squared Error (MSE) loss
def calculate_mse_loss(intercept, slope, features, targets):
    # Compute the predictions for a linear model
    predictions = linear_regression_model(intercept, slope, features)
    # Calculate and return the MSE loss
    loss = tf.keras.losses.mean_squared_error(targets, predictions)
    return loss
