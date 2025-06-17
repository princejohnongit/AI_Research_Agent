from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search=DuckDuckGoSearchRun()
search_tool=Tool(name="search",
                  func=search.run,
                  description="Useful to search information on the Web")

api_wrapper=WikipediaAPIWrapper(top_k_result=1,doc_content_chars_max=10,
                                 )

wiki_tool=WikipediaQueryRun(api_wrapper=api_wrapper)