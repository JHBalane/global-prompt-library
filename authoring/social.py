PACK = {
    "id": "social-content",
    "name": "Social Content",
    "description": "Hooks, scripts, captions and repurposing for people who post their own work — without the influencer voice.",
    "category": "creative",
    "created": "2026-08-12",
    "tags": ["social", "content", "video", "writing"],
}

PROMPTS = [
    {
        "title": "Ten Hooks From One Story",
        "description": "The first line is the whole battle — generate and rank options",
        "difficulty": "beginner",
        "content": """Write hooks for this: {{story}}

Platform: {{platform}}
Audience: {{audience}}

Give 10 first lines, each under 12 words, using different angles:
- The number that surprises
- The mistake I made
- The thing everyone believes that is wrong
- The before/after
- The specific moment

Then rank the top three and say what each one promises — and whether the content actually delivers it.

Rules:
- No "Here's why…", no "Let me tell you…", no question hooks that any account could post
- A hook that promises more than the content delivers is worse than a weak hook
- Must be readable and static in frame 0 — no hook that only works once it animates""",
    },
    {
        "title": "Short Video Script",
        "description": "A 30-second script with the beats timed",
        "difficulty": "intermediate",
        "content": """Write a {{duration}} script for {{platform}}.

Topic: {{topic}}
Point: {{lesson}}
Audience: {{audience}}

Format as a table of beats: time, spoken line, what is on screen.

Structure:
- 0–3 s: the hook, spoken and on screen
- 3–8 s: why this matters to them specifically
- 8 s–end: the substance, one idea, concrete
- Last 3 s: {{cta}}

Rules:
- Spoken lines must be sayable in one breath
- One idea per video. A second idea halves retention on both.
- No intro ("hey guys"), no outro sign-off, no "make sure to follow" before the value landed""",
    },
    {
        "title": "Turn Work Into a Post",
        "description": "Make a post out of something you actually did",
        "difficulty": "beginner",
        "content": """I did this: {{story}}

Platform: {{platform}}
Recurring theme of my account: {{content_pillar}}

Produce:
1. What is genuinely interesting here to someone who is not me
2. The post — the specific detail first, the general lesson second
3. What to leave out because it only matters to me

Rules:
- Process and specifics, not results as a flex
- No numbers that read as bragging; the interesting part is what went wrong and what it cost
- Write like telling a competent friend, no motivational register
- No hashtag block""",
    },
    {
        "title": "Carousel Outline",
        "description": "One idea per slide, built to be swiped to the end",
        "difficulty": "intermediate",
        "content": """Outline a carousel about {{topic}} for {{platform}}.

Audience: {{audience}}
Point: {{lesson}}

Produce 8 slides. Per slide: the headline (max 8 words) and the supporting line (max 20 words).

Rules:
- Slide 1 promises something specific; slide 2 must start delivering, not restate
- One idea per slide. If two fit, split them.
- Slide 8 is the payoff, not a "follow me" card
- Every slide must make sense if it is the only one someone screenshots""",
    },
    {
        "title": "Rewrite a Post That Flopped",
        "description": "Diagnose why it died before rewriting it",
        "difficulty": "advanced",
        "content": """This post did not land: {{text}}

Platform: {{platform}}
What I know about how it performed: {{context}}

Produce:
1. Three candidate causes: hook, topic-audience mismatch, no tension, or wrong format
2. What the performance pattern would look like for each cause — views vs watch-time vs saves
3. The most likely cause given what I said
4. One rewrite fixing that cause only
5. What to keep — flops usually contain one good line

Rules:
- Do not rewrite everything. Changing everything teaches nothing.
- If the post was fine and the topic was wrong, say that instead of polishing it""",
    },
    {
        "title": "Content From One Question",
        "description": "Turn a question you get asked into a week of posts",
        "difficulty": "beginner",
        "content": """People keep asking me: {{topic}}

My actual answer: {{context}}
Pillar: {{content_pillar}}

Produce 5 posts from this one question:
1. The direct answer
2. The wrong answer most people give, and why it fails
3. The story of when I learned it
4. The exception where the usual advice is wrong
5. The one-line version

For each: the format that fits it (video, carousel, text) and the hook.

Rules:
- Five posts, five different angles — not the same post five times
- Each must stand alone""",
    },
    {
        "title": "Caption for a Video",
        "description": "The text under the video, doing its own job",
        "difficulty": "beginner",
        "content": """Write the caption for a video about {{topic}} on {{platform}}.

What the video shows: {{context}}
Action I want: {{cta}}

Rules:
- Do not summarize the video. Add the thing that did not fit in it.
- First line visible before "more" must work alone
- One call to action, phrased as a specific question if you want comments
- No hashtag walls — at most three, only if the platform actually uses them
- Under 60 words""",
    },
    {
        "title": "Repurpose Long Into Short",
        "description": "Cut a long piece into standalone short pieces",
        "difficulty": "intermediate",
        "content": """Break this into short-form content: {{input}}

Target platform: {{platform}}

Produce:
1. The 5 strongest standalone moments, each with the exact quote or timestamp
2. Why each works alone, without the surrounding context
3. A hook per piece
4. What must NOT be cut short because it needs the full setup

Rules:
- A clip that needs "as I mentioned earlier" is not standalone
- Rank by strength, do not just take them in order""",
    },
    {
        "title": "Comment Reply Set",
        "description": "Answer comments without sounding automated",
        "difficulty": "beginner",
        "content": """Comments on a post about {{topic}}: {{input}}

Write replies for:
1. The genuine question
2. The disagreement with a fair point
3. The disagreement that is bad faith
4. The compliment
5. The one asking for something free

Rules:
- Each under 25 words
- Concede real points immediately; it is the cheapest credibility available
- Bad-faith reply: answer once, factually, and do not continue
- No emoji-only replies, no "great question!\"""",
    },
    {
        "title": "Weekly Content Plan",
        "description": "A plan built on what you already have, not on ideas",
        "difficulty": "intermediate",
        "content": """Plan a week of content for {{platform}}.

Pillar: {{content_pillar}}
What I actually did this week: {{context}}
Capacity: {{constraints}}

Produce:
1. Five posts, each tied to something real that happened — no invented topics
2. Per post: format, hook, and the one thing it should make the viewer think
3. Which one is the bet worth extra effort
4. What to drop first when the week goes wrong

Rules:
- Do not plan more than the stated capacity allows
- At least one post that risks being unpopular with the existing audience""",
    },
    {
        "title": "Rewrite in My Voice",
        "description": "Strip the LLM register out of a draft",
        "difficulty": "intermediate",
        "content": """Rewrite this in a plainer voice: {{text}}

Audience: {{audience}}
Tone: {{tone}}

Rules to apply:
- Cut every sentence that only sets up the next one
- Replace abstractions with the concrete thing they refer to
- Remove: "in today's world", "game-changer", "unlock", "leverage", "dive into", "it's not just X, it's Y", "here's the thing"
- No em-dash-and-triplet rhythm, no rhetorical question openers
- Keep contractions and short sentences
- Same meaning, roughly 60% of the length

Then list what you removed and why, so the pattern is visible next time.""",
    },
    {
        "title": "Profile Bio",
        "description": "A bio that says what someone gets by following",
        "difficulty": "beginner",
        "content": """Write a bio for {{platform}}.

What I do: {{context}}
What I post about: {{content_pillar}}
Who should follow: {{audience}}

Rules:
- What a follower gets, in the first line — not a job title, not a list of adjectives
- One concrete proof of competence, if there is one
- No "helping X do Y", no "building in public", no arrow-separated word chains
- One link, and say what is behind it
- Fit the platform's character limit and state which limit you used""",
    },
]
