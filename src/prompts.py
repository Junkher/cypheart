from langchain import PromptTemplate

CYPHER_GENERATION_TEMPLATE = """你现在是一个Cypher语句生成模型，基于给定的Schema和Question，生成查询图数据库的Cypher语句。
Schema:{schema}
问题:{question}"""

CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)

CYPHER_QA_TEMPLATE = """你现在是一个帮助生成人类容易理解的答案的助手，请根据人类提供的信息生成答案。
信息：{context}
问题: {question}"""

CYPHER_QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"], template=CYPHER_QA_TEMPLATE
)


BASIC_QA_PROMPT = PromptTemplate(
    input_variables=["question"], template="{question}"
)