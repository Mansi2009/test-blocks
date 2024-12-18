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
    
    if value <= 0.33:
        bin = "G1"
    elif 0.33 < value <= 0.41:
        bin = "G2"
    elif 0.41 < value <= 0.48:
        bin = "G3"
    elif 0.48 < value <= 0.61:
        bin = "G4"
    elif 0.61 < value <= 0.65:
        bin = "G5"
    else:
        bin = "G6"
        
    result = {"bin": bin}
    logger.info("Returning result: %s", result)
    return  result