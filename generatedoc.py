from jinja2 import Environment, FileSystemLoader
import os
import json # Used for tojson filter in Jinja2

def generate_documentation(api_info, template_dir, output_dir):
    """Generates documentation from structured API info."""
    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Add a filter to convert dicts to formatted JSON
    env.filters['tojson'] = json.dumps

    # Render the main template
    main_template = env.get_template('main_template.html.j2')
    rendered_docs = main_template.render(api_info=api_info)

    # Write the output file
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(rendered_docs)
    
    print(f"Documentation generated and saved to {output_dir}/index.html")
