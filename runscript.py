if __name__ == "__main__":
    spec_file = 'path/to/your/openapi.yaml'
    template_dir = 'path/to/your/templates'
    output_dir = 'path/to/your/docs_output'
    
    # 1. Analyze the spec
    api_data = analyze_openapi_spec(spec_file)

    # 2. Generate the documentation
    generate_documentation(api_data, template_dir, output_dir)
