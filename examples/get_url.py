import asyncio
import fasmga
import os

client = fasmga.Client(os.getenv("FGA_TOKEN"))


@client.on("ready")
async def main():
    url = client.get_url("your-url-id")
    print("Your shortened URL is:", url)
    print("It redirects to", url.uri)
    await asyncio.sleep(
        10
    )  # wait for 10 seconds before editing, we don't want to run things too fast
    await url.edit(
        url="https://example.com", password="mysupersecurepassword"
    )  # edit the redirect URL and add a password
    print(f"Your URL {url} has been edited.")
    print("Now it redirects to", url.uri)
    print("Remember: Passwords aren't stored in URL instances.")
    await client.close()  # closes the client, if you want to keep the event loop running you can comment this line


client.start()
