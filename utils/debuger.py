import logging

from django.db import connection, reset_queries
import time


def debug_queries(func):
    def wrapper(*args, **kwargs):
        reset_queries()
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        logging.getLogger('apm').debug('<------------------------------------------------>\n')
        logging.getLogger('apm').debug('Total time: %s \n' % (end - start))
        logging.getLogger('apm').debug('Total queries: %s \n' % len(connection.queries))
        for query in connection.queries:
            logging.getLogger('apm').debug('Query: %s *---* Time : %s' % (query['sql'], query['time']))
        return res

    return wrapper
