from langchain.agents.agent import AgentExecutor
from langchain.agents.tools import Tool
from langchain.agents import initialize_agent, AgentType
from q_cypher_a_chain import GraphCypherQAChain
from chat_model import ChatGLM

class JunkAgent(AgentExecutor):
    @staticmethod
    def function_name():
        return "junkagent"

    @classmethod
    def initialize(cls, graph, model_name, *args, **kwargs):
        llm = ChatGLM(model_name)

        cypher_tool = GraphCypherQAChain(
            llm=llm, graph=graph, verbose=True
        )
        tools = [
            Tool(
              name="Cypher search",
              func=cypher_tool.run,
              description="bullshit"
            )
        ]

        agent_chain = initialize_agent(
            tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True
        )

        return agent_chain
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)