import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

def __main__(value: float) -> dict:
    """
    Main function to categorize a float value into a grade.

    :param value: Numeric value (expected float or convertible to float)
    :bin = : Dictionary containing the categorized grade
    :raises ValueError: If input value is not numeric
    """
    logger.info("Received input: value=%.2f", value)
    
    if not isinstance(value, (int, float)):
        logger.error("Invalid input type: value=%s", type(value).__name__)
        raise ValueError("Input value must be a number (int or float)")
    
    if value <= 0.219999999999999:
        bin = "A1"
    elif 0.219999999999999 < value <= 0.339999999999999:
        bin = "A2"
    elif 0.339999999999999 < value <= 0.419999999999999:
        bin = "B1"
    elif 0.419999999999999 < value <= 0.514999999999999:
        bin = "B2"
    elif 0.514999999999999 < value <= 0.559999999999999:
        bin = "C1"
    else:
        bin = "C2"
        
    result = {"bin": bin}
    logger.info("Returning result: %s", result)
    return  result