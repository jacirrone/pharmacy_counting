import argparse
import os
import csv
import utils

def main():
    parser = argparse.ArgumentParser(description='pharmacy_counting')
    parser.add_argument('input', metavar='in', help='Input')
    parser.add_argument('output', metavar='out',
                        help='Output')
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as input_file:
            reader = csv.reader(input_file, delimiter=',')
            next(reader)
            drugs = {}
            for i, element in enumerate(reader):
                utils.add_element(element, drugs)
    except IOError:
        print 'Cant find input file'
        return

    drugs_output = zip(drugs.keys(), drugs.values())
    drugs_output = list(drugs_output)
    drugs_output = sorted(drugs_output, key=lambda row: (-row[1]['cost'], row[0]))

    with open(args.output, 'w') as output_file: #, newline='\n'
        column_names = ['drug_name', 'num_prescriber', 'total_cost']
        writer = csv.DictWriter(output_file, fieldnames=column_names)
        writer.writeheader()
        for element in drugs_output:
            writer.writerow(
                {'drug_name': element[0],
                 'num_prescriber': len(element[1]) - 1,
                 'total_cost': element[1]['cost']}
            )
        output_file.truncate(output_file.tell() - len(os.linesep))


if __name__ == '__main__':
    main()