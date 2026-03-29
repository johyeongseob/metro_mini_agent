from PIL import Image
import torch


def perception(image_path, processor, model):
    image = Image.open(image_path).convert("RGB")

    # ---------- Prompt 강화 ----------
    messages = [
        {
            "role": "system",
            "content": "You are a strict JSON generator. Output ONLY raw JSON. Never use markdown."
        },
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {
                    "type": "text",
                    "text": (
                        "Analyze infrastructure defects.\n\n"
                        "Return ONLY valid JSON.\n"
                        "No markdown. No explanation. No extra text.\n\n"

                        "Constraints:\n"
                        "- severity: float [0,1]\n"
                        "- confidence: float [0,1]\n"
                        "- location: one of [top-left, top-right, center, bottom-left, bottom-right]\n\n"

                        "Output EXACTLY this schema:\n"
                        '{"defect_type": "", "severity": 0.0, "confidence": 0.0, "location": "", "recommended_action": ""}'
                    )
                }
            ],
        }
    ]
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = processor(
        text=[text],
        return_tensors="pt"
    )

    # ---------- device 자동 처리 ----------
    device = model.device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # ---------- 안정적인 generation ----------
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128,
            do_sample=False,
            temperature=None,
            repetition_penalty=1.05
        )

    result = processor.batch_decode(outputs, skip_special_tokens=True)[0]

    return result