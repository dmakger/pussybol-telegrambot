import asyncio
import g4f

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.Aivvm,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.CodeLinkAva,
    g4f.Provider.DeepAi,
    g4f.Provider.GptGo,
    g4f.Provider.Wewordle,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
]


async def run_provider(provider: g4f.Provider.AsyncProvider):
    try:
        response = await provider.create_async(
            model=g4f.models.default.name,
            messages=[{"role": "user", "content": "Hello"}],
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())