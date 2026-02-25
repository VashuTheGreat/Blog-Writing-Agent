from langchain_aws import ChatBedrockConverse
LLM_MODEL_ID = "us.meta.llama3-3-70b-instruct-v1:0"
LLM_REGION = "us-east-1"
llm = ChatBedrockConverse(
    model_id=LLM_MODEL_ID,
    region_name=LLM_REGION
)