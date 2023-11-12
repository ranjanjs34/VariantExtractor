import os
from tqdm import tqdm

# Ask the user to input the path to the directory with CSV files
csv_dir = input("Enter the path to the directory with Annotated CSV files: ")

# Ask the user to input the path to the file with the list of words
word_file = input("Enter the gene or variant list file name: ")

# Read the list of words from the file
with open(word_file, 'r') as f:
    words = set(line.strip() for line in f)

# Loop over all CSV files in the directory
for filename in tqdm(os.listdir(csv_dir)):
    if filename.endswith('.txt'):
        with open(os.path.join(csv_dir, filename), 'r') as csv_in:
            # Open a new output file with the same name as the input file, but with a `_filter.csv` extension
            csv_out = open(os.path.join(csv_dir, filename.replace('.txt', '_filter.txt')), 'w')

            # Loop over the input file and write rows where the word is in the 7th column
            for i, line in enumerate(csv_in):
                if i == 0:
                    # Write the header line to the output file
                    csv_out.write(line.strip() + ',filename\n')
                else:
                    parts = line.strip().split('\t')
                    if len(parts) > 6 and parts[6] in words:
                        # Write the row to the output file with the filename
                        csv_out.write(line.strip() + f',{filename}\n')

            # Close the output file
            csv_out.close()
