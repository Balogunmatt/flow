import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f_hand = logging.FileHandler('decor.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
f_hand.setFormatter(formatter)
logger.addHandler(f_hand)
s_hand = logging.StreamHandler()
s_hand.setFormatter(formatter)
logger.addHandler(s_hand)
# a decorator is a function which takes another function as an argument and returns a function
# the function returned by the main function executes the function that is passed into the main function as an argument
# the argument passed into the inner function should be the same passed into the function used as an argument by the main function

# example:
def dec_func(original_func):
    def wrap_func(*args, **kwargs):
        logger.info(f'this is also an inner function executes the {original_func.__name__}')
        return original_func(*args, **kwargs)
    return wrap_func
@dec_func
# the fucntion argument is executed straight away by writing the above syntax
def disp_func(wrd):
    logger.info(f'displaying the {wrd} as passed')
try:
    disp_func('word')
except Exception as f:
    logger.error(f)

# my_dec = dec_func(disp_func)
# logger.info(my_dec)
# logger.info(my_dec())
