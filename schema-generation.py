import pandas as pd
import json

def generate_json_schema_from_csv(csv_file, output_file):
    df = pd.read_csv(csv_file)

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {},
        "required": []
    }

    data_type_mapping = {
        "date": {"type": "string", "format": "date"},
        "int": {"type": "integer"},
        "float": {"type": "number"},
        "string": {"type": "string"}
    }

    for _, row in df.iterrows():
        var_name = row['var_name']
        description = row['description']
        data_type = row['data_type']

        if data_type in data_type_mapping:
            schema_properties = data_type_mapping[data_type]
            schema_properties["description"] = description
            schema['properties'][var_name] = schema_properties
            schema['required'].append(var_name)
        else:
            raise ValueError(f"Unsupported data_type: {data_type}")

    with open(output_file, 'w') as f:
        json.dump(schema, f, indent=2)


csv_file = "C:/Users/cbollu/Downloads/Data Dict - Variables - PD V1 - Model Variables.csv"
output_file = "C:/Users/cbollu/Downloads/test_blocks/test_blocks/sequence-1/pd_v1_processing/request_schema.json"
generate_json_schema_from_csv(csv_file, output_file)

