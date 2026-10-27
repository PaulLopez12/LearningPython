from fastapi import FastAPI
import link_bio.constants as const
from .TwitchAPI import TwitchApi
from .SupabaseAPI import SupabaseAPI

api_app = FastAPI()

TWITCH_API = TwitchApi()
SUPABASE_API = SupabaseAPI()


@api_app.get("/repo")
async def repo() -> str:
    return const.REPO_URL

@api_app.get("/live/{user}")
async def live(user : str) -> dict:
    return TWITCH_API.live(user)

async def featured() -> list:
    return SUPABASE_API.featured()