1 file changed
+19
-10
lines changed

 
"""
Grade Calculator Program
This script prompts the user to enter their score, determines their letter grade,
and displays the result.It includes functions for input validation and grading logic.
"""
def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates the input, 
    Prompts the user to enter their score, validates the input,
    and returns the numerical score as a float.
    """
    while True:
        try:
            score = float(input("Enter your score: 90"))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input.Please enter a score between 0 and 100.")
            print("Invalid input.Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input.Please enter a valid numeric score.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    
    Parameters:
    score (float):The student's numerical score.
    
    Returns:
    str:The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return "A"
    elif score >= 80:
    if score >= 80:
        return "B"
    elif score >= 70:
    if score >= 70:
        return "C"
    elif score >= 60:
    if score >= 60:
        return "D"
    else:
        return "F"
    return "F"  # No need for "else", as return ends function execution

# Main program flow
def main():
    """
    Main function that drives the program.
    It gets the user's score,calculates the grade,and prints the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if _name_ == "_main_":
    main()