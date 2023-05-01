
import os, sys, time
from device_manager import *


class mRulePriorityEnum(Enum):
    """ task queue priority enum    """
    PRIOR_LOW    = 1
    PRIOR_MEDIUM = 2
    PRIOR_HIGH   = 3

class mRule(object):
    """_summary_
    achieve task class
    Args:
        indevice  : input device
        outdevice : output device
        operation : data operation
        priority  : task priority
    """
    def __init__(self, indevice: str, outdevice: str, priority: mRulePriorityEnum):
        """ init param and create task  """
        self._indevice  = indevice
        self._outdevice = outdevice
        self._priority  = priority

class mRuleTable(object):
    """_summary_
    achieve rule table
    Args:
        maxsize  : the max size of rule table
    """
    def __init__(self, maxsize=10):
        self._maxsize = maxsize

        # create rule task
        self._list = []

    def isEmpty(self):
        """ detect list isEmpty     """
        if self.size() == 0:
            return True
        else:
            return False

    def isFull(self):
        """ detect list isFull      """
        if self.size() == self._maxsize:
            return True
        else:
            return False

    def size(self):
        """ query list size         """
        return len(self._list)

    def add(self, rule: mRule):
        """ append a new rule       """
        if not self.isFull():
            self._list.append(rule)

    def close(self):
        del self._list



def load_rule_table_from_config_file(file_name):
    """ load routing table from config file    """
    rule_list = []
    with open(file_name, "r") as f:
        while True:
            rdata = f.readline().replace("\n","")
            if rdata:
                if not "#" in rdata:
                    param1, param2, param3 = rdata.replace(" ","").split(",")
                    rule_list.append(mRule(indevice=param1, outdevice=param2, priority=conv_from_str_to_enum(mRulePriorityEnum, param3)))
            else:
                break
    return rule_list

def test_for_task_queue():
    rule_table = mRuleTable()
    for rule in load_rule_table_from_config_file("../config/forwarding_rule.conf"):
        rule_table.add(rule)
        print(rule._indevice, rule._outdevice, rule._priority)

    print(rule_table._list[0]._indevice)
    print(rule_table._list[1]._indevice)

if __name__ == "__main__":
    test_for_task_queue()
