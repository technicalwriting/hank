import {p, e} from './data.json';

export default {
  async fetch(request, env, ctx) {
    const url = 'https://api.openai.com/v1/completions';
    const model = 'curie:ft-personal:hank-v5-2023-05-07-03-53-02';
    const stopSequence = '( ͡° ͜ʖ ͡°)';
    const prompt = p;
    const expected = e;
    const promptWithStopSequence = `${prompt}${stopSequence}`;
    const requestOptions = {
      'method': 'POST',
      'headers': {
        'Content-Type': 'application/json',
        // https://developers.cloudflare.com/workers/platform/environment-variables/#add-secrets-to-your-project
        'Authorization': `Bearer ${env.OPENAI_API_KEY}`,
      },
      'body': JSON.stringify({
	'prompt': promptWithStopSequence,
        'model': model,
        'temperature': 0,
        'stop': stopSequence,
      }),
    };
    const response = await fetch(url, requestOptions);
    const json = await response.json();
    const completion = json.choices[0].text;
    const responseOptions = {
      'headers': {
        'content-type': 'text/html; charset=utf-8',
      },
    };
    const html = `<!doctype html>
	<html lang="en">
	  <head>
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1">
	    <title>hank</title>
	  </head>
	  <body>
	    <h1>hank</h1>
	    <p>Model: ${model}</p>
	    <h2>Original</h2>
	    <p>${prompt}</p>
	    <h2>Expected</h2>
	    <p>${expected}</p>
	    <h2>Actual</h2>
	    <p>${completion}</p>
	    <h2>Debug</h2>
	    <pre><code>${JSON.stringify(json, null, 2)}</code></pre>
	  </body>
	</html>`;
    return new Response(html, responseOptions);
  },
};
