# main.py - simple BMI calculator

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError as e:
            print("Invalid input:", e)

def main():
    print("BMI Calculator")
    weight = get_float("Enter weight (kg): ")
    height_cm = get_float("Enter height (cm): ")
    height_m = height_cm / 100.0
    bmi = calculate_bmi(weight, height_m)
    print(f"Your BMI is: {bmi:.2f}")
    print("Category:", bmi_category(bmi))

if __name__ == "__main__":
    main()
