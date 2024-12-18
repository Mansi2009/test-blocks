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
    
    if value <= 0.3200099998:
        bin = "1"
    elif 0.3200099998 < value <= 0.4459999998:
        bin = "2"
    elif 0.4459999998 < value <= 0.5394999999:
        bin = "3"
    elif 0.5394999999 < value <= 0.6186978508:
        bin = "4"
    elif 0.6186978508 < value <= 0.6350320994:
        bin = "5"
    elif 0.6350320994 < value <= 0.6553314835:
        bin = "6"
    elif 0.6553314835 < value <= 0.6759955555:
        bin = "7"
    elif 0.6759955555 < value <= 0.7399999999:
        bin = "8"
    elif 0.7399999999 < value <= 0.7899992753:
        bin = "9"
    elif 0.7899992753 < value <= 0.8199900001:
        bin = "10"
    elif 0.8199900001 < value <= 0.8400000009:
        bin = "11"
    else:
        bin = "12"
        
    result = {"bin": bin}
    logger.info("Returning result: %s", result)
    return  result