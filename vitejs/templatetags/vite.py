from django import template
from django.utils.safestring import mark_safe
from urllib.parse import urljoin
from django.conf import settings

register = template.Library()


@register.simple_tag
@mark_safe
def vite_module(path: str) -> str:
    src = urljoin(settings.VITE_URL, path if path is not None else "")
    return f'<script type="module" src="{src}"></script>'


@register.simple_tag
@mark_safe
def vite_client() -> str:
    src = urljoin(settings.VITE_URL, '/@vite/client')
    return f'<script type="module" src="{src}"></script>'


@register.simple_tag
@mark_safe
def vite_entry() -> str:
    src = urljoin(settings.VITE_URL, settings.VITE_ENTRY)
    return f'<script type="module" src="{src}"></script>'
