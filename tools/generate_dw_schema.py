import os

tables = [
    "customers",
    "products",
    "orders",
    "payments",
    "shipments",
    "inventory",
    "stores",
    "suppliers",
    "reviews",
    "promotions",
]

template = """
CREATE TABLE {table} (
    id INT,
    name VARCHAR(255),
    created_at DATETIME
);
"""

output_dir = "sql/generated"

os.makedirs(output_dir, exist_ok=True)

for table in tables:
    file_path = f"{output_dir}/{table}.sql"

    with open(file_path, "w") as f:
        f.write(template.format(table=table))

print("Schema files generated successfully")
