

def count_words(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

file_path = 'P1_data.txt'
assert count_words(file_path)['success'] == 3

file_path = 'P1_data.txt'
count_words(file_path)['man']
