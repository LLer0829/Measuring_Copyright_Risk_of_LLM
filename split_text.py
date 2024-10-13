import os


def split_novel_into_samples(novel_path, output_dir, num_samples=20, sample_length=200):
    # Read the content of the novel
    with open(novel_path, 'r', encoding='utf-8') as file:
        novel_content = file.read()

    words = novel_content.split()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract and save the samples
    for i in range(num_samples):
        sample_start = i * sample_length
        sample_end = sample_start + sample_length
        sample_words = words[sample_start:sample_end]
        sample_content = ' '.join(sample_words)

        sample_filename = os.path.join(output_dir, f'sample_{i + 1}.txt')
        with open(sample_filename, 'w', encoding='utf-8') as sample_file:
            sample_file.write(sample_content)


# Example usage
novel_path = 'Pride and Prejudice.txt'
output_dir = 'Pride and Prejudice/sample'
split_novel_into_samples(novel_path, output_dir)

