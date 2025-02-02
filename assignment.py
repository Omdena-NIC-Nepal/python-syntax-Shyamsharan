def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return(f"My name is {name} and I am {age} years old.")


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10: 
        return "Greater"
    if number < 10:
        return "Lesser"
    if number == 10:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    i = 1
    added_values = 0
    while i <= n:
        added_values += i
        i = i+1
    return(added_values)
    
def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return(0, None, None)
    return(sum(numbers), max(numbers), min(numbers))



def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    Student = []
    for item in students_dict:
        if students_dict[item]> 80:
            Student.append(item)
    return Student

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1) & set(list2)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {
        'Sum': a + b,
        'Difference': a - b, 
        'Multiplication': a * b, 
        'Power': a ** b, 
        'Remainder': a / b if b!= 0 else "Not possible to divide by zero"
        }


def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        'and operation': x and y ,
        'or operation': x or y,
        'xor operation': x != y, 
        'not x operation': not x, 
        'not y operation': not y,
        }

def bitwise_ops(a, b):
    """
    Perform bitwise operations. 
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        'bitwise and ': a & b,
        'bitwise or ': a | b, 
        'bitwise xor': a ^ b,
        'bitwise left_shift': a << b,
        'bitwise right_shift': a >>b
        }
