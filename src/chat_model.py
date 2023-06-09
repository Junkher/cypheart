from transformers import AutoTokenizer, AutoModel
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Optional, List

class ChatGLM(LLM):
    max_token: int = 10000
    temperature: float = 0.1
    history = []
    history_mode: bool = False
    tokenizer: object = None
    model: object = None

    @property
    def _llm_type(self) -> str:
        return "ChatGLM"

    def __init__(self, model_name: str="THUDM/chatglm-6b"):
        # print('__init__')
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_name, trust_remote_code=True).half().cuda()    
        self.model.eval()   

    def _call(self, 
              prompt: str, 
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None) -> str:
        response, history = self.model.chat(
            self.tokenizer,
            prompt,
            history=self.history,
            max_length=self.max_token,
            temperature=self.temperature,
        ) 
        if self.history_mode:   
          self.history = history  
        return response
   
