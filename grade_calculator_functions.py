# grade_calculator_functions.py

def get_student_score() -> float:
    """
    Prompts the user to input their score and ensures it is a valid number.
    
    Returns:
        float: The student's score as a numerical value.
    """
    while True:
        try:
            score = float(input("Enter your score: "))  # Try to convert the input to a float
            if 0 <= score <= 100:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the score.
    
    Args:
        score (float): The numerical score to evaluate.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main Program Flow
def main():
    score = get_student_score()  # Get the score from the user
    grade = calculate_grade(score)  # Calculate the grade
    print(f"Your Grade is: {grade}")  # Display the grade

# If the script is being run directly, call the main function
if __name__ == "__main__":
    main()
