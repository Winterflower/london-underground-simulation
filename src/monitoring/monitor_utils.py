"""
Functions used to monitor resources - developed with the guidance from Simpy documentation page
Copied from https://simpy.readthedocs.io/en/latest/topical_guides/monitoring.html - only for
demo/testing.
"""

from functools import partial, wraps
import simpy
import logging

def patch_resource(resource, pre=None, post=None):
    def get_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if pre:
                logging.info('Calling pre function')
                pre(resource) 
            ret = func(*args, **kwargs)
            if post:
                logging.info('Calling post function')
                post(resource)
            return ret
        return wrapper
    for name in ['put', 'get', 'request', 'release']:
        if hasattr(resource, name):
            setattr(resource, name, get_wrapper(getattr(resource, name)))



