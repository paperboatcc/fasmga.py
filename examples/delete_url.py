import asyncio
import fasmga
import os

client = fasmga.Client(os.getenv("FGA_TOKEN"))

@client.on("ready")
async def main():
    url = client.urls[-1]
    print("Your shortened URL is:", url)
    print("It redirects to", url.uri)
    print(client.urls)
    await asyncio.sleep(
        10
    )  # wait for 10 seconds before deleting, we don't want to run things too fast
    await url.delete()
    print(f"Your URL {url} has been deleted.")
    await client.close()  # closes the client, if you want to keep the event loop running you can comment this line


client.start()
