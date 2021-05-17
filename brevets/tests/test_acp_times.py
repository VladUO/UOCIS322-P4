from acp_times import open_time, close_time

import logging
import nose
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

time = arrow.get("2021-01-01T01:01", 'YYYY-MM-DDTHH:mm')

def test_200():
    assert open_time(0, 200, time) == arrow.get('2021-01-01 01:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(0, 200, time) == arrow.get('2021-01-01 02:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(50, 200, time) == arrow.get('2021-01-01 02:29', 'YYYY-MM-DDTHH:mm')
    assert close_time(50, 200, time) == arrow.get('2021-01-01 04:31', 'YYYY-MM-DDTHH:mm')

    assert open_time(100, 200, time) == arrow.get('2021-01-01 03:57', 'YYYY-MM-DDTHH:mm')
    assert close_time(100, 200, time) == arrow.get('2021-01-01 07:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(150, 200, time) == arrow.get('2021-01-01 05:26', 'YYYY-MM-DDTHH:mm')
    assert close_time(150, 200, time) == arrow.get('2021-01-01 11:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(200, 200, time) == arrow.get('2021-01-01 06:54', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 200, time) == arrow.get('2021-01-01 14:31', 'YYYY-MM-DDTHH:mm')


def test_300():
    assert open_time(50, 300, time) == arrow.get('2021-01-01 02:29', 'YYYY-MM-DDTHH:mm')
    assert close_time(50, 300, time) == arrow.get('2021-01-01 04:31', 'YYYY-MM-DDTHH:mm')

    assert open_time(100, 300, time) == arrow.get('2021-01-01 03:57', 'YYYY-MM-DDTHH:mm')
    assert close_time(100, 300, time) == arrow.get('2021-01-01 07:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(200, 300, time) == arrow.get('2021-01-01 05:26', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 300, time) == arrow.get('2021-01-01 11:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(300, 300, time) == arrow.get('2021-01-01 10:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(300, 300, time) == arrow.get('2021-01-01 21:01', 'YYYY-MM-DDTHH:mm') 

    assert open_time(330, 400, time) == arrow.get('2021-01-01 10:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(330, 400, time) == arrow.get('2021-01-01 21:01', 'YYYY-MM-DDTHH:mm')    

def test_400():
    assert open_time(200, 400, time) == arrow.get('2021-01-01 06:54', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 400, time) == arrow.get('2021-01-01 14:21', 'YYYY-MM-DDTHH:mm')

    assert open_time(250, 400, time) == arrow.get('2021-01-01 08:28', 'YYYY-MM-DDTHH:mm')
    assert close_time(250, 400, time) == arrow.get('2021-01-01 17:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(300, 400, time) == arrow.get('2021-01-01 10:01', 'YYYY-MM-DDTHH:mm')
    assert close_time(300, 400, time) == arrow.get('2021-01-01 21:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(350, 400, time) == arrow.get('2021-01-01 11:35', 'YYYY-MM-DDTHH:mm')
    assert close_time(350, 400, time) == arrow.get('2021-01-02 00:21', 'YYYY-MM-DDTHH:mm') 

    assert open_time(400, 400, time) == arrow.get('2021-01-01 13:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(400, 400, time) == arrow.get('2021-01-02 04:01', 'YYYY-MM-DDTHH:mm')    

def test_600():
    assert open_time(400, 600, time) == arrow.get('2021-01-01 13:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(400, 600, time) == arrow.get('2021-01-02 03:41', 'YYYY-MM-DDTHH:mm')

    assert open_time(450, 600, time) == arrow.get('2021-01-01 14:49', 'YYYY-MM-DDTHH:mm')
    assert close_time(450, 600, time) == arrow.get('2021-01-02 07:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(500, 600, time) == arrow.get('2021-01-01 16:29', 'YYYY-MM-DDTHH:mm')
    assert close_time(500, 600, time) == arrow.get('2021-01-02 10:21', 'YYYY-MM-DDTHH:mm')

    assert open_time(550, 600, time) == arrow.get('2021-01-01 18:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(550, 600, time) == arrow.get('2021-01-02 13:41', 'YYYY-MM-DDTHH:mm') 

    assert open_time(600, 600, time) == arrow.get('2021-01-01 19:49', 'YYYY-MM-DDTHH:mm')
    assert close_time(600, 600, time) == arrow.get('2021-01-02 17:01', 'YYYY-MM-DDTHH:mm')     

def test_1000():
    assert open_time(600, 1000, time) == arrow.get('2021-01-01 19:49', 'YYYY-MM-DDTHH:mm')
    assert close_time(600, 1000, time) == arrow.get('2021-01-02 17:01', 'YYYY-MM-DDTHH:mm')

    assert open_time(700, 1000, time) == arrow.get('2021-01-01 23:23', 'YYYY-MM-DDTHH:mm')
    assert close_time(700, 1000, time) == arrow.get('2021-01-03 01:46', 'YYYY-MM-DDTHH:mm')

    assert open_time(800, 1000, time) == arrow.get('2021-01-02 02:58', 'YYYY-MM-DDTHH:mm')
    assert close_time(800, 1000, time) == arrow.get('2021-01-03 10:31', 'YYYY-MM-DDTHH:mm')

    assert open_time(900, 1000, time) == arrow.get('2021-01-02 06:32', 'YYYY-MM-DDTHH:mm')
    assert close_time(900, 1000, time) == arrow.get('2021-01-03 19:16', 'YYYY-MM-DDTHH:mm') 

    assert open_time(1000, 1000, time) == arrow.get('2021-01-02 10:06', 'YYYY-MM-DDTHH:mm')
    assert close_time(1000, 1000, time) == arrow.get('2021-01-04 04:01', 'YYYY-MM-DDTHH:mm')        