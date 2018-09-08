# A program for string matching OMIM phenotypes to MeSH disease terms or other string matching.

fw = open('Matching_strings_test.txt','w') # Write to 'Matching_strings_test.txt' file.
fw2 = open('OMIM_phenotypes which_dont_match_up_test.txt','w') # 'Write to 'OMIM_phenotypes which_dont_match_up.txt' file.
file1 = set(line.strip() for line in open('final_required_phenotypes_test.txt')) # file1 is the txt file in brakets.
file2 = set(line.strip() for line in open('final_required_phenotypes_with_some_not_in_original_test.txt')) # Replace file2 with MeSH file.
for line in file1 & file2: # Looking at lines in both files at the same time.
    if line:
        fw.write(line + '\r\n') # If lines match then writes to fw.

file_1 = set() # Converts file_1 to a set.
file_2 = set() # Converts file_2 to a set.

with open('final_required_phenotypes_test.txt') as f: # Opens this file.
    for line in f: # Reads each separate line in txt file.
        file_1.add(line.strip()) # Strips out the white spaces in file_1.

with open('final_required_phenotypes_with_some_not_in_original_test.txt') as f: # Opens this file.
    for line in f: # Reads each separate line in txt file.
        file_2.add(line.strip()) # Strips out the white spaces in file_2.

fw2.write(str("\r\n".join(file_1-file_2))) # Compares file_1 and file_2 and writes to fw2 strings which dont match.
