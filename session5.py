import numpy as np

def main():
    """
    Main function that tabulates sin(x) vs. x for 1000 points between 0 and 2.
    """
    # Create an array of 1000 equally spaced x values from 0 to 2
    x_values = np.linspace(0, 2, 1000)
    
    # Compute sin(x) for each value of x
    sin_values = np.sin(x_values)
    
    # Print a header for the table
    print(f"{'x':>10} {'sin(x)':>15}")
    print("-" * 26)
    
    # Print the first 10 values as a preview
    for i in range(10):
        print(f"{x_values[i]:10.6f} {sin_values[i]:15.6f}")
    
    # (Optional) If you want to print all 1000 rows, uncomment this:
    # for i in range(len(x_values)):
    #     print(f"{x_values[i]:10.6f} {sin_values[i]:15.6f}")

# Run the program
if __name__ == "__main__":
    main()