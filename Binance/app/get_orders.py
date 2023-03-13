#import keys
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

#config_logging(logging, logging.DEBUG)


def Orders(key, secret):

    um_futures_client = UMFutures(key, secret)

    try:
        response = um_futures_client.get_orders(recvWindow=2000)
        return response

        # logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
