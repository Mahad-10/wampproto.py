import cbor2

from wamp.messages import Message
from wamp.serializers import Serializer
from wamp.serializers.serializer import to_message


class CBORSerializer(Serializer):
    def serialize(self, message: Message) -> bytes:
        return cbor2.dumps(message.marshal())

    def deserialize(self, data: bytes) -> Message:
        wamp_message = cbor2.loads(data)
        return to_message(wamp_message)
