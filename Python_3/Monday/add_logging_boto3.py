import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('boto3')
logger.setLevel(logging.DEBUG)