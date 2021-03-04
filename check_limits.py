from bms_health import bms_health_check
from input_validator import bms_parameter_name_validation
from input_validator import bms_parameter_value_validation

if __name__ == '__main__':
    assert (bms_parameter_name_validation({'bms_temperature': 40, 'soc': 40, 'charging_rate': 0.8}) == 'UNKNOWN PARAMETER')
    assert (bms_parameter_name_validation({'temperature': 40, 'soc': 40, 'charging_rate': 0.6}) == 'OK')

    assert (bms_parameter_value_validation({'temperature': 'nan', 'soc': 40, 'charging_rate': 0.8}) == 'INVALID PARAMETER VALUE')
    assert (bms_parameter_value_validation({'temperature': 40, 'soc': '', 'charging_rate': 0.8}) == 'INVALID PARAMETER VALUE')
    assert (bms_parameter_value_validation({'temperature': 40, 'soc': 40 , 'charging_rate': 'unknown'}) == 'INVALID PARAMETER VALUE')
    assert (bms_parameter_name_validation({'temperature': 40, 'soc': 40, 'charging_rate': 0.6}) == 'OK')

    assert (len(bms_health_check({'temperature': 40, 'soc': 40, 'charging_rate': 0.6})) == 0)
    assert (len(bms_health_check({'temperature': 100, 'soc': 40, 'charging_rate': 0.8})) > 0)
    assert (len(bms_health_check({'temperature': -5, 'soc': 40, 'charging_rate': 0.8})) > 0)
