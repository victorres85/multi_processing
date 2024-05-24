from multiprocessing import get_logger
import logging

def logger(level=logging.INFO) -> logging.Logger:
    ''' centralize logger from multiprocess '''
    log = get_logger()
    log.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(ldvelname)s: %(asctime)s - %(process)s - %(message)s'
    ))
    log.addHandler(handler)
    return log

app_logger = logger()
