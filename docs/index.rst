Welcome
=========

Welcome to the fasmga.py documentation!

fasmga.py is a Fasm.ga API wrapper written in Python using asyncio.

`Fasm.ga`_ is a free and open-source URL shortener.

Quickstart
----------

There isn't yet a public way to get an API token.
You may ask one in Fasm.ga's `Discord server`_.

.. code-block:: python

    import fasmga

    client = fasmga.Client("your-api-token")


    @client.on("ready")
    async def main():
        url = await client.shorten("http://example.com")
        print("Your shortened URL is:", url)
        print("It will redirect to", url.uri)
        await client.close()

    client.start()


.. _Fasm.ga: https://fasmga.org
.. _Discord server: https://discord.gg/MgQhdSZSsp
