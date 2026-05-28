
def generate_mock_analysis(transcript: str):

    transcript_lower = transcript.lower()

    pain = "Invoice processing delays"
    metrics = "15% revenue leakage"
    buyer = "CFO and IT Director"

    if "revenue" not in transcript_lower:
        metrics = "Not clearly discussed"

    return {
        "meddic": {
            "Metrics": {
                "value": metrics,
                "confidence": "High",
                "quote": "Around 15% revenue leakage."
            },
            "Economic Buyer": {
                "value": buyer,
                "confidence": "Medium",
                "quote": "Our CFO and IT Director."
            },
            "Decision Criteria": {
                "value": "Automation and efficiency",
                "confidence": "Low",
                "quote": "Implicitly discussed"
            },
            "Decision Process": {
                "value": "Internal approval process",
                "confidence": "Low",
                "quote": "Not fully discussed"
            },
            "Identify Pain": {
                "value": pain,
                "confidence": "High",
                "quote": "We are struggling with invoice processing delays."
            },
            "Champion": {
                "value": "Operations team lead",
                "confidence": "Low",
                "quote": "Not clearly identified"
            }
        },

        "objections": [
            {
                "objection": "We already have a process in place",
                "category": "Competition",
                "handling": "Addressed",
                "suggestion": "Provide ROI comparison"
            }
        ],

        "deal_intelligence": {
            "deal_risk": 4,
            "risk_factors": [
                "Champion not identified",
                "Decision process unclear",
                "Budget timeline not discussed"
            ],
            "buying_signals": [
                "Customer discussed business pain",
                "Stakeholders identified"
            ],
            "next_actions": [
                "Rep will send case study by Friday",
                "Customer will schedule follow-up meeting"
            ]
        },

        "coaching": {
            "talk_ratio": "45% Rep / 55% Customer",
            "question_quality": "Good discovery questions",
            "top_coaching_points": [
                "Ask more about implementation timeline",
                "Identify internal champion earlier",
                "Explore budget process in detail"
            ]
        }
    }
