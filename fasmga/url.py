class Url:
    def __init__(self,
        client,
        gash: str, redirect: str,
        nsfw: bool = False,
        clicks: int = 0,
    *args, **kwargs):
        from .client import Client

        self.client: Client = client
        self.gash = gash.strip("/")
        self.uri = redirect
        self.is_nsfw = nsfw
        self.clicks = clicks

    def __str__(self,
        mode: str = "short"
    ):
        root_url = "fga.sh" if mode is short else "fasmga.org"
        return f"https://{root_url}/{self.gash}"

    def __repr__(self):
        return f"<url gash='{self.gash}' redirect='{self.redirect}' nsfw={self.is_nsfw}>"

    async def edit(self,
        redirect: str = None,
        password: str = None,
        nsfw: bool = False
    *args, **kwargs):
        await self.client.edit(
            self.gash,
            url = redirect,
            password = password, nsfw = nsfw)
        self.uri = redirect
        self.is_nsfw = nsfw
    
    async def delete(self):
        self.client._pending_deletion_urls.append(self)
        await self.client.delete(self.gash)
        self.client.urls.remove(self)
        self.client._pending_deletion_urls.remove(self)
