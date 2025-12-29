from flask import Flask, render_template, request
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
  
@app.route('/generate', methods=['GET', 'POST'])


def generate():
  if request.method == 'POST':  
    prompt_template = PromptTemplate.from_template("Generate a blog on title {title}?")
    llm = OpenAI(temperature=0.3) 
    chain = prompt_template | llm
    title = request.json.get('prompt')
    output = chain.invoke({"title": title})
    return output


app.run(host='0.0.0.0', port=5000)
