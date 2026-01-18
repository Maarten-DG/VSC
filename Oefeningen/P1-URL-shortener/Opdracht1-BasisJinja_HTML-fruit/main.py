# 1. Importeer de benodigde klasse uit de Jinja2 bibliotheek
from jinja2 import Template

# 2. De data: Een eenvoudige Python-lijst die we in de HTML willen tonen
vruchten = ["appel", "peer", "banaan"]

# 3. De Template: Een 'multi-line string' met HTML en Jinja-syntax
# {% ... %} wordt gebruikt voor logica (zoals loops of if-statements)
# {{ ... }} wordt gebruikt om de waarde van een variabele te printen
html_template = """
<ul>
{% for vrucht in fruit_lijst %}
    <li>{{ vrucht }}</li>
{% endfor %}
</ul>
"""

# 4. Maak een Template-object aan op basis van onze string
tm = Template(html_template)

# 5. Het 'renderen': Hier wordt de Python-lijst (vruchten) gekoppeld 
# aan de naam in de template (fruit_lijst) en samengevoegd tot HTML
output = tm.render(fruit_lijst=vruchten)

# 6. Print het resultaat naar de terminal (of stuur het naar een bestand)
print(output)