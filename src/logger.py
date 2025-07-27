# logger.py

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name based on current timestamp
LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',  # Append mode
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


if __name__=="__main__" :
 logging.info("logging has started")
        