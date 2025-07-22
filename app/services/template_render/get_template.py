from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.template import Template

class TemplateRenderer:
    def __init__(self, session: AsyncSession, fallback_lang: str = "en"):
        self.session = session
        self.fallback_lang = fallback_lang

    
    async def get_template(self, name: str, lang: str = None) -> Template:
        for lang in [lang, self.fallback_lang]:
            stmt = select(Template).where(
                Template.name == name,
                Template.lang == lang 
            )
            result = await self.session.execute(stmt)
            template = result.scalar_one_or_none()
            if template:
                return template
        
        raise ValueError(f"Template '{name}' not found in '{lang}' or fallback '{self.fallback_lang}'")
    
    def render(self, template_str: str, context: dict) -> str:
        return template_str.format(**context)

    async def render_by_name(self, name: str, lang: str, context: dict) -> str:
        template = await self.get_template(name, lang)
        return self.render(template.body, context)
    