"""
This program asks the user for their weight in pounds and height in feet and inches,
then calculates and displays their Body Mass Index (BMI) to one decimal place.

BMI categories are based on CDC (Centers for Disease Control and Prevention) guidelines:
- Underweight: less than 18.5
- Normal weight: 18.5 – 24.9
- Overweight: 25.0 – 29.9
- Obesity: 30.0 and above
Source: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
"""

# Unit conversion
poundsToKilo = 0.4536
inPerFt = 12
inToM = 0.0254

# Getting the user's measurments.
def getUserInfo():
    """Prompt the user for their weight in pounds and height in feet and inches."""
    weightLbs = float(input("Enter your weight (in pounds): "))
    heightFt = int(input("Enter your height (feet): "))
    heightIn = int(input("Enter your remaining height (inches): "))
    return weightLbs, heightFt, heightIn

#Coverting all imperial units to metric
def convertToM(weightLbs, heightFt, heightIn):
    """Convert imperial units to metric (kilograms and meters)."""
    weightKg = weightLbs * poundsToKilo
    totalIn = heightFt * inPerFt + heightIn
    heightM = totalIn * inToM
    return weightKg, heightM

def calculateBMI(weightKg, heightM):
    """Calculate BMI using the formula: BMI = weight (kg) / [height (m)]^2"""
    bmi = weightKg / (heightM ** 2)
    return bmi

def displayResults(bmi):
    """Display the BMI value and BMI category legend."""
    print(f"\nYour BMI is: {bmi:.1f}")
    print("\nBMI Categories (Source: CDC)")
    print("Underweight: less than 18.5")
    print("Normal weight: 18.5 – 24.9")
    print("Overweight: 25.0 – 29.9")
    print("Obesity: 30.0 and above")

def main():
    """Main program execution."""
    weightLbs, heightFt, heightIn = getUserInfo()
    weightKg, heightM = convertToM(weightLbs, heightFt, heightIn)
    bmi = calculateBMI(weightKg, heightM)
    displayResults(bmi)

# Run the program
if __name__ == "__main__":
    main()
