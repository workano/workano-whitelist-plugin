from wazo_bus.resources.mohsen.event import (
    WhitelistCreatedEvent,
    WhitelistDeletedEvent,
    WhitelistEditedEvent,
)

from wazo_confd import bus


class WhitelistNotifier:
    def __init__(self, bus):
        self.bus = bus

    def created(self, mohsen):
        event = WhitelistCreatedEvent(mohsen.id, mohsen.tenant_uuid)
        self.bus.queue_event(event)

    def edited(self, mohsen):
        event = WhitelistEditedEvent(mohsen.id, mohsen.tenant_uuid)
        self.bus.queue_event(event)

    def deleted(self, mohsen):
        event = WhitelistDeletedEvent(mohsen.id, mohsen.tenant_uuid)
        self.bus.queue_event(event)


def build_whitelist_notifier():
    return WhitelistNotifier(bus)
