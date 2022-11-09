from decorator import logger


@logger
def get_employees():
    print('get_employees')