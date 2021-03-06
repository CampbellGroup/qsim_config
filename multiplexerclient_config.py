class multiplexer_config(object):
    '''
    multiplexer client configuration file
    
    Attributes
    ----------
    info: dict
    {channel_name: (port, hint, display_location, stretched, display_pid, dac, dac_rails)}
    '''
    info = {
        '935': (4, '320.571975', (0, 3), True, True, 7, [0.0, 10.0]),
        '760': (5, '555.424', (0, 4), True, True, 5, [-.4, 0.4]),
        '780': (1, '384.571975', (0, 5), True, False, 1, [0.0, 10.0]),
        '760 (Repump)': (2, '494.424', (4, 4), True, True, 6, [-1.0, 1.0]),
        '822': (3, '729.475800', (4, 3), True, True, 3, [-10.0, 10.0]),
        #'822': (1, '364.737', (0, 5), True, True, 1, [-10.0, 10.0]),
        '976': (7, '307.058', (4, 5), True, True, 4, [-10.0, 10.0]),
        #'1108': (6, '270.430', (0, 5), True, True, 2, [0.0, 10.0]),
            }
    ip = '10.97.112.2'
