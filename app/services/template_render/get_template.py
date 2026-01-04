from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.template import Template


class TemplateRenderer:
    def __init__(self, session: AsyncSession, fallback_lang: str = "en"):
        self.session = session
        self.fallback_lang = fallback_lang

    async def get_template(self, name: str, lang: str | None = None) -> Template:
        languages: list[str] = []

        if lang:
            languages.append(lang)

        if self.fallback_lang not in languages:
            languages.append(self.fallback_lang)

        for l in languages:
            stmt = select(Template).where(
                Template.name == name,
                Template.language == l
            )
            result = await self.session.execute(stmt)
            template = result.scalars().first()
            if template:
                return template

        raise ValueError(
            f"Template '{name}' not found for languages {languages}"
        )

    def render(self, template_str: str, context: dict) -> str:
        return template_str.format(**context)

    async def render_by_name(self, name: str, lang: str | None, context: dict) -> dict:
        template = await self.get_template(name, lang)
        return {
            "title": self.render(template.title_tpl or "", context),
            "body": self.render(template.body, context),
        }
