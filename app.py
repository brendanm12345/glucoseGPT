import os
import sys
from dotenv import load_dotenv
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv()

db = SQLDatabase.from_uri(os.getenv("DBURI"))
llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAPI_API_KEY"))

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

if len(sys.argv) > 1:
    query = sys.argv[1]
    db_chain.run(query)

# queries = [
#     "How different PtIDs are there?",
#     "What is the max number of days from enroll?",
#     "What was Patient 1's highest glucose value on the fifth day after enrolling?"
# ]

# for query in queries:
#     db_chain.run(query)
