# notifier.py
from wazo_confd import bus, sysconfd


class WhitelistNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, whitelist):
        pass

    def edited(self, whitelist):
        pass

    def deleted(self, whitelist):
        pass


def build_whitelist_notifier():
    return WhitelistNotifier(bus, sysconfd)
