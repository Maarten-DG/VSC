from jinja2 import Template

producten_prijzen = {
    "T-shirt": 19.99,
    "Python Gids": 25.50,
    "Gaming Muis": 49.95,
    "Laptop Tas": 35.00
}

# 3. De Template: Een 'multi-line string' met HTML en Jinja-syntax
# {% ... %} wordt gebruikt voor logica (zoals loops of if-statements)
# {{ ... }} wordt gebruikt om de waarde van een variabele te printen
html_template = """
<table border="1">
    <thead>
        <tr>
            <th>Product</th>
            <th>Prijs</th>
        </tr>
    </thead>
    <tbody>
        {% for product, prijs in data.items() %}
        <tr>
            <td>{{ product }}</td>
            <td>€ {{ prijs }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
"""

# 4. Maak een Template-object aan op basis van onze string
tm = Template(html_template)

output = tm.render(data=producten_prijzen)

# 6. Print het resultaat naar de terminal (of stuur het naar een bestand)
print(output)