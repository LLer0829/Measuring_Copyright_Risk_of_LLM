# Measuring Copyright Risk of LLMs
This repository includes the original implementation of the paper [Measuring Copyright Risks of Large Language Model via Partial Information Probing](https://arxiv.org/abs/2409.13831) by Weijie Zhao, Huajie Shao, Zhaozhuo Xu, Suzhen Duan, Denghui Zhang.

## Installation
Install dependent Python libraries by running the command below.
```
pip install -r requirements.txt
```

## Quick Start
Measuring Copyright Risks of Large Language Model via Partial Information Probing is mainly carried out through the following three steps:
- Split Text
- LLMs Completion
- Calculate Rouge-Score

### Splite Text
```
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
text_path = 'Title'
output_dir = 'File'
split_text_into_samples(text_path, output_dir)
```
First, please replace text_path with the path to the text you want to test, and output_dir with the location where you want the samples to be saved. Next, num_samples controls the number of samples to extract, and sample_length controls the length of each sample. Adjust these parameters based on your needs.

### LLMs Completion

### Calculate Rouge-Score
