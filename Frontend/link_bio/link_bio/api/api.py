from fastapi import FastAPI
import link_bio.constants as const
from .TwitchAPI import TwitchApi

api_app = FastAPI()

TWITCH_API = TwitchApi()


@api_app.get("/repo")
async def repo() -> str:
    return const.REPO_URL

@api_app.get("/live/{user}")
async def live(user : str) -> bool:
    return TWITCH_API.live(user)