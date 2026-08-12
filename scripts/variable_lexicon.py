#!/usr/bin/env python3
"""
Shared vocabulary for prompt variables.

Every `{{variable}}` used anywhere in the library resolves its description and
example from here, so the same placeholder means the same thing in every pack
and the app's variable fields read consistently. Adding a variable to a prompt
without adding it here is a build warning, not a silent fallback with a worse
description.
"""

# name -> (description, example)
LEXICON: dict[str, tuple[str, str]] = {
    # --- universal ---
    "topic": ("What the text is about", "our move to a four-day week"),
    "audience": ("Who will read this", "non-technical hospital administrators"),
    "tone": ("Voice to write in", "direct and warm, no corporate filler"),
    "goal": ("What this should achieve", "get a 15-minute call booked"),
    "context": ("Background the model needs", "we shipped late twice this quarter"),
    "constraints": ("Hard limits to respect", "under 150 words, no bullet points"),
    "language": ("Language to answer in", "German (Sie-form)"),
    "length": ("Target length", "3 short paragraphs"),
    "format": ("Shape of the output", "a table with columns Risk / Impact / Fix"),
    "text": ("The text to work on", "paste your draft here"),
    "input": ("The material to work from", "paste notes, transcript or data here"),
    "deadline": ("Relevant date or timeframe", "Friday, end of business"),
    "name": ("Person's name", "Maria Sander"),
    "company": ("Company name", "Nordwind Logistik GmbH"),
    "role": ("Job title or function", "Head of Operations"),
    "product": ("Product or service name", "TextDeck"),
    "price": ("Price and terms", "€49 per seat/month, billed yearly"),
    "industry": ("Industry or sector", "regional logistics"),
    "channel": ("Where this will be published or sent", "LinkedIn post"),
    "budget": ("Money available", "€2,500 one-off"),
    "timeline": ("Time available", "six weeks, hard stop"),
    "expert_role": ("Expertise the model should take on", "employment lawyer"),
    "output_format": ("Exact structure the answer must follow", "numbered list, one line each"),

    # --- hiring / recruiting ---
    "job_title": ("Role being filled", "Senior Backend Engineer (Go)"),
    "seniority": ("Experience level", "5+ years, first lead role"),
    "must_haves": ("Non-negotiable requirements", "Go in production, on-call experience"),
    "nice_to_haves": ("Desirable but optional", "Kubernetes, German B2"),
    "candidate_name": ("Candidate's name", "Jonas Weber"),
    "candidate_background": ("Candidate's relevant history", "6 years at a payments startup, led 3 engineers"),
    "salary_range": ("Compensation on offer", "€75–90k plus equity"),
    "rejection_reason": ("Honest reason the candidate was not chosen", "another candidate had deeper on-call experience"),
    "interview_stage": ("Which round this is", "second round, technical deep-dive"),
    "team_description": ("Who the hire will work with", "four engineers, no manager layer, remote-first"),

    # --- sales / outreach ---
    "prospect_name": ("Person you are writing to", "Dr. Anke Reuter"),
    "prospect_company": ("Their company", "Stadtwerke Aalen"),
    "trigger_event": ("Why you are reaching out now", "they posted three warehouse roles this month"),
    "value_proposition": ("The change you create for them", "cuts shift planning from a day to an hour"),
    "objection": ("The concern they raised", "we already pay for a tool that does this"),
    "competitor": ("Who they compare you to", "an in-house Excel process"),
    "deal_stage": ("Where the deal stands", "demo done, no reply for 12 days"),
    "call_notes": ("Raw notes from the conversation", "paste your notes here"),
    "proof_point": ("Evidence that you deliver", "Ernst Logistik cut planning time 70% in 4 weeks"),

    # --- support ---
    "customer_message": ("What the customer wrote", "paste the ticket here"),
    "issue": ("The problem in one line", "invoice PDF is empty for yearly plans"),
    "resolution": ("What you can actually offer", "refund this month, fix ships Thursday"),
    "policy": ("Rule you must stay inside", "refunds only within 30 days"),
    "severity": ("How bad it is for the customer", "blocking — they cannot invoice at all"),

    # --- freelance / client work ---
    "scope": ("What is included in the work", "audit, report, one implementation call"),
    "out_of_scope": ("What is explicitly not included", "ongoing maintenance, hosting costs"),
    "deliverable": ("What the client receives", "a 12-page written audit plus a Loom walkthrough"),
    "client_name": ("Client's name or company", "Praxis Dr. Neumann"),
    "rate": ("Your price or rate", "€1,200 fixed"),
    "change_request": ("What the client now wants added", "two more languages and a second dashboard"),

    # --- teaching / learning ---
    "subject": ("Subject or course", "9th-grade chemistry"),
    "grade_level": ("Age or level of the learners", "15–16 year olds, mixed ability"),
    "learning_objective": ("What learners should be able to do afterwards", "balance simple redox equations"),
    "misconception": ("The common mistake to address", "that electrons are 'used up'"),
    "duration": ("How long the session is", "45 minutes"),
    "concept": ("The idea being taught", "opportunity cost"),

    # --- ecommerce / retail ---
    "product_features": ("Concrete features and specs", "merino wool, 250g, machine washable"),
    "customer_problem": ("What the buyer is trying to solve", "shirts that smell after one wear"),
    "marketplace": ("Where it is sold", "Etsy"),
    "keywords": ("Search terms to work in", "merino t-shirt, odor resistant, travel shirt"),
    "review_text": ("The customer review", "paste the review here"),
    "return_reason": ("Why the item came back", "sizing ran small"),

    # --- real estate ---
    "property_type": ("Kind of property", "3-room flat, 1960s building"),
    "location": ("Where it is", "Munich, Westend"),
    "property_features": ("Notable features and condition", "82 m², balcony south, needs a new kitchen"),
    "target_buyer": ("Who it suits", "first-time buyers, couple without children"),
    "asking_price": ("Price asked", "€549,000"),

    # --- social / content ---
    "hook": ("The opening line that stops the scroll", "I shipped 12 apps last year. Nobody used 9."),
    "platform": ("Social platform", "TikTok"),
    "content_pillar": ("Recurring theme of the account", "building software alone"),
    "cta": ("What the viewer should do next", "comment 'audit' for the checklist"),
    "story": ("The real thing that happened", "our launch got 3,000 downloads and 2 reviews"),
    "lesson": ("The takeaway worth someone's time", "downloads measure curiosity, not value"),

    # --- development ---
    "code": ("The code to work on", "paste the snippet here"),
    "language_or_stack": ("Language and framework", "Swift 6 / SwiftUI"),
    "error_message": ("The exact error", "paste the full error and stack trace"),
    "expected_behavior": ("What should happen", "the panel closes and pastes into the previous app"),
    "actual_behavior": ("What happens instead", "the panel closes, clipboard unchanged"),
}


def humanize(name: str) -> str:
    return name.replace("_", " ").strip().capitalize()


def lookup(name: str) -> tuple[str, str | None]:
    """Return (description, example). Unknown names degrade to a humanized
    description with no example — and the caller warns about it."""
    if name in LEXICON:
        desc, example = LEXICON[name]
        return desc, example
    return humanize(name), None
