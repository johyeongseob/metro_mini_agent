import json
from config import IMAGE_PATH

from models.loader import load_model
from perception.vision import perception
from utils.parser import extract_json_only

from agent.decision import decision_engine, compute_risk
from agent.action import action_generator


def main():
    processor, model = load_model()

    raw = perception(IMAGE_PATH, processor, model)
    parsed = extract_json_only(raw)

    decision = decision_engine(parsed)
    risk = compute_risk(parsed)
    action = action_generator(decision)

    print(json.dumps({
        "perception": parsed,
        "risk_score": risk,
        "decision": decision,
        "action": action
    }, indent=2))


if __name__ == "__main__":
    main()