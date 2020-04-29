# -*- coding: utf-8 -*-
""" Configuration handler """
import dynamic_dynamodb.config as config

CONFIGURATION = config.get_configuration()


def get_configured_tables():
    """ Returns a list of all configured tables

    :returns: list -- List of tables
    """
    try:
        return CONFIGURATION['tables'].keys()
    except KeyError:
        return []

def get_configured_time_series_key_names():
    """ Returns the list of all configured tables that should be time series tables
    
    :returns: list -- List of tables
    """
    try:
        time_series_key_names = set()
        for key_name in CONFIGURATION['tables'].keys():
            key_config = CONFIGURATION['tables'][key_name]            
            if 'rotate_interval_unit' in key_config and key_config['rotate_interval_unit'] != None:
               time_series_key_names.add( key_name )

        return time_series_key_names                
    except KeyError:
         return []

def get_configured_rotated_key_names():
    """ Returns the list of all configured tables that should be rotated
    
    :returns: list -- List of tables
    """
    try:
        rotated_key_names = set()
        for key_name in CONFIGURATION['tables'].keys():
            key_config = CONFIGURATION['tables'][key_name]            
            if 'rotate_interval' in key_config and key_config['rotate_interval'] != None:
               rotated_key_names.add( key_name )

        return rotated_key_names                
    except KeyError:
         return []
         
         
def get_global_option(option):
    """ Returns the value of the option

    :returns: str or None
    """
    try:
        return CONFIGURATION['global'][option]
    except KeyError:
        return None


def get_gsi_option(table_key, gsi_key, option):
    """ Returns the value of the option

    :type table_key: str
    :param table_key: Table key name
    :type gsi_key: str
    :param gsi_key: GSI key name
    :returns: str or None
    """
    try:
        return CONFIGURATION['tables'][table_key]['gsis'][gsi_key][option]
    except KeyError:
        return None


def get_logging_option(option):
    """ Returns the value of the option

    :returns: str or None
    """
    try:
        return CONFIGURATION['logging'][option]
    except KeyError:
        return None


def get_table_option(table_name, option):
    """ Returns the value of the option

    :type table_name: str
    :param table_name: Name of the DynamoDB table
    :returns: str or None
    """
    try:
        return CONFIGURATION['tables'][table_name][option]
    except KeyError:
        return None
