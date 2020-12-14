import glob
import os
from avro_to_python_types import schema_to_typed_dict

current_directory = f"{os.getcwd()}/examples/sync_types"
schema_file_paths = glob.glob(f"{current_directory}/schemas/*.avsc")
types_directory = f"{current_directory}/types"


def schema_name_from_path(path):
    file_name = path.rsplit("/", 1)[-1]
    schema_name = file_name.rsplit(".")[0]
    return schema_name


def generate_types_from_schemas():
    for schema_file_path in schema_file_paths:
        with open(schema_file_path) as f:
            avro_schema = f.read()
        python_contents = schema_to_typed_dict(avro_schema)
        schema_name = schema_name_from_path(schema_file_path)
        type_file_name = f"{types_directory}/{schema_name}.py"
        print(type_file_name)
        with open(type_file_name, "w+") as f:
            f.write(python_contents)
