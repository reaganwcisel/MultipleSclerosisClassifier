def clean_data(input_file, output_file):
    lines = open(input_file, 'r').readlines()
    cleaned = []
    for line in lines:
        comma_index = line.find(',')
        cleaned.append(line[comma_index + 1:])
    open(output_file, 'w').writelines(cleaned)

def update_data(input_file, output_file):
    lines = open(input_file, 'r').readlines()
    cleaned = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) > 3:
            # Remove 3rd-to-last and 2nd-to-last items
            del parts[-3:-1]
        cleaned.append(','.join(parts) + '\n')
    open(output_file, 'w').writelines(cleaned)

def main():
    clean_data('conversion_predictors_of_clinically_isolated_syndrome_to_multiple_sclerosis.data', 'initial_cleaned.data')
    update_data('initial_cleaned.data', 'updated_removed.dataa')

if __name__ == '__main__':
    main()
