PACK = {
    "id": "teaching-education",
    "name": "Teaching & Education",
    "description": "Lesson plans, explanations, feedback and parent emails — for teachers, trainers and anyone who has to make something land.",
    "category": "productivity",
    "created": "2026-08-12",
    "tags": ["teaching", "education", "training", "learning"],
}

PROMPTS = [
    {
        "title": "Lesson Plan With One Objective",
        "description": "A single session built backwards from what learners must be able to do",
        "difficulty": "beginner",
        "content": """Plan a {{duration}} session on {{subject}} for {{grade_level}}.

Objective: {{learning_objective}}

Structure:
1. The check at the end that proves the objective was met — write this first
2. Opening hook, 5 minutes, that surfaces what they already believe
3. Input — the minimum explanation needed, with the one analogy you would keep
4. Practice — what learners DO, with the exact task wording
5. The check from step 1
6. What to cut if you lose 10 minutes

Rules:
- One objective. If two appear, pick the one the check can measure.
- Learners must be doing something within the first 12 minutes
- Name what you will NOT cover and why""",
    },
    {
        "title": "Explain It Three Ways",
        "description": "Same concept at three depths, so you can switch mid-lesson",
        "difficulty": "beginner",
        "content": """Explain {{concept}} to {{grade_level}}.

Give three versions:
1. One sentence, no jargon
2. A concrete example from their actual life, worked through step by step
3. The precise version, with the terms they will meet in exams or at work

Then:
- The analogy's breaking point — where it stops being true, stated plainly
- The check question that distinguishes real understanding from repeating words

Rules:
- Never use an analogy without saying where it fails
- No "imagine you have 10 apples" unless the apples do real work in the explanation""",
    },
    {
        "title": "Attack a Misconception",
        "description": "Plan the moment where a wrong idea gets replaced",
        "difficulty": "advanced",
        "content": """Learners of {{grade_level}} believe: {{misconception}}
Correct understanding: {{concept}}

Produce:
1. Why the wrong idea is reasonable — state it sympathetically, it usually works in some cases
2. The exact case where it fails, small enough to demonstrate in class
3. The demonstration or worked example, step by step
4. The question that reveals whether the correction stuck — where the old idea would give a different answer
5. What they will still get wrong next week, and the reminder that fixes it

Rules:
- Never just assert the correct version. Wrong ideas survive contradiction; they die from a failed prediction.""",
    },
    {
        "title": "Practice Questions With Rubric",
        "description": "A graded set of exercises plus how to mark them",
        "difficulty": "intermediate",
        "content": """Write practice questions on {{learning_objective}} for {{grade_level}}.

Produce 8 questions, ordered by difficulty:
- 3 that check the basic mechanic
- 3 that apply it in an unfamiliar situation
- 2 that require combining it with something learned earlier

For each: the answer, the most likely wrong answer, and what that wrong answer reveals.

Then a 4-level rubric describing what each level looks like in a learner's work.

Rules:
- No trick questions. Difficulty comes from transfer, not from wording.
- Every question answerable with what was actually taught""",
    },
    {
        "title": "Feedback on Student Work",
        "description": "Comments a learner can act on before the next attempt",
        "difficulty": "intermediate",
        "content": """Give feedback on this work from a {{grade_level}} learner.

Work: {{text}}
Objective: {{learning_objective}}

Structure:
1. What works, named specifically — quote the line
2. The single most important thing to change, and why it matters
3. Exactly how to do it differently — a rewritten example of one part
4. One question for the learner to answer themselves

Rules:
- One priority. A list of eight fixes gets none of them done.
- Address the work, never the person ("this paragraph assumes…" not "you always…")
- No praise sandwich — learners see through it and discount the praise""",
    },
    {
        "title": "Differentiate One Lesson",
        "description": "Adapt a single plan for the range actually in the room",
        "difficulty": "advanced",
        "content": """Adapt this lesson for a mixed group: {{context}}

Objective everyone must reach: {{learning_objective}}

Produce:
1. The core task everyone does
2. Support version — same task, scaffolded. Name the scaffold and when to remove it.
3. Extension — deeper, not more of the same. No busywork.
4. What the teacher watches for to decide who needs which, in the first 10 minutes
5. How this is arranged so nobody is publicly labelled

Rules:
- Same objective for all three. Differentiate the route, not the destination.
- Extension must be harder thinking, not extra questions""",
    },
    {
        "title": "Email to a Parent About a Problem",
        "description": "Raise a concern without triggering defensiveness",
        "difficulty": "intermediate",
        "content": """Write to the parent of a {{grade_level}} learner.

Concern: {{issue}}
Evidence: {{context}}
What I propose: {{resolution}}

Structure:
1. One specific positive that is actually true
2. The concern, described as observed behaviour with dates and examples
3. What I have already tried
4. What I am asking of them — one concrete thing
5. An offer to talk, with two proposed times

Rules:
- Observations, not diagnoses. No labels, no speculation about home life.
- No education jargon
- Under 200 words, written to be read on a phone""",
    },
    {
        "title": "Turn a Text Into a Worksheet",
        "description": "Convert reading material into structured practice",
        "difficulty": "beginner",
        "content": """Turn this material into a worksheet for {{grade_level}}.

Material: {{input}}
Objective: {{learning_objective}}

Produce:
1. Three comprehension questions answerable from the text
2. Two questions requiring inference beyond the text
3. One task that produces something (a diagram, a summary in 20 words, a counter-argument)
4. Vocabulary: the terms that will block understanding, with a one-line definition each
5. The answer key, including acceptable alternatives

Rules:
- No question whose answer is a single copied word
- Instructions written to the learner, in the imperative""",
    },
    {
        "title": "Course Outline From Scratch",
        "description": "Sequence a subject so each session earns the next",
        "difficulty": "advanced",
        "content": """Design a course on {{subject}} for {{audience}}, running {{duration}}.

Where they end: {{learning_objective}}

Produce:
1. The final capability, phrased as something they can do and show
2. Sessions in order — each with its objective and the check that closes it
3. The dependency map: which session must come before which, and why
4. The three points where learners typically drop out, and what is placed there to hold them
5. What is deliberately excluded

Rules:
- Every session ends in the learner producing something
- No session that is only theory
- If the sequence has a hard prerequisite outside the course, name it in session one""",
    },
    {
        "title": "Exit Ticket and Reteach Plan",
        "description": "A two-minute check plus what to do with each answer",
        "difficulty": "beginner",
        "content": """Write an exit ticket for {{learning_objective}}, answerable in two minutes.

Produce:
1. Two questions — one mechanical, one that requires transfer
2. What each possible wrong answer tells you
3. The reteach move for each failure mode, five minutes each
4. The threshold: at what share of the class you reteach to everyone rather than individually

Rules:
- No "how confident do you feel" self-report. Confidence is not evidence.
- Must be markable at a glance""",
    },
    {
        "title": "Group Work That Isn't One Person Working",
        "description": "Design a task where the group is actually necessary",
        "difficulty": "intermediate",
        "content": """Design group work on {{learning_objective}} for {{grade_level}}, {{duration}}.

Produce:
1. A task that cannot be completed by one person doing everything — state why
2. Roles with real decisions attached, not "timekeeper"
3. What each individual must produce alone, so the assessment is not collective
4. How the teacher intervenes when a group stalls, without taking over
5. The failure mode of this task and the early sign of it

Rules:
- If one strong learner could do it alone in half the time, redesign it""",
    },
    {
        "title": "Rewrite a Lesson That Fell Flat",
        "description": "Diagnose why a session failed and fix the actual cause",
        "difficulty": "advanced",
        "content": """This lesson did not work: {{context}}

What I observed: {{issue}}
Objective: {{learning_objective}}

Produce:
1. Three candidate causes: wrong prerequisite, too much input before doing, unclear task, or objective too large
2. The evidence that would distinguish them — what to look at in their work
3. The most likely cause, with reasoning
4. The rewritten section — only what changes, not the whole plan
5. What to check within the first 10 minutes next time

Rules:
- Do not attribute the failure to motivation or attention before ruling out design
- Change one thing, not everything""",
    },
]
