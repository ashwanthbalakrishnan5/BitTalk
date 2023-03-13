#import keys
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

#config_logging(logging, logging.DEBUG)


def Balance(key, secret):
    um_futures_client = UMFutures(key, secret)
    i = 9
    try:
        response = um_futures_client.balance(recvWindow=60000)
        while (i >= 0):
            if float(response[i]['availableBalance']) == 0.00:
                del response[i]
            i -= 1
        return response
    # logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
