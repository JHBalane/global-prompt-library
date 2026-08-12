PACK = {
    "id": "hiring-recruiting",
    "name": "Hiring & Recruiting",
    "description": "Job ads, screening, interviews, offers and the rejections nobody likes writing — worded so candidates stay warm to you.",
    "category": "business",
    "created": "2026-08-12",
    "tags": ["hiring", "recruiting", "interviews", "hr"],
}

PROMPTS = [
    {
        "title": "Job Ad That Filters",
        "description": "A job ad that repels the wrong applicants instead of collecting hundreds",
        "difficulty": "beginner",
        "content": """You are a hiring manager writing a job ad for {{job_title}} at {{company}}.

Role facts:
- Seniority: {{seniority}}
- Must-haves: {{must_haves}}
- Nice-to-haves: {{nice_to_haves}}
- Team: {{team_description}}
- Compensation: {{salary_range}}

Write the ad so the WRONG people opt out. Structure:
1. One sentence on the actual problem this person will own
2. "What you'll do in the first 90 days" — three concrete outcomes, not responsibilities
3. "This is a bad fit if…" — three honest disqualifiers
4. Must-haves as a short list, nice-to-haves clearly marked optional
5. Compensation, stated plainly
6. How to apply, one step

Rules:
- No "rockstar", "ninja", "fast-paced environment", "wear many hats"
- No adjective without evidence — replace "collaborative team" with what the team actually does
- Under 350 words""",
    },
    {
        "title": "Screen a CV Against the Role",
        "description": "Structured first-pass read of a CV with the evidence quoted",
        "difficulty": "beginner",
        "content": """You are screening a candidate for {{job_title}}.

Must-haves: {{must_haves}}
Candidate background: {{candidate_background}}

Produce:
1. Verdict — advance / borderline / decline, one line
2. Evidence table: each must-have, met yes/no/unclear, and the exact line from the background that shows it
3. Three specific things to probe in a call, phrased as questions
4. Risks a CV cannot show

Rules:
- Never infer a skill that is not stated. "Unclear" is a valid and useful answer.
- Ignore school prestige, employment gaps, and years-of-experience as a proxy for skill.
- If the evidence is too thin to judge, say so instead of guessing.""",
    },
    {
        "title": "Interview Questions for One Role",
        "description": "Questions that test the actual work rather than personality",
        "difficulty": "intermediate",
        "content": """Design the questions for a {{interview_stage}} interview for {{job_title}}.

The work: {{context}}
Must-haves to test: {{must_haves}}

Give 6 questions. For each:
- The question, worded exactly as it should be asked
- What a strong answer contains
- What a weak answer sounds like
- One follow-up that separates the two

Rules:
- Every question must be about work the person has actually done, or a realistic scenario from this role
- No brain teasers, no "where do you see yourself", no culture-fit vibes questions
- At most one hypothetical""",
    },
    {
        "title": "Structured Interview Debrief",
        "description": "Turn messy interview notes into a decision, not a feeling",
        "difficulty": "intermediate",
        "content": """Turn these interview notes into a debrief for {{job_title}}.

Notes: {{call_notes}}
Must-haves: {{must_haves}}

Output:
1. Recommendation — hire / no hire / need one more signal
2. Per must-have: evidence observed, and how strong it was (strong / partial / none)
3. What we still do not know
4. The single cheapest next step to resolve the biggest doubt

Rules:
- Separate observation from interpretation. Quote what the candidate said before judging it.
- Flag any judgement that rests on likeability, communication polish, or shared background — those are bias, not signal.
- No score out of ten.""",
    },
    {
        "title": "Rejection That Doesn't Burn the Bridge",
        "description": "Honest, short, and specific enough to be useful",
        "difficulty": "beginner",
        "content": """Write a rejection email to {{candidate_name}}, who interviewed for {{job_title}}.

Honest reason: {{rejection_reason}}
Tone: {{tone}}

Rules:
- Decision in the first two sentences. No suspense build-up.
- Give the real reason in one specific sentence, without turning it into a performance review
- No "we were impressed by many strong candidates" filler, no "we'll keep your CV on file" unless it is true
- Offer exactly one genuine thing: feedback on request, a referral, or a note for a future role — only if you mean it
- Under 120 words, signed by a person""",
    },
    {
        "title": "Sourcing Message a Person Would Answer",
        "description": "Cold outreach to a passive candidate that isn't recruiter spam",
        "difficulty": "beginner",
        "content": """Write a first message to {{candidate_name}}, a passive candidate for {{job_title}} at {{company}}.

What made you contact them: {{trigger_event}}
The interesting part of the role: {{context}}
Compensation: {{salary_range}}

Rules:
- First line must prove you looked at their actual work — no "your impressive profile"
- Say the salary range. Not saying it is the reason these messages get ignored.
- One question at the end that is answerable in one line
- No company boilerplate, no "exciting opportunity", no bullet lists of perks
- Under 90 words""",
    },
    {
        "title": "Take-Home Task Worth Doing",
        "description": "A small task that predicts the job and respects the candidate's time",
        "difficulty": "advanced",
        "content": """Design a take-home task for {{job_title}}.

Real work this role does: {{context}}
Skills to observe: {{must_haves}}
Time budget: {{duration}}

Produce:
1. The task brief exactly as the candidate receives it
2. Why this predicts on-the-job performance
3. A scoring rubric with 4 criteria and what 'strong' looks like for each
4. What you will explicitly NOT judge

Rules:
- Must be completable inside the stated time. Say what to skip if time runs out.
- No unpaid work the company would otherwise pay for
- Ambiguity is allowed only if handling ambiguity is part of the job — then say so""",
    },
    {
        "title": "Offer Call Script",
        "description": "Deliver an offer so it is accepted, without pressure tactics",
        "difficulty": "intermediate",
        "content": """Prepare a script for offering {{job_title}} to {{candidate_name}} at {{salary_range}}.

What they said mattered to them: {{context}}

Produce:
1. Opening — the offer itself, in the first 20 seconds
2. Three sentences connecting the offer to what THEY said they wanted
3. Answers to the three most likely objections
4. The deadline, framed as a real constraint, not a squeeze
5. What to do if they ask for more money

Rules:
- No exploding offers, no "we have other candidates" pressure
- Never say the number is final unless it is
- Written to be spoken aloud: short sentences""",
    },
    {
        "title": "Onboarding Plan, First 30 Days",
        "description": "A concrete plan so a new hire is useful in week one",
        "difficulty": "intermediate",
        "content": """Write a 30-day onboarding plan for a new {{job_title}}.

Team: {{team_description}}
What they will own: {{context}}

Structure:
- Day 1: three things, ending with something they shipped or produced
- Week 1: the first real contribution, plus who they meet and why
- Week 2–4: one owned deliverable with a named reviewer
- The five things that must be ready BEFORE day 1

Rules:
- Every item names a person responsible, not a department
- No week of reading documentation
- Include how you will notice, by day 10, that this hire is going badly""",
    },
    {
        "title": "Rewrite a Job Ad in Plain Language",
        "description": "Strip corporate fog out of an existing ad",
        "difficulty": "beginner",
        "content": """Rewrite this job ad in plain language.

Ad: {{text}}

Output:
1. The rewritten ad
2. A short list of the vague claims you removed and what you replaced them with
3. Any requirement that looks like it will exclude good candidates for no reason (e.g. a degree, a years-count, a specific tool that is learnable in a week)

Rules:
- Keep every fact. Remove every adjective that has no evidence behind it.
- Same meaning, roughly half the words""",
    },
    {
        "title": "Reference Call Questions",
        "description": "Questions that get past 'they were great to work with'",
        "difficulty": "intermediate",
        "content": """Prepare a reference call about {{candidate_name}}, who we are hiring as {{job_title}}.

The doubt we want resolved: {{context}}

Give 8 questions in order, each with the follow-up to use if the answer is vague.

Rules:
- Ask for examples and behaviour, never for ratings or opinions
- Include one question that makes it easy to say something negative
- End with: "Who else worked closely with them that I should speak to?"
- Note which answers would be a genuine red flag versus normal friction""",
    },
    {
        "title": "Salary Benchmark Argument",
        "description": "Build the internal case for a specific number",
        "difficulty": "advanced",
        "content": """Build the internal argument for paying {{salary_range}} for {{job_title}} at {{company}} in {{location}}.

Constraint we face: {{constraints}}

Produce:
1. The number, and what it buys us
2. The cost of underpaying, quantified: time-to-hire, offer decline rate, replacement cost
3. Three counter-arguments finance will raise, and the answer to each
4. The fallback: what to offer instead if the number is refused — and what that costs us

Rules:
- Mark every figure as either a known fact from our own data or an assumption. Never blur the two.
- If you do not have salary data for this market, say what data would settle it rather than inventing a benchmark.""",
    },
]
