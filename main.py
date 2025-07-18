from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent,AgentExecutor
from tools import search_tool,wiki_tool,save_tool

load_dotenv()
#API_KEY=
#llm=ChatOpenAI(model="gpt-4o",)

class ResearchResponse(BaseModel):
    topic:str
    summary:str
    sources:list[str]
    tools_used:list[str]

llm=ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser=PydanticOutputParser(pydantic_object=ResearchResponse)
prompt=ChatPromptTemplate.from_messages(
    [
        (
            'system',
            """You are a helpful research assistant that will help generate
            a research paper. Answer the user query and use neccesary tools.
            Wrap the output in this format and provide no other 
            text\n{format_instructions}
            """,
          ),
         ("placeholder","{chat_histroy}"),
         ("human","{query}"),
         ("placeholder","{agent_scratchpad}")
    ]).partial(format_instructions=parser.get_format_instructions())

tools=[search_tool,wiki_tool,save_tool]
agent=create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
query=input("What can i help to reasearch for you? ")
raw_response=None
#print(raw_response)
try:
    agent_executor=AgentExecutor(agent=agent,tools=[],verbose=True)
    raw_response=agent_executor.invoke({"query": query})
    structured_response=parser.parse(raw_response.get('output'))[0]["text"]
    print(structured_response)
except Exception as e:
    print("Error Parsing REsponse",e,"-------Raw_repsonse----- ", raw_response)


