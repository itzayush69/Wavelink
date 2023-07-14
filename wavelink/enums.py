"""
MIT License

Copyright (c) 2019-Current PythonistaGuild, EvieePy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import enum

__all__ = ("NodeStatus", "TrackSource", "DiscordVoiceCloseType")


class NodeStatus(enum.Enum):
    """Enum representing the connection status of a Node.

    Attributes
    ----------
    DISCONNECTED
        0
    CONNECTING
        1
    CONNECTED
        2
    """

    DISCONNECTED = 0
    CONNECTING = 1
    CONNECTED = 2


class TrackSource(enum.Enum):
    """Enum representing a :class:`Playable` source.

    Attributes
    ----------
    YouTube
        0
    YouTubeMusic
        1
    SoundCloud
        2
    """

    YouTube = 0
    YouTubeMusic = 1
    SoundCloud = 2


class DiscordVoiceCloseType(enum.Enum):
    """Enum representing the various Discord Voice Websocket Close Codes.

    Attributes
    ----------
    CLOSE_NORMAL
        1000
    UNKNOWN_OPCODE
        4001
    FAILED_DECODE_PAYLOAD
        4002
    NOT_AUTHENTICATED
        4003
    AUTHENTICATION_FAILED
        4004
    ALREADY_AUTHENTICATED
        4005
    SESSION_INVALID
        4006
    SESSION_TIMEOUT
        4009
    SERVER_NOT_FOUND
        4011
    UNKNOWN_PROTOCOL
        4012
    DISCONNECTED
        4014
    VOICE_SERVER_CRASHED
        4015
    UNKNOWN_ENCRYPTION_MODE
        4016
    """

    CLOSE_NORMAL = 1000  # Not Discord but standard websocket
    UNKNOWN_OPCODE = 4001
    FAILED_DECODE_PAYLOAD = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    SESSION_INVALID = 4006
    SESSION_TIMEOUT = 4009
    SERVER_NOT_FOUND = 4011
    UNKNOWN_PROTOCOL = 4012
    DISCONNECTED = 4014
    VOICE_SERVER_CRASHED = 4015
    UNKNOWN_ENCRYPTION_MODE = 4016
