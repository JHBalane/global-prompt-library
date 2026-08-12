PACK = {
    "id": "customer-support",
    "name": "Customer Support",
    "description": "Ticket replies, apologies, refusals and outage notes that keep the customer instead of following a de-escalation script.",
    "category": "business",
    "created": "2026-08-12",
    "tags": ["support", "service", "email", "customers"],
}

PROMPTS = [
    {
        "title": "Reply to a Ticket",
        "description": "A straight answer to a support message, no service-desk theatre",
        "difficulty": "beginner",
        "content": """Answer this support message.

Message: {{customer_message}}
What is actually true: {{context}}
What I can offer: {{resolution}}

Structure:
1. The answer in the first sentence — yes, no, or here's how
2. The steps, numbered, if there are any
3. What happens next and by when
4. One line inviting a reply if it did not work

Rules:
- No "we apologise for any inconvenience", no "thank you for reaching out", no "I completely understand your frustration"
- Never promise a timeline you do not control
- If you do not know, say what you will do to find out and by when
- Match the customer's level of detail — do not explain the product to an expert""",
    },
    {
        "title": "Say No Without Losing the Customer",
        "description": "Refuse a request clearly and offer the nearest real thing",
        "difficulty": "intermediate",
        "content": """A customer asked for something we cannot do.

Their request: {{customer_message}}
Why we cannot: {{policy}}
Nearest thing we can do: {{resolution}}

Rules:
- The no comes in the first two sentences. Burying it wastes their time and reads as evasion.
- Give the real reason in one sentence. "Policy" alone is not a reason.
- Offer the nearest workable alternative, or say plainly that there is none
- No apology loop, no "unfortunately at this time"
- Under 120 words""",
    },
    {
        "title": "Apology for a Real Failure",
        "description": "Own a mistake without corporate fog",
        "difficulty": "intermediate",
        "content": """We got something wrong. Write the apology.

What happened: {{issue}}
How bad it was for them: {{severity}}
What we are doing: {{resolution}}

Structure:
1. What happened, factually, in one sentence
2. What it cost them — acknowledge the actual impact, not the inconvenience
3. What we are doing about it and when
4. What we are changing so it does not recur
5. Compensation, if any, stated without being asked twice

Rules:
- Active voice. "We deleted your data", not "data was lost".
- No "if you were affected", no "some users may have experienced"
- Do not ask for understanding
- No more than 150 words""",
    },
    {
        "title": "Bug Report From a Vague Ticket",
        "description": "Turn a frustrated message into something engineering can act on",
        "difficulty": "intermediate",
        "content": """Convert this customer message into a bug report.

Message: {{customer_message}}

Produce:
1. Title — one line, the observable failure
2. Steps to reproduce, as far as they can be inferred
3. Expected vs actual
4. What information is MISSING to reproduce it
5. The exact follow-up question to ask the customer — at most two questions
6. Severity, with the reason

Rules:
- Never invent steps the customer did not describe. Missing is missing.
- Strip emotion, keep facts, keep their exact wording where it is diagnostic""",
    },
    {
        "title": "Angry Customer, Real Answer",
        "description": "Respond to hostility by resolving, not by soothing",
        "difficulty": "advanced",
        "content": """A customer is angry.

Their message: {{customer_message}}
What is true: {{context}}
What I can do: {{resolution}}

Rules:
- Do not mirror the emotion, do not name their emotion back at them ("I hear that you're frustrated")
- Answer the substantive complaint first, in the first sentence
- Concede every point where they are right, explicitly
- Correct any factual error calmly and once
- If they were abusive, set one plain boundary without threatening
- Short sentences. Under 130 words.""",
    },
    {
        "title": "Outage or Incident Notice",
        "description": "Tell everyone what broke while it is still broken",
        "difficulty": "intermediate",
        "content": """Write a status update for an ongoing incident.

What is broken: {{issue}}
Who is affected: {{audience}}
What we know so far: {{context}}
Next update: {{deadline}}

Structure:
1. What is not working, in plain terms
2. Who it affects and what they should do meanwhile
3. What we know and what we do not
4. When the next update comes — a time, always

Rules:
- Publish before you have the cause. Uncertainty stated is better than silence.
- No "degraded performance" when it means "down"
- No blame, no vendor names, no speculation about cause
- Under 120 words""",
    },
    {
        "title": "Refund Decision Reply",
        "description": "Grant or refuse a refund in a way that reads as fair",
        "difficulty": "beginner",
        "content": """Answer a refund request.

Request: {{customer_message}}
Policy: {{policy}}
Decision: {{resolution}}

Rules:
- Decision first, always
- If granting: state the amount, the method and when it arrives. No conditions added afterwards.
- If refusing: give the specific rule and the date/fact it turns on, plus anything we CAN do
- Never make them ask twice
- No lecture about the policy they should have read""",
    },
    {
        "title": "Feature Request Reply",
        "description": "Answer 'can you build X' truthfully",
        "difficulty": "beginner",
        "content": """A customer asked for a feature.

Request: {{customer_message}}
Reality: {{context}}

Pick exactly one honest answer:
- Planned, with a rough timeframe we can defend
- Not planned, with the reason
- Possible today via a workaround — show the steps

Rules:
- Never say "great suggestion, I'll pass it to the team" as a way of saying no
- No roadmap promises without a date range you would repeat under pressure
- Ask one question about the underlying problem — the requested feature is often not the fix
- Under 100 words""",
    },
    {
        "title": "Help Article From a Repeated Ticket",
        "description": "Write the doc that stops the same question recurring",
        "difficulty": "intermediate",
        "content": """Write a help article for this recurring question.

Question: {{issue}}
The answer: {{context}}
Audience: {{audience}}

Structure:
1. Title phrased as the user would search it
2. The answer in the first two sentences, before any explanation
3. Steps, numbered, one action each
4. "If that didn't work" — the two most likely failure branches
5. Related setting or limit that surprises people

Rules:
- No introduction paragraph about why the feature exists
- Screenshots marked as [screenshot: what it shows]
- Second person, present tense, no "simply" or "just\"""",
    },
    {
        "title": "Cancellation Reply",
        "description": "Let someone leave cleanly and learn why",
        "difficulty": "beginner",
        "content": """A customer wants to cancel {{product}}.

Their message: {{customer_message}}

Rules:
- Confirm the cancellation in the first sentence, with the effective date and what happens to their data
- Exactly one question about why — optional to answer, no form
- One offer at most, only if it plainly matches their stated reason. No retention gauntlet.
- Say how to come back, in one line
- Under 90 words""",
    },
    {
        "title": "Macro Set for One Issue Type",
        "description": "Reusable replies that still sound human",
        "difficulty": "intermediate",
        "content": """Write a set of reusable replies for this recurring issue: {{issue}}

Known resolutions: {{resolution}}

Produce four variants:
1. Quick fix confirmed
2. Needs more information — with the two questions that matter
3. Known bug, fix in progress
4. Works as intended, but the expectation was reasonable

Each under 80 words, with [square-bracket] slots for the parts that must be personalised.

Rules:
- No greeting/sign-off boilerplate in the macro — that is the agent's job
- Every variant must be usable verbatim without sounding templated""",
    },
    {
        "title": "Weekly Support Summary",
        "description": "Turn a week of tickets into something product can act on",
        "difficulty": "advanced",
        "content": """Summarise this week of support for the product team.

Tickets: {{input}}

Produce:
1. The three issues by total volume, each with the customer's own phrasing
2. The one issue with the highest damage per occurrence, even if rare
3. What we told customers that we should stop saying
4. The single change that would remove the most tickets, with the estimated ticket count it saves

Rules:
- Counts, not adjectives. "17 tickets", not "a lot of complaints".
- Separate what customers asked for from what would actually fix their problem
- Mark any estimate as an estimate""",
    },
]
