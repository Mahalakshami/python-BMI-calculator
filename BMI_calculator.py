try:
    # Get user input
    height = float(input("Enter your height (in meters): "))
    weight = float(input("Enter your weight (in kilograms): "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Categorize health
    if bmi < 18.5:
        health_category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        health_category = "Normal weight"
    elif 25 <= bmi < 29.9:
        health_category = "Overweight"
    else:
        health_category = "Obesity"

    # Display results
    print(f"\nBMI: {bmi:.2f}")
    print(f"Health Category: {health_category}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Height should not be zero.")
