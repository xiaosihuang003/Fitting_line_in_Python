import numpy as np

def my_linfit(x, y):
    """Use analytical solution for precise linear regression"""
    N = len(x)
    
    # Calculate required sums for least squares formulas
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)
    
    # Compute coefficients using analytical formulas (exact solution)
    denominator = N * sum_x2 - sum_x ** 2
    a = (N * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - a * sum_x) / N
    
    return a, b

def main():
    """Main function with interactive plotting - only executed when run as script"""
    try:
        import matplotlib.pyplot as plt
        
        # Initialize list to store points
        points = []
        
        # Create figure window
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title('Left click: add point, Press ENTER key: fit line')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.grid(True)
        
        # Mouse click event handler
        def onclick(event):
            if event.button == 1:  # Left click
                x, y = event.xdata, event.ydata
                points.append((x, y))
                print(f"Added point: ({x:.2f}, {y:.2f})")
                
                # Update scatter plot
                x_vals = [p[0] for p in points]
                y_vals = [p[1] for p in points]
                ax.scatter(x_vals, y_vals, color='blue')
                plt.draw()
        
        # Keyboard event handler
        def onkey(event):
            if event.key == 'enter' and len(points) >= 2:
                # Extract coordinates
                x_vals = np.array([p[0] for p in points])
                y_vals = np.array([p[1] for p in points])
                
                print("\nComputing linear regression using analytical solution...")
                
                # Use analytical solution for fitting
                a, b = my_linfit(x_vals, y_vals)
                
                # Plot fitted line
                x_fit = np.linspace(min(x_vals)-1, max(x_vals)+1, 100)
                y_fit = a * x_fit + b
                ax.plot(x_fit, y_fit, 'r-', linewidth=2, 
                       label=f'y = {a:.6f}x + {b:.6f}')
                
                # Add legend
                ax.legend()
                plt.draw()
                
                print(f"\nFinal result: a = {a:.12f}, b = {b:.12f}")
                print(f"Linear equation: y = {a:.12f}x + {b:.12f}")
                print("Analytical solution - mathematically exact!")
        
        # Connect events
        fig.canvas.mpl_connect('button_press_event', onclick)
        fig.canvas.mpl_connect('key_press_event', onkey)
        
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Running in headless mode.")
        print("The my_linfit function is available for import and testing.")

if __name__ == '__main__':
    main()