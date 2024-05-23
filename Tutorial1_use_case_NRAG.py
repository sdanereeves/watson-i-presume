# Tutorial1_use_case_NRAG
# Copyright (c) Secondary content - Steven D. Reeves IBM
# WML python SDK
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods

# URL of the hosted LLMs is hardcoded because at this time all LLMs share the same endpoint
url = "https://us-south.ml.cloud.ibm.com"


#Variable tracing
#print(url)
#print(watsonx_project_id)
#print(api_key)

# The get_model function creates an LLM model object with the specified parameters
def get_model(model_type,max_tokens,min_tokens,decoding,temperature):

    generate_params = {
        GenParams.MAX_NEW_TOKENS: max_tokens,
        GenParams.MIN_NEW_TOKENS: min_tokens,
        GenParams.DECODING_METHOD: decoding,
        GenParams.TEMPERATURE: temperature
    }

    model = Model(
        model_id=model_type,
        params=generate_params,
        credentials={
            "apikey": api_key,
            "url": url
        },
        project_id=watsonx_project_id
        )

    return model

def main():

    # Ask a question relevant to the info in the document
    # You can try asking different questions
    #question = "Who is Oracle?"
    #prompt = "Answer the question provided in '''.  Give specific use cases. Question: ''' "
    #prompt = "Answer the question provided in '''.   Question: ''' "
    #question = "Answer the question provided in '''.  Give specific use cases. Question: ''' I have a client who is a wine company with about 100K customers having their data stored in one place. They are looking for a solution with a use case to look into historical data and get insights on trends and triggers that tell them the behavior of their customers, for example who are their loyal customers. How can they use predictive analytics ? '''"
    print(question)
    answer_questions_from_doc(api_key, watsonx_project_id, question)

def answer_questions_from_doc(request_api_key, request_project_id, question):

    # Update the global variable
    globals()["api_key"] = request_api_key
    globals()["watsonx_project_id"] = request_project_id

    # Specify model parameters
    #model_type = "meta-llama/llama-2-70b-chat"
    model_type = "meta-llama/llama-3-70b-instruct"
    max_tokens = 800
    min_tokens = 200
    decoding = DecodingMethods.GREEDY
    temperature = 0.7

    # Get the watsonx model
    model = get_model(model_type, max_tokens, min_tokens, decoding, temperature)

    # Get the prompt
    complete_prompt = question

    # Let's review the prompt
    print("----------------------------------------------------------------------------------------------------")
    print("*** Prompt:" + complete_prompt + "***")
    print("----------------------------------------------------------------------------------------------------")

    generated_response = model.generate(prompt=complete_prompt)
    response_text = generated_response['results'][0]['generated_text']

    # print model response
    #print("--------------------------------- Generated response -----------------------------------")
    #response_text="This is stubbed"
    print(response_text)
    #print("*********************************************************************************************")

    return response_text

# Invoke the main function
if __name__ == "__main__":
    main()

