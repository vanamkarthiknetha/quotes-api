import asyncio

from app.integrations import slack
from app.services import analytics_service


async def main() -> None:
    lines = [f"{key}: {sum(paths.values())}" for key, paths in analytics_service._usage.items()]
    await slack.notify("Daily API usage\n" + ("\n".join(lines) or "no traffic"))


if __name__ == "__main__":
    asyncio.run(main())
