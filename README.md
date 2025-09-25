# API Documentation Generator Agent 🤖

A Python-based agent that automates the generation of a static HTML API documentation site from an **OpenAPI Specification (OAS)** file. This tool allows you to maintain your API documentation as code, ensuring it is always up-to-date with your API's design.

-----

## Features ✨

  * **Automated Generation:** Reads an OpenAPI JSON file and generates a complete HTML documentation site.
  * **Dynamic Templating:** Uses Jinja2 templates to separate the presentation layer from the data, making it easy to customize the look and feel.
  * **Dynamic Navigation:** Automatically generates a responsive, navigable sidebar with links to each API endpoint.
  * **Static Assets Management:** Copies CSS and other static files to the output directory, ensuring your documentation is ready to be hosted.
  * **Clean Code:** Designed with separate modules for parsing (`Analyzer`) and rendering (`Generator`), following best practices for maintainable code.

-----

## Getting Started 🚀

Follow these steps to set up and run the documentation generator.

### Prerequisites

  * **Python 3.8+**
  * **pip** (Python package installer)

### Installation

Install the required Python libraries using pip:

```bash
pip install jinja2 python-slugify PyYAML
```

### Project Structure

Organize your project files in the following structure. This is essential for the script to find the correct files.

```
documentation_agent/
├── main.py                # The main script
├── apidoc.json            # Your OpenAPI spec file
├── templates/
│   ├── main_template.html.j2  # The main HTML template
│   ├── endpoint_template.html.j2# The template for each endpoint section
│   └── styles.css             # The stylesheet for the documentation
└── docs/                    # Output directory for generated docs
```

### Configuration

Open **`main.py`** and ensure the file paths match your project structure.

```python
# main.py

# ... (rest of the code)

if __name__ == "__main__":
    # Get the absolute path of the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full paths to the input and output directories
    spec_file = os.path.join(script_dir, 'apidoc.json')
    template_dir = os.path.join(script_dir, 'templates') 
    output_dir = os.path.join(script_dir, 'docs')
    
    # ... (rest of the code)
```

-----

## Usage 💻

1.  Place your **OpenAPI JSON file** inside the project root (e.g., `apidoc.json`).
2.  Ensure your Jinja2 templates and CSS file are in the `templates/` directory.
3.  Run the main script from your terminal:

<!-- end list -->

```bash
python main.py
```

After a few moments, a new `index.html` file and the `styles.css` file will be created inside the `docs/` directory. You can open `index.html` in your browser to view the generated documentation.

-----

## Customizing Templates 🎨

You can easily customize the look and feel of your documentation by editing the files in the `templates/` directory:

  * **`main_template.html.j2`**: Change the overall layout, add sections, or adjust the sidebar structure.
  * **`endpoint_template.html.j2`**: Modify how each individual API endpoint is displayed.
  * **`styles.css`**: Update colors, fonts, and spacing to match your brand.

-----

## License 📄

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.
