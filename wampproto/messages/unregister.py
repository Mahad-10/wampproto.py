from __future__ import annotations

from typing import Any

from wampproto.messages.message import Message
from wampproto.messages import util
from wampproto.messages.validation_spec import ValidationSpec


class UnRegister(Message):
    TEXT = "UNREGISTER"
    TYPE = 66

    VALIDATION_SPEC = ValidationSpec(
        min_length=3,
        max_length=3,
        message=TEXT,
        spec={
            1: util.validate_request_id,
            2: util.validate_registration_id,
        },
    )

    def __init__(self, request_id: int, registration_id: int):
        super().__init__()
        self.request_id = request_id
        self.registration_id = registration_id

    @classmethod
    def parse(cls, msg: list[Any]) -> UnRegister:
        f = util.validate_message(msg, cls.TYPE, cls.TEXT, cls.VALIDATION_SPEC)
        return UnRegister(f.request_id, f.registration_id)

    def marshal(self) -> list[Any]:
        return [self.TYPE, self.request_id, self.registration_id]
