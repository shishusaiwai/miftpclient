import re
import subprocess


class InterfaceText(object):

    def __init__(self):
        self.lines = []
        self.is_complete = False

    def add_line(self, line):
        self.lines.append(line)

    def is_net_available(self):
        for line in self.lines:
            if "UP BROADCAST RUNNING MULTICAST" in line:
                return True
        return False

    def set_complete(self):
        self.is_complete = True

    def get_lan_ip(self):
        text = "".join(self.lines)
        p = re.compile("192.168.[0-9]{1,3}.[0-9]{1,3}")
        m = p.search(text)
        return m.group(0)


def parse_ip():
    ifconfig_text = subprocess.check_output("ifconfig")
    lines = ifconfig_text.split("\n")
    interfases = []
    current_if = InterfaceText()
    for line in lines:
        text = line.strip()
        if not text:
            current_if.set_complete()
            interfases.append(current_if)
            current_if = InterfaceText()
        else:
            current_if.add_line(text)
    current_if.set_complete()
    interfases.append(current_if)

    for if_ in interfases:
        if if_.is_net_available():
            return if_.get_lan_ip()
    return None
