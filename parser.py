import json

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
