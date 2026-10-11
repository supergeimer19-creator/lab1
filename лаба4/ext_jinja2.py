from jinja2 import Template

def test_jinja2():
    template = Template("Привіт, {{ name }}!")
    result = template.render(name="Студент")
    print(f"jinja2: Шаблон відрендерено -> {result}")