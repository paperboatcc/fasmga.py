import asyncio
import fasmga
import os

client = fasmga.Client(os.getenv("FGA_TOKEN"))


@client.on("ready")
async def main():
    url = await client.shorten("http://example.com", "your-url-id")
    # change "your-url-id" with the url ID you want,
    # or remove it if you want it to generate a random one.
    print("Your shortened URL is:", url)
    print("It will redirect to", url.uri)
    await asyncio.sleep(10)  # wait for 10 seconds if you want to try the shortened site
    await url.edit(
        url="https://google.com", password="mysupersecurepassword"
    )  # edit the redirect URL and add a password
    print(f"Your URL {url} has been edited.")
    print("Now it redirects to", url.uri)
    print("Remember: Passwords aren't stored in URL instances.")
    await client.close()  # closes the client, if you want to keep the event loop running you can comment this line


client.start()
