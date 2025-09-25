from jinja2 import Environment, FileSystemLoader
import os
import json # Used for tojson filter in Jinja2

def analyze_openapi_spec_json(file_path):
    """
    Parses an OpenAPI spec from a JSON file and returns a structured dictionary.
    """
    with open(file_path, 'r') as file:
        spec_data = json.load(file)

    # Dictionary to hold the extracted information
    api_info = {
        "info": spec_data.get('info', {}),
        "servers": spec_data.get('servers', []),
        "endpoints": []
    }

    # Iterate through paths to extract endpoint details
    paths = spec_data.get('paths', {})
    for path, path_data in paths.items():
        for method, method_data in path_data.items():
            endpoint = {
                "path": path,
                "method": method.upper(),
                "summary": method_data.get('summary', 'No summary provided.'),
                "description": method_data.get('description', ''),
                "requestBody": method_data.get('requestBody', {}),
                "responses": method_data.get('responses', {}),
                "parameters": method_data.get('parameters', [])
            }
            api_info["endpoints"].append(endpoint)
            
    # Add reusable components (schemas) for later use
    api_info['schemas'] = spec_data.get('components', {}).get('schemas', {})

    return api_info


def generate_documentation(api_info, template_dir, output_dir):
    """Generates documentation from structured API info."""
    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Create a custom filter that correctly uses the 'indent' argument
    # the 'value' argument is automatically passed by Jinja2
    # Add a filter to convert dicts to formatted JSON
    env.filters['tojson'] = lambda value, indent=None: json.dumps(value,indent=indent)

    # Render the main template
    main_template = env.get_template('main_template.html.j2')
    rendered_docs = main_template.render(api_info=api_info)

    # Write the output file
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(rendered_docs)
    
    print(f"Documentation generated and saved to {output_dir}/index.html")


if __name__ == "__main__":
    # Get absolut path of the directory where script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full paths to the template and output directories
    spec_file = os.path.join(script_dir,'apidoc.json')
    template_dir = os.path.join(script_dir,'templates') 
    output_dir = os.path.join(script_dir,'docs_output')
    
    # 1. Analyze the spec
    api_data = analyze_openapi_spec_json(spec_file)

    # 2. Generate the documentation
    generate_documentation(api_data, template_dir, output_dir)
