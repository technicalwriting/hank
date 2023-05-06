import jsonlines
from glob import glob

def main():
    print('I am the bat.')
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
