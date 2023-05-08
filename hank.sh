function export_key {
  source www/.dev.vars
  export OPENAI_API_KEY=$OPENAI_API_KEY
}

function tmp {
  read -p "Name: " name
  source venv/bin/activate
  python3 main.py tmp $name
  deactivate
}

function bootstrap {
  python3 -m venv venv
  source venv/bin/activate
  python3 -m pip install -r requirements.txt
}

function www {
  source venv/bin/activate
  export_key
  python3 main.py model
  if [ $? -ne 0 ]; then
    echo "Model script did not exit successfully"
    deactivate
    return 1
  fi
  MODEL=$(cat model.txt)
  sed -i "s/model = '.*'/model = '$MODEL'/" www/src/index.js
  git add www/src/index.js model.txt
  git commit -m "Bump model to $MODEL"
  deactivate
  cd www
  npx wrangler publish
  cd ..
}

function transform {
  source venv/bin/activate
  python3 main.py transform
  if [ $? -ne 0 ]; then
    echo "Transform script did not exit successfully"
    deactivate
    return 1
  fi
  deactivate
}

function job {
  source venv/bin/activate
  openai api fine_tunes.follow -i $(cat job.txt)
  deactivate
}

function create {
  source venv/bin/activate
  export_key
  VERSION=$(cat version.txt)
  ((VERSION++))
  echo $VERSION > version.txt
  SUFFIX="hank-v$VERSION"
  echo "*************************************************"
  echo "Remember to save the fine-tune job ID to job.txt!"
  echo "*************************************************"
  openai api fine_tunes.create -t training.jsonl -m curie --suffix $SUFFIX
  git add version.txt www/src/index.js
  git commit -m "Bump to v$VERSION"
  deactivate
}

$1
