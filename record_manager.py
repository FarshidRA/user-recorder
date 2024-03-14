import pandas as pd

def add_record(name, sname, age):
    try:
        age = int(age)
    except ValueError:
        return 'Enter valid age'

    if 0 <= age <= 1:
        category = 'Nini'
    elif 1 < age <= 12:
        category = 'Kid'
    elif 12 < age < 18:
        category = 'Teenager'
    elif 18 <= age < 40:
        category = 'Adult'
    elif 40 <= age <= 65:
        category = 'Big'
    else:
        category = 'Old'

    new_record = [{'Name': name, 'Sure Name': sname, 'Age': age, 'Category': category}]
    new_df = pd.DataFrame(new_record)

    existing_df = pd.DataFrame()
    try:
        existing_df = pd.read_excel('user_records.xlsx')
    except FileNotFoundError:
        pass

    updated_df = pd.concat([existing_df, new_df], ignore_index=True)

    if 'Row Number' in updated_df.columns:
        updated_df = updated_df.drop('Row Number', axis=1)
    updated_df.insert(0, 'Row Number', updated_df.index + 1)

    updated_df.to_excel('user_records.xlsx', index=False)

    return f'Number {updated_df.index[-1] + 1} user added successfully!'
