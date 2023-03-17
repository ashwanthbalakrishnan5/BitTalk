#import keys
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

#config_logging(logging, logging.DEBUG)


def Positions(key, secret):
    um_futures_client = UMFutures(key, secret)
    try:
        response = um_futures_client.get_position_risk(recvWindow=6000)
        i = len(response)-1
        while (i >= 0):
            if float(response[i]['positionAmt']) == 0:
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
