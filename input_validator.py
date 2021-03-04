bms_parameters =['temperature','soc','charging_rate']

def bms_parameter_name_validation(status_report):
    for param_name in status_report.keys():
        if param_name not in bms_parameters:
            return 'UNKNOWN PARAMETER'
    return 'OK'

def bms_parameter_value_validation(status_report):
    for param_value in status_report.values():
        param_value_type = type(param_value)
        if param_value_type not in [int,float]:
            return 'INVALID PARAMETER VALUE'
    return 'OK'

