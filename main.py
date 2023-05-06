from jsonlines import open as jsonl_open
from glob import glob
from json import load

def main():
    data_files = glob('data/*.json')
    jsonl = []
    for data_file in data_files:
        with open(data_file, 'r') as f:
            data = load(f)
        for pair in data:
            prompt = pair[0]
            completion = pair[1]
            jsonl.append({'prompt': prompt, 'completion': completion})
        with jsonl_open('training.jsonl', 'w') as writer:
            writer.write_all(jsonl)
    # output = []
    # for item in data:
    #     original = item['original']
    #     edited = item['edited']
    #     prompt = 'FIXME: {}@STOP!!'.format(original)
    #     completion = ' {}'.format(edited)
    #     output.append({'prompt': prompt, 'completion': completion})
    #     with jsonlines.open('training.jsonl', 'w') as writer:
    #         writer.write_all(output)

if __name__ == '__main__':
    main()
