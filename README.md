# Metro Mini Agent

Agentic AI demo for **predictive maintenance** in cognitive city infrastructure.

## Overview

This project implements a lightweight **agentic pipeline** that goes beyond defect detection:

- Perception (Vision-Language Model)
- Risk Scoring
- Decision Making
- Action Generation

## Pipeline

- Image → Perception → Risk → Decision → Action

## Sample Output (./cracks/sample.jpg)

```json
{
  "perception": {
    "defect_type": "Infrastructure Defect",
    "severity": 0.5,
    "confidence": 0.8,
    "location": "bottom-right",
    "recommended_action": "Immediate inspection and repair"
  },
  "risk_score": 0.4,
  "decision": "inspect",
  "action": "Schedule inspection"
}

