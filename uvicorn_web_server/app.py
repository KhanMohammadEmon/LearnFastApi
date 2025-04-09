async def app(scope, receive, send):
    assert scope['type'] == 'http'

    try:
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [(
                b"content-type", b"text-plain"
            )]
        })

        await send({
            "type": "http.response.body",
            "body": b"<h1>This is Emon. How are you</h1>"
        })

    except:
        print("Fail to start server!")
