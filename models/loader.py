import torch
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration
from config import MODEL_NAME

def load_model():
    processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        use_fast=False,
    )

    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        torch_dtype=torch.float16
    )

    model.generation_config.temperature = None
    model.eval()

    return processor, model