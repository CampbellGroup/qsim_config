class switch_config(object):
    '''
    configuration file for multiplexer client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted)), }
    '''
    info = {
            '399 Loading': (10, (1, 0), True),
            'State Detection Shutter': (12, (3, 0), False),
            'Protection Beam': (9, (5, 0), False)
    }

