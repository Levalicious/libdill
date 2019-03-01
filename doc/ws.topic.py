
ws_flags = """
            The socket can be either text- (**WS_TEXT** flag) or binary-
            (**WS_BINARY** flag) based. Binary is the default. When sending
            messages via **msend** or **msendl** these will be typed based on
            the socket type. When receiving messages via **mrecv** or **mrecvl**
            encountering a message that doesn't match the socket type results in
            **EPROTO** error.

            If you want to combine text and binary messages you can do so by
            using functions such as **ws_send** and **ws_recv**.

            **WS_NOHTTP** flag can be combined with socket type flags. If set,
            the protocol will skip the initial HTTP handshake. In this case
            **resource** and **host** arguments won't be used and can be set
            to **NULL**.

            Skipping HTTP handshake is useful when you want to do the handshake
            on your own. For example, if you want to implement custom WebSocket
            extensions or if you want to write a multi-protocol application
            where initial HTTP handshake can be followed by different kinds
            of protocols (e.g. HTML and WebSocket).
"""

ws_topic = {
    "name": "ws",
    "title": "WebSocket protocol",
    "protocol": "message",
    "info": """
        WebSocket is a message-based protocol defined in RFC 6455. It can be
        used as a bidirectional communication channel for communication with
        a web server.
    """,
    "example": """
        struct ipaddr addr;
        ipaddr_remote(&addr, "www.example.org", 80, 0, -1);
        int s = tcp_connect(&addr, -1);
        s = ws_attach_client(s, "/", "www.example.org", WS_TEXT, -1);
        ws_send(s, WS_TEXT, "Hello, world!", 13, -1);
        int flags;
        char buf[256];
        ssize_t sz = ws_recv(s, &flags, buf, sizeof(buf), -1);
        assert(flags & WS_TEXT);
        s = ws_detach(s, -1);
        tcp_close(s, -1);
    """,
    "consts": {"WS_KEY_SIZE": "32"},
    "opaque": {"ws_storage" : 176},
    "opts": {
        "ws_": [
            {
                "name": "mem",
                "type": "struct ws_storage*",
                "dill": True,
                "default": "NULL",
                "info": "Memory to store the object in. If NULL, the memory will be allocated automatically.",
            },
            {
                "name": "http",
                "type": "unsigned int",
                "suffix": ":1",
                "default": "1",
                "info": "If true, the socket will perform initial HTTP negotiation. If false, it does not and the user is free to do it themselves.",
            },
            {
                "name": "text",
                "type": "unsigned int",
                "suffix": ":1",
                "default": "1",
                "info": "If true, messages will be of type TEXT by default. Otherwise, they will be of type BINARY. See RFC 6455, section 5.6.",
            },
        ],
    },
    "experimental": True,
}

new_topic(ws_topic)

