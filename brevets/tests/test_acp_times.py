from acp_times import open_time, close_time

import logging
import nose
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

time = arrow.get("2021-01-01T01:01", 'YYYY-MM-DDTHH:mm')

def test_200():
    assert open_time(0, 200, time) == arrow.get('2021-01-01T01:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(0, 200, time) == arrow.get('2021-01-01T02:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(50, 200, time) == arrow.get('2021-01-01T02:29', 'YYYY-MM-DDTHH:mm')
    assert close_time(50, 200, time) == arrow.get('2021-01-01T04:31', 'YYYY-MM-DDTHH:mm')

    assert open_time(100, 200, time) == arrow.get('2021-01-01T03:57', 'YYYY-MM-DDTHH:mm')
    assert close_time(100, 200, time) == arrow.get('2021-01-01T07:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(150, 200, time) == arrow.get('2021-01-01T05:26', 'YYYY-MM-DDTHH:mm')
    assert close_time(150, 200, time) == arrow.get('2021-01-01T11:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(200, 200, time) == arrow.get('2021-01-01T06:54', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 200, time) == arrow.get('2021-01-01T14:31', 'YYYY-MM-DDTHH:mm')


def test_300():
    assert open_time(50, 300, time) == arrow.get('2021-01-01T02:29', 'YYYY-MM-DDTHH:mm')
    assert close_time(50, 300, time) == arrow.get('2021-01-01T04:31', 'YYYY-MM-DDTHH:mm')

    assert open_time(100, 300, time) == arrow.get('2021-01-01T03:57', 'YYYY-MM-DDTHH:mm')
    assert close_time(100, 300, time) == arrow.get('2021-01-01T07:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(200, 300, time) == arrow.get('2021-01-01T06:54', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 300, time) == arrow.get('2021-01-01T14:21', 'YYYY-MM-DDTHH:mm')

    assert open_time(290, 400, time) == arrow.get('2021-01-01T09:43', 'YYYY-MM-DDTHH:mm')
    assert close_time(290, 400, time) == arrow.get('2021-01-01T20:21', 'YYYY-MM-DDTHH:mm') 

    assert open_time(300, 300, time) == arrow.get('2021-01-01T10:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(300, 300, time) == arrow.get('2021-01-01T21:01', 'YYYY-MM-DDTHH:mm') 

    
def test_400():
    assert open_time(200, 400, time) == arrow.get('2021-01-01T06:54', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 400, time) == arrow.get('2021-01-01T14:21', 'YYYY-MM-DDTHH:mm')

    assert open_time(250, 400, time) == arrow.get('2021-01-01T08:28', 'YYYY-MM-DDTHH:mm')
    assert close_time(250, 400, time) == arrow.get('2021-01-01T17:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(300, 400, time) == arrow.get('2021-01-01T10:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(300, 400, time) == arrow.get('2021-01-01T21:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(350, 400, time) == arrow.get('2021-01-01T11:35', 'YYYY-MM-DDTHH:mm')
    assert close_time(350, 400, time) == arrow.get('2021-01-02T00:21', 'YYYY-MM-DDTHH:mm') 

    assert open_time(400, 400, time) == arrow.get('2021-01-01T13:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(400, 400, time) == arrow.get('2021-01-02T04:01', 'YYYY-MM-DDTHH:mm')    

def test_600():
    assert open_time(400, 600, time) == arrow.get('2021-01-01T13:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(400, 600, time) == arrow.get('2021-01-02T03:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(450, 600, time) == arrow.get('2021-01-01T14:49', 'YYYY-MM-DDTHH:mm')
    assert close_time(450, 600, time) == arrow.get('2021-01-02T07:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(500, 600, time) == arrow.get('2021-01-01T16:29', 'YYYY-MM-DDTHH:mm')
    assert close_time(500, 600, time) == arrow.get('2021-01-02T10:21', 'YYYY-MM-DDTHH:mm')

    assert open_time(550, 600, time) == arrow.get('2021-01-01T18:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(550, 600, time) == arrow.get('2021-01-02T13:41', 'YYYY-MM-DDTHH:mm') 

    assert open_time(600, 600, time) == arrow.get('2021-01-01T19:49', 'YYYY-MM-DDTHH:mm')
    assert close_time(600, 600, time) == arrow.get('2021-01-02T17:01', 'YYYY-MM-DDTHH:mm')     

def test_1000():
    assert open_time(600, 1000, time) == arrow.get('2021-01-01T19:49', 'YYYY-MM-DDTHH:mm')
    assert close_time(600, 1000, time) == arrow.get('2021-01-02T17:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(700, 1000, time) == arrow.get('2021-01-01T23:23', 'YYYY-MM-DDTHH:mm')
    assert close_time(700, 1000, time) == arrow.get('2021-01-03T01:46', 'YYYY-MM-DDTHH:mm')

    assert open_time(800, 1000, time) == arrow.get('2021-01-02T02:58', 'YYYY-MM-DDTHH:mm')
    assert close_time(800, 1000, time) == arrow.get('2021-01-03T10:31', 'YYYY-MM-DDTHH:mm')

    assert open_time(900, 1000, time) == arrow.get('2021-01-02T06:32', 'YYYY-MM-DDTHH:mm')
    assert close_time(900, 1000, time) == arrow.get('2021-01-03T19:16', 'YYYY-MM-DDTHH:mm') 

    assert open_time(1000, 1000, time) == arrow.get('2021-01-02T10:06', 'YYYY-MM-DDTHH:mm')
    assert close_time(1000, 1000, time) == arrow.get('2021-01-04T04:01', 'YYYY-MM-DDTHH:mm')        