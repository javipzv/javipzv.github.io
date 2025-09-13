from bs4 import BeautifulSoup

def add_experience(company, role, period, description_en, description_es, logo_path, html_path="index.html"):
    # Cargar HTML
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Crear contenedor de experiencia
    new_div = soup.new_tag("div", **{"class": "experience-item"})

    # Logo
    img = soup.new_tag("img", src=logo_path, **{"class": "experience-logo"})
    new_div.append(img)

    # Contenedor de texto
    details_div = soup.new_tag("div", **{"class": "experience-details"})
    
    # Títulos (EN/ES)
    h5_en = soup.new_tag("h5", **{"class": "english"})
    h5_en.string = f"{role} - {company} ({period})"
    details_div.append(h5_en)

    h5_es = soup.new_tag("h5", **{"class": "spanish"})
    h5_es.string = f"{role} - {company} ({period})"
    details_div.append(h5_es)

    # Descripciones (EN/ES)
    p_en = soup.new_tag("p", **{"class": "english"})
    p_en.string = description_en
    details_div.append(p_en)

    p_es = soup.new_tag("p", **{"class": "spanish"})
    p_es.string = description_es
    details_div.append(p_es)

    # Añadir detalles al bloque
    new_div.append(details_div)

    # Insertar en la lista de experiencias
    container = soup.find("div", {"id": "experience-list"})
    container.append(new_div)

    # Guardar cambios
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))

    print(f"✅ Experiencia añadida: {company} - {role}")

# Ejemplo de uso
add_experience(
    company="Whitebox",
    role="Junior Data Scientist",
    period="Sept 2025 - Present",
    description_en="Participo activamente en proyectos de mayor escala, trabajando con modelos de lenguaje (LLMs) o apoyando el despliegue de soluciones en entornos de nube.",
    description_es="Take an active role in larger-scale projects, working with language models (LLMs) or supporting the deployment of solutions in cloud environments.",
    logo_path="static/whitebox.png"
)
