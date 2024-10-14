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
- Compute Rouge Score

## Text Split
First, please make sure to replace `text_path` with the path to the text you want to test, and `output_dir` with the location where you want the samples to be saved. Additionally, `num_samples` controls the number of samples you want to extract, and `sample_length` controls the length of each sample. You can adjust these parameters according to your needs.

## Test Infringement Risks
In this section, you will need to modify the API interface within the `get_llm_completion` function based on the LLMs you wish to test. This project uses Llama2 as an example, so please adjust it according to your specific requirements. (Note: Before use, please store the API KEY in your local environment.)
