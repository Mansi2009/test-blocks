import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

def __main__(probability:float):
    logger.info("Received input: probability=%.2f", probability)
    
    if not isinstance(probability, (int, float)):
        logger.error("Invalid input type: probability=%s", type(probability).__name__)
        raise ValueError("Input probability must be a number (int or float)")
    
    if probability <= 0.26:
        grade = "A1"
    elif 0.26 < probability <= 0.38:
        grade = "A2"
    elif 0.38 < probability <= 0.52:
        grade =  "B1"
    elif 0.52 < probability <= 0.652:
        grade =  "B2"
    elif 0.652 < probability <= 0.7:
        grade =  "C1"
    else:
        grade = "C2"
        
    return {"grade":grade}