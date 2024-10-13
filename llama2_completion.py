import os
import csv
import replicate
from rouge_score import rouge_scorer


def read_sample(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_llm_completion(prompt):
    input = {
        "prompt": prompt,
        "temperature": 0,
        "max_tokens": 300,
    }

    completion = ""
    for event in replicate.stream(
            "meta/llama-2-70b",
            input=input
    ):
        completion += event.data
    return completion.replace('\n', ' ').strip()


def calculate_rouge(reference, hypothesis):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    return scores['rougeL'].precision


def main_evaluate(samples_dir, output_csv):
    sample_files = [f for f in os.listdir(samples_dir) if f.endswith('.txt')]

    results = []

    for sample_file in sample_files:
        sample_path = os.path.join(samples_dir, sample_file)
        sample = read_sample(sample_path)

        words_in_sample = sample.split()
        prompt = " ".join(words_in_sample[:20])
        reference_continuation = " ".join(words_in_sample[20:])

        completion = get_llm_completion(prompt)

        rouge_l_precision = calculate_rouge(reference_continuation, completion)
        results.append({
            'LLMs': 'llama2',
            'Parameter scale': '70b',
            'Title': "HP3",
            'Prompt': prompt,
            'Completion': completion,
            'ROUGE-L': rouge_l_precision,
            'Temperature': '0',
            'max_tokens': '300'
        })
        print(f"{sample_file} ROUGE-L Recall: {rouge_l_precision}")

    with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['LLMs', 'Parameter scale', 'Title', 'Prompt', 'Completion', 'ROUGE-L', 'Temperature', 'max_tokens']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for result in results:
            writer.writerow(result)


if __name__ == "__main__":
    samples_dir = "HP3/sample_200"
    output_csv = "Add Data.csv"
    main_evaluate(samples_dir, output_csv)

