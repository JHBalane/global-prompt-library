PACK = {
    "id": "sales-outreach",
    "name": "Sales & Outreach",
    "description": "Cold emails, follow-ups, objections and proposals written like a person who has done the homework, not a sequence tool.",
    "category": "business",
    "created": "2026-08-12",
    "tags": ["sales", "outreach", "email", "b2b"],
}

PROMPTS = [
    {
        "title": "Cold Email With a Real Reason",
        "description": "First contact that earns a reply because it proves research",
        "difficulty": "beginner",
        "content": """Write a first cold email to {{prospect_name}}, {{role}} at {{prospect_company}}.

Why now: {{trigger_event}}
What we change for them: {{value_proposition}}
Evidence: {{proof_point}}

Structure:
1. One line that proves you looked at their specific situation
2. One line on the problem you suspect they have — as a question, not a claim
3. One sentence of evidence with a number
4. One ask, small enough to say yes to in a sentence

Rules:
- Under 90 words. No greeting paragraph, no company introduction.
- No "I hope this finds you well", "quick question", "circling back", "synergy"
- Never claim to know their pain. Ask.
- No attachments, no links in the first mail""",
    },
    {
        "title": "Follow-Up That Adds Something",
        "description": "A nudge that carries new information instead of guilt",
        "difficulty": "beginner",
        "content": """Write follow-up number {{context}} to {{prospect_name}} at {{prospect_company}}.

Original ask: {{goal}}
New thing I can offer: {{proof_point}}

Rules:
- Never mention that they did not reply. No "just following up", "bumping this", "in case you missed it".
- The mail must carry one new thing: a relevant example, a number, a resource — otherwise say nothing at all
- Under 60 words
- Make it trivially easy to say no: include one sentence giving them a graceful exit""",
    },
    {
        "title": "Answer an Objection Honestly",
        "description": "Handle a real concern without a rebuttal script",
        "difficulty": "intermediate",
        "content": """{{prospect_name}} at {{prospect_company}} raised this objection: {{objection}}

Our position: {{context}}

Produce:
1. What they most likely actually mean — two readings of the objection
2. The question you ask to find out which one it is
3. A straight answer for each reading, including the case where they are right and we are not a fit
4. What NOT to say

Rules:
- Never reframe a real limitation as a feature
- If we lose on this point, say so and name who they should use instead
- No "I understand how you feel, many of our customers felt…" formulas""",
    },
    {
        "title": "Post-Call Summary Email",
        "description": "Turn call notes into a summary that moves the deal",
        "difficulty": "beginner",
        "content": """Turn these notes into a follow-up email to {{prospect_name}}.

Notes: {{call_notes}}

Structure:
1. The problem in THEIR words, quoted back
2. What we agreed, as a short list
3. Who does what by when — named, dated
4. One open question that needs their answer

Rules:
- Nothing enters the summary that was not actually said on the call
- Mark anything you inferred with "I understood that…" so they can correct it
- No recap of your product
- Under 150 words""",
    },
    {
        "title": "Break-Up Email",
        "description": "Close a dead thread without passive aggression",
        "difficulty": "beginner",
        "content": """Write a final email to {{prospect_name}} at {{prospect_company}}. The thread is dead: {{deal_stage}}

Rules:
- State plainly that you are stopping, and that this is fine
- No guilt, no "should I close your file?", no fake urgency, no last-chance discount
- Leave one door genuinely open with a specific trigger: "if {{trigger_event}} changes, write me"
- Under 60 words""",
    },
    {
        "title": "Discovery Call Question Set",
        "description": "Questions that surface whether there is a deal at all",
        "difficulty": "intermediate",
        "content": """Prepare a discovery call with {{prospect_company}} about {{product}}.

What I already know: {{context}}

Give 10 questions grouped as:
- Situation today (what they do now, and what it costs them)
- Consequence (what happens if nothing changes)
- Decision (who decides, what the process is, what the budget is)

For each: the question, and what a disqualifying answer sounds like.

Rules:
- No question whose answer I could have found myself
- No pitching disguised as a question ("would it be helpful if…")
- Include the one question that most often reveals there is no real project""",
    },
    {
        "title": "One-Page Proposal",
        "description": "A proposal a busy person can decide on in two minutes",
        "difficulty": "intermediate",
        "content": """Write a one-page proposal for {{client_name}}.

Their problem: {{context}}
Scope: {{scope}}
Not included: {{out_of_scope}}
Price: {{rate}}
Timeline: {{timeline}}

Structure:
1. The problem, in their words, three sentences
2. What we do about it — plain description, no methodology names
3. What they get, as concrete artefacts
4. What is explicitly not included
5. Price and timeline, stated once, unhedged
6. What happens if they say yes today — first step only

Rules:
- No slogans. Write it as a colleague, not a vendor.
- No option A/B/C ladder unless the choices are genuinely different work
- Under 400 words""",
    },
    {
        "title": "Pricing Conversation Prep",
        "description": "Hold your number without bluffing",
        "difficulty": "advanced",
        "content": """Prepare for a pricing conversation with {{prospect_company}} about {{price}}.

Their likely pushback: {{objection}}
Our real floor: {{constraints}}

Produce:
1. The one-sentence justification of the price, in terms of their outcome
2. Three concessions that cost us little and what to demand in return for each
3. The point at which walking away is the right call, stated concretely
4. Wording for holding the price without arrogance

Rules:
- Never discount without removing scope. Say which scope.
- No invented ROI figures — if a number is an estimate, label it and show the arithmetic""",
    },
    {
        "title": "Referral Request",
        "description": "Ask a happy customer for an introduction, specifically",
        "difficulty": "beginner",
        "content": """Write a referral request to {{client_name}}, who is happy with {{product}}.

Result they got: {{proof_point}}
Who I want to meet: {{target_buyer}}

Rules:
- Name the type of person specifically. "Anyone who might need this" gets nothing.
- Include a forwardable paragraph they can paste without editing
- Make refusal easy and cost-free, in one sentence
- Under 100 words""",
    },
    {
        "title": "Competitive Positioning Without Trash Talk",
        "description": "Explain the difference to a prospect comparing you",
        "difficulty": "intermediate",
        "content": """{{prospect_company}} is comparing {{product}} with {{competitor}}.

Our actual difference: {{value_proposition}}

Produce:
1. Where the competitor is genuinely the better choice — say it first
2. Where we are better, tied to a situation rather than a feature list
3. Three questions the prospect should ask BOTH vendors to tell us apart
4. The honest summary in two sentences

Rules:
- No FUD, no "unlike others", no unnamed comparisons
- Every claim about the competitor must be verifiable by the prospect. If unsure, say "check this with them".""",
    },
    {
        "title": "Renewal or Churn-Risk Email",
        "description": "Reach out to a quiet account before it lapses",
        "difficulty": "intermediate",
        "content": """Write to {{client_name}}, whose renewal is at {{deadline}}. Usage has dropped.

What we know: {{context}}

Rules:
- Lead with a question about their outcome, not our renewal date
- Name the drop in usage as an observation, not an accusation
- Offer one concrete thing: a working session, a scope change, or an honest downgrade
- Include the option to cancel cleanly. Hiding it is how you get a bad review.
- Under 120 words""",
    },
    {
        "title": "Turn a Case Into a Proof Point",
        "description": "Compress a customer result into a usable sentence",
        "difficulty": "beginner",
        "content": """Turn this customer story into proof points.

Story: {{story}}

Produce:
1. One sentence with a number, usable in a cold email
2. A three-sentence version for a call
3. The claim stripped to what is strictly verifiable
4. What we must NOT claim from this story

Rules:
- No percentage without its base ("70% faster — from a day to two hours")
- Separate what the customer said from what we measured
- If the story does not actually support a number, say that plainly""",
    },
]
