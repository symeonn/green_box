import logging

logs_path = '/home/pi/gb_data/gb_logs/'


def init(log_name):
    logging.basicConfig(format='%(asctime)s :: %(levelname)s: %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S',
                        level=logging.DEBUG,
                        filename=logs_path + log_name)


def debug(msg, *args, **kwargs):
    logging.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    logging.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    logging.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    logging.error(msg, *args, **kwargs)
