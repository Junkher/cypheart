from prompts import CYPHER_GENERATION_PROMPT, CYPHER_QA_PROMPT, BASIC_QA_PROMPT
from q_cypher_a_chain import GraphCypherQAChain
from langchain import LLMChain
from langchain.graphs import Neo4jGraph
from chat_model import ChatGLM
from dotenv import load_dotenv
import os

load_dotenv()
neo4j_url = os.environ.get("NEO4J_URL")
neo4j_user = os.environ.get("NEO4J_USER")
neo4j_password = os.environ.get("NEO4J_PWD")
model_path = os.environ.get("MODEL_PATH")

graph = Neo4jGraph(url=neo4j_url, username=neo4j_user, password=neo4j_password)
graph.refresh_schema()

print(model_path)
llm = ChatGLM(model_path)

domain_chain = GraphCypherQAChain.from_llm(llm=llm, 
                                    cypher_prompt=CYPHER_GENERATION_PROMPT, 
                                    qa_prompt=CYPHER_QA_PROMPT, 
                                    graph=graph, 
                                    verbose=True)

general_chain = LLMChain(prompt=BASIC_QA_PROMPT, llm=llm)

def get_load(question: str, mode: str):
  if mode == "domain":
    return domain_chain.run(question)
  else:
    return general_chain.run(question)


if __name__ == "__main__":
  print(domain_chain.run("与平安银行属于同一行业的股票有哪些，并告诉我股票代码。"))
