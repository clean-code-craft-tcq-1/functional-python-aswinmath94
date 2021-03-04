from bms_constants import bms_thresholds


def collect_anomalies(anomaly, bms_parameter, bms_parameter_value, bms_parameter_range):
    if bms_parameter_value < bms_parameter_range['min']:
        anomaly.append([bms_parameter, 'UNDER LIMIT'])
    elif bms_parameter_value > bms_parameter_range['max']:
        anomaly.append([bms_parameter, 'OVER LIMIT'])


def bms_health_check(status_report):
    anomalies = []
    for bms_parameter in status_report:
        collect_anomalies(anomalies, bms_parameter, status_report[bms_parameter], bms_thresholds[bms_parameter])
    bms_breach_param(anomalies)
    return anomalies

def bms_breach_param(anomalies):
    if len(anomalies) == 0:
        print('All Parameters are OK')
    else:
        for parameter in anomalies:
            unsafe_param_name = parameter[0]
            unsafe_param_status = parameter[1
            print('BMS Operating in Unsafe Condition:{} -> {}'.format(unsafe_param_name,unsafe_param_status))
