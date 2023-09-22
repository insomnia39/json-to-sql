import json

def json_to_sql_insert(json_file, table_name, category, status, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    columns = []
    values = []

    for item in data:
        for key, value in item.items():
            if key not in columns:
                columns.append(key)
            values.append(value)

    sql_query = f"INSERT INTO {table_name} ({', '.join(columns)}, category, status) VALUES "
    t = 0
    value_strings = []
    for i in range(0, len(values), len(columns)):
        t += 1
        value_strings.append("(" + ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in values[i:i+len(columns)]]) + 
        f", `{category}`, '{status}')")

    sql_query += ', '.join(value_strings) + ";"
    
    with open(output_file, 'w') as sql_file:
        sql_file.write(sql_query)

if __name__ == "__main__":
    json_file = "proceed-course-sms1.json"
    table_name = "CMSProceedCourse"
    category = "COOR-V2-SMS1"
    status = "not started"
    output_file = "output.sql"

    json_to_sql_insert(json_file, table_name, category, status, output_file)
    print(f"SQL query has been saved to {output_file}")