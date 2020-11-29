import re


def read_lines(file_path):
    lines = []
    with open(file_path, 'r') as inf:
        for line in inf:
            lines.append(line.rstrip('\n'))
    return lines


def write_lines(lines, file_path):
    with open(file_path, 'w') as outf:
        for line in lines:
            outf.write(line + '\n')


dicts = ['korean_dictionary1.json', 'korean_dictionary2.json']
nouns = set()
for d in dicts:
    d_lines = read_lines(d)
    for d_line in d_lines:
        r_word = r"(?<={)\'.+?\': '(.+?)',"
        r_raw = r"'raw': (.+)}"
        word = re.search(r_word, d_line)[1]
        raw = re.search(r_raw, d_line)[1]
        if '［명사］' in raw:
            nouns.add(word)

write_lines(sorted(list(nouns)), 'all_nouns')
print('done')
