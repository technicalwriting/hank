python3 -m venv venv
source venv/bin/activate
python3 -m pip install jsonlines openai
read -p "Enter your OpenAI API key: " openai_api_key
echo $openai_api_key > key.txt
deactivate
