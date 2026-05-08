def get_bmi_advice(bmi):
    if bmi < 18.5:
        return "You are underweight. Consider eating a balanced diet and consulting a doctor if needed."
    if bmi < 25:
        return "You are in the healthy range. Keep up your good habits."
    if bmi < 30:
        return "You are overweight. Regular exercise and balanced meals may help."
    return "You are in the obesity range. It may help to speak with a healthcare professional."


def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(get_bmi_advice(bmi))


if __name__ == "__main__":
    main()
