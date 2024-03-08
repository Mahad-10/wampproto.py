from wamp.messages import Message, Hello, Welcome, Abort, Challenge, Authenticate, Goodbye


class Serializer:
    def serialize(self, message: Message) -> bytes:
        raise NotImplementedError()

    def deserialize(self, message: Message) -> Message:
        raise NotImplementedError()


def to_message(message: list) -> Message:
    if not isinstance(message, list):
        raise TypeError(f"invalid type '{type(message)}', expected a list")

    message_type = message[0]
    if not isinstance(message_type, int):
        raise TypeError(f"invalid message type '{type(message[0])}', expected an integer")

    match message_type:
        case Hello.MESSAGE_TYPE:
            return Hello.parse(message)
        case Welcome.MESSAGE_TYPE:
            return Welcome.parse(message)
        case Abort.MESSAGE_TYPE:
            return Abort.parse(message)
        case Challenge.MESSAGE_TYPE:
            return Challenge.parse(message)
        case Authenticate.MESSAGE_TYPE:
            return Authenticate.parse(message)
        case Goodbye.MESSAGE_TYPE:
            return Goodbye.parse(message)
        case _:
            raise ValueError("unknown message type")
