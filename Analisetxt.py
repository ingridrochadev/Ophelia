import re

def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        issuing_post_name, control_number = re.findall(r'(\S.+) (\d+)', lines[1])[0]
        surname = lines[3].strip()

        if len(lines[6].split()) >= 3:
            name, visa_type, visa_class = lines[6].split()[:3]
        else:
            name, visa_type, visa_class = '', '', ''

        passport_number, sex, dob, nationality = lines[8].split()
        entry, issuance_date, expiration_date = lines[11].split()
        annotations = [line.strip() for line in lines[15:18]]

        data = {
            "issuing_post_name": issuing_post_name,
            "control_number": int(control_number),
            "surname": surname,
            "name": name,
            "visa_type": visa_type,
            "visa_class": int(visa_class) if visa_class.isdigit() else None,
            "passport_number": int(passport_number) if passport_number.isdigit() else None,
            "sex": sex,
            "dob": dob,
            "nationality": nationality,
            "entry": entry,
            "issuance_date": issuance_date,
            "expiration_date": expiration_date,
            "annotations": annotations
        }
        return data

file_path = "visto_texto_extraido1.txt"  
parsed_data = parse_file(file_path)
print(parsed_data)



