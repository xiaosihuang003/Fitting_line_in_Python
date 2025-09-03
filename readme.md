# Linear Regression with Gradient Descent

A Python implementation of linear regression using gradient descent optimization with interactive mouse-based data point collection.

## Features

- **Interactive Point Collection**: Left-click to add data points, press ENTER to fit the linear model
- **Gradient Descent Optimization**: Finds optimal parameters by minimizing MSE loss function
- **Real-time Visualization**: Live plotting of data points and fitted line
- **Mathematical Foundation**: Implements partial derivative calculations based on MSE minimization

## Mathematical Background

The program solves the linear regression problem `y = ax + b` by minimizing the Mean Squared Error (MSE) loss function:

$$L_{MSE}(a, b) = \frac{1}{N} \sum_{i=1}^{N} (y_i - (a \cdot x_i + b))^2$$

The optimal parameters are found where the gradient is zero:
$$\frac{\partial L_{MSE}}{\partial a} = 0, \quad \frac{\partial L_{MSE}}{\partial b} = 0$$

## Installation

1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd Fitting_line_in_Python
    ```

2.  Create and activate conda environment:
    ```bash
    conda create -n dataml100 python=3.8
    conda activate dataml100
    ```

3.  Install required packages:
    ```bash
    pip install numpy matplotlib
    ```

## Usage

Run the main script:
```bash
python fit_line.py

