import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

def __main__(value: float) -> dict:
    logger.info("Received input: value=%.2f", value)
    
    if not isinstance(value, (int, float)):
        logger.error("Invalid input type: value=%s", type(value).__name__)
        raise ValueError("Input value must be a number (int or float)")
        
    result = {"bin": bin}
    logger.info("Returning result: %s", result)
    return  result