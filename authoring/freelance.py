PACK = {
    "id": "freelance-client-work",
    "name": "Freelance & Client Work",
    "description": "Scoping, quoting, chasing invoices and saying no to scope creep — the paperwork that decides whether the work was worth it.",
    "category": "business",
    "created": "2026-08-12",
    "tags": ["freelance", "clients", "proposals", "invoicing"],
}

PROMPTS = [
    {
        "title": "Scoping Questions Before Quoting",
        "description": "The questions that stop you from quoting a project you don't understand",
        "difficulty": "beginner",
        "content": """A prospective client wants: {{scope}}
What they told me: {{context}}

Give the questions I must answer before quoting, grouped as:
- Outcome (what changes for them when this is done, how they will judge it)
- Constraints (deadline, budget, systems, approvals)
- Ownership (who decides, who reviews, who else must agree)
- Aftermath (who runs this once I leave)

For each question, add what a worrying answer sounds like.

Rules:
- No more than 12 questions total
- Include the one question that most often reveals the project is not funded""",
    },
    {
        "title": "Fixed-Price Quote",
        "description": "A quote with the boundaries written down before the work starts",
        "difficulty": "intermediate",
        "content": """Write a quote for {{client_name}}.

Work: {{scope}}
Not included: {{out_of_scope}}
Deliverable: {{deliverable}}
Price: {{rate}}
Timeline: {{timeline}}

Structure:
1. What you get — the deliverable, concretely
2. How we get there — phases with a date each
3. What is not included, listed plainly
4. What I need from you, with dates — and what happens to the timeline if it is late
5. Price, payment schedule, validity date

Rules:
- Every phase ends in something the client can see
- Name the change process for extra work, with a rate, before it is needed
- Colleague tone, no agency slogans
- Under 450 words""",
    },
    {
        "title": "Scope Creep Reply",
        "description": "Say yes to the work and no to doing it for free",
        "difficulty": "intermediate",
        "content": """The client wants something extra: {{change_request}}

Agreed scope: {{scope}}
My rate: {{rate}}

Rules:
- Start with a plain yes — this is doable
- Then state what it costs in time and money, and what it does to the current deadline
- Offer the trade: add it, swap it for something already in scope, or do it after delivery
- No guilt, no reference to how much extra you already did unpaid
- Never say "that wasn't in scope" as the opening line
- Under 120 words""",
    },
    {
        "title": "Chase an Overdue Invoice",
        "description": "Escalating reminders that stay professional and get paid",
        "difficulty": "beginner",
        "content": """Write invoice reminders for {{client_name}}.

Invoice: {{price}}, due {{deadline}}
Relationship: {{context}}

Produce three escalating messages:
1. Day 3 overdue — friendly, assumes an oversight, restates payment details
2. Day 14 — plain, names the amount and the due date, asks for a payment date
3. Day 30 — states consequences you will actually carry out (work paused, late fee, handover withheld)

Rules:
- Never apologise for asking to be paid
- Every message repeats the amount, invoice number slot, and payment details
- No threats you will not execute
- Each under 90 words""",
    },
    {
        "title": "Project Status Update",
        "description": "A weekly update that prevents surprises",
        "difficulty": "beginner",
        "content": """Write this week's update for {{client_name}}.

Progress: {{context}}
Blockers: {{issue}}
Next: {{goal}}

Structure:
1. Status in one word — on track / at risk / late — and one sentence why
2. Done this week, as things they can look at
3. Blocked, with what I need from whom by when
4. Next week
5. Anything that changes the date or the price — stated here, never later

Rules:
- Bad news goes at the top, never buried in point 3
- No effort narratives ("worked hard on"), only outcomes
- Under 200 words""",
    },
    {
        "title": "Say No to a Project",
        "description": "Decline work without burning the relationship",
        "difficulty": "beginner",
        "content": """Decline this project from {{client_name}}: {{scope}}
Real reason: {{context}}

Rules:
- No in the first sentence, no build-up
- One honest sentence of reason — capacity, fit, or budget. Do not invent a nicer reason.
- Refer someone specific if you can, or say what kind of person they need
- Leave a real door open only if you mean it
- Under 80 words""",
    },
    {
        "title": "Raise Your Rates",
        "description": "Tell an existing client the price is going up",
        "difficulty": "advanced",
        "content": """Tell {{client_name}} that my rate goes from {{price}} to {{rate}}.

Relationship: {{context}}
Effective: {{deadline}}

Structure:
1. The new number and the date it starts — first two sentences
2. One sentence of reason, not an apology and not a cost-of-living essay
3. What stays the same for them
4. A transition option: the old rate honoured for current work, or a lower-scope package

Rules:
- Do not ask permission and do not negotiate against yourself
- No lengthy justification — length reads as doubt
- Under 120 words""",
    },
    {
        "title": "Kickoff Agenda and Ground Rules",
        "description": "Set the working rules while everyone is still friendly",
        "difficulty": "intermediate",
        "content": """Prepare the kickoff for {{client_name}} on {{scope}}.

Timeline: {{timeline}}

Produce:
1. Agenda with times, 45 minutes total
2. The decisions that must be made in this meeting, listed
3. Working rules to agree out loud: response times, review turnaround, who signs off, where files live, how change requests happen
4. The three assumptions I am making that they must confirm or correct

Rules:
- Every ground rule states the consequence if it slips
- No round of introductions longer than five minutes""",
    },
    {
        "title": "Handover Document",
        "description": "Leave the work usable by someone who has never met you",
        "difficulty": "intermediate",
        "content": """Write the handover for {{deliverable}} delivered to {{client_name}}.

What was built: {{context}}

Structure:
1. What this is and what it does, for a non-technical reader
2. How to run/change/publish it — the three most common tasks, step by step
3. Access and accounts: what exists, who owns it, what it costs
4. Known limitations and what to do about each
5. What breaks first if nobody maintains it, and the cheapest prevention

Rules:
- Assume the reader has never spoken to me
- No links to my own tools they cannot access
- Name every recurring cost with its renewal date slot""",
    },
    {
        "title": "Testimonial Request",
        "description": "Ask for a reference that is actually usable",
        "difficulty": "beginner",
        "content": """Ask {{client_name}} for a testimonial about {{deliverable}}.

Result they got: {{proof_point}}

Rules:
- Ask three specific questions instead of "would you write a testimonial" — the answers become the quote
- Offer to draft it from their answers and let them edit
- Say exactly where it will appear
- Make no a comfortable answer
- Under 100 words""",
    },
    {
        "title": "Estimate a Project Honestly",
        "description": "Break work into estimable parts and expose the uncertainty",
        "difficulty": "advanced",
        "content": """Estimate this project: {{scope}}

What I know: {{context}}
Constraints: {{constraints}}

Produce:
1. Work breakdown — tasks of at most one day each
2. Per task: optimistic / likely / pessimistic in hours
3. The three biggest uncertainties, each with what would resolve it and what it could cost if it goes wrong
4. A recommended quote with the buffer stated separately, not hidden in the tasks
5. What to cut first if the budget is half this

Rules:
- No task larger than a day — if it cannot be split, it is not understood
- Name every assumption. Unstated assumptions become unpaid work.""",
    },
    {
        "title": "Fire a Client",
        "description": "End a working relationship cleanly and in writing",
        "difficulty": "advanced",
        "content": """End the engagement with {{client_name}}.

Reason: {{context}}
Current state of work: {{deliverable}}
Notice period: {{deadline}}

Structure:
1. The decision and the last working day, first sentence
2. What will be finished before then, and what will not
3. Handover: files, access, documentation, and the date each arrives
4. Outstanding invoices and what is owed
5. One neutral closing line

Rules:
- No blame, no grievance list, no "as you know"
- Never leave the deliverable in a state only I can rescue
- Written so it reads fine if forwarded to their lawyer
- Under 180 words""",
    },
]
