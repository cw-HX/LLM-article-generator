from flask import Flask, render_template, request
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
import markdown

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
  

@app.route('/generate', methods=['GET', 'POST'])
def generate():
  if request.method == 'POST':  
    prompt_template = PromptTemplate.from_template("Generate a blog on title {title}?")
    llm = ChatGroq(
        temperature=0.3,
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    ) 
    chain = prompt_template | llm
    title = request.json.get('prompt')
    output = chain.invoke({"title": title})
    # ChatGroq returns a BaseMessage, extract content and convert markdown to HTML
    html_content = markdown.markdown(output.content)
    return html_content


app.run(host='0.0.0.0', port=5000)
