import keys
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

#config_logging(logging, logging.DEBUG)

key = keys.api
secret = keys.secretKey

um_futures_client = UMFutures(key=key, secret=secret)

try:
    response = um_futures_client.get_orders(recvWindow=2000)
    # logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
for i in response:
    print("\n")
    print(i)
    print("\n")
