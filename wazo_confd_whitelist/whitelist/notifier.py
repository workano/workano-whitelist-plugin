from wazo_bus.resources.whitelist.event import (
    WhitelistCreatedEvent,
    WhitelistDeletedEvent,
    WhitelistEditedEvent,
)

from wazo_confd import bus


class WhitelistNotifier:
    def __init__(self, bus):
        self.bus = bus

    def created(self, whitelist):
        event = WhitelistCreatedEvent(whitelist.id, whitelist.tenant_uuid)
        self.bus.queue_event(event)

    def edited(self, whitelist):
        event = WhitelistEditedEvent(whitelist.id, whitelist.tenant_uuid)
        self.bus.queue_event(event)

    def deleted(self, whitelist):
        event = WhitelistDeletedEvent(whitelist.id, whitelist.tenant_uuid)
        self.bus.queue_event(event)


def build_whitelist_notifier():
    return WhitelistNotifier(bus)
