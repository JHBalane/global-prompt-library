PACK = {
    "id": "ecommerce-seller",
    "name": "Online Selling",
    "description": "Listings, product copy, reviews and returns for people who sell things online — Etsy, Amazon, Shopify or their own shop.",
    "category": "business",
    "created": "2026-08-12",
    "tags": ["ecommerce", "etsy", "listings", "retail"],
}

PROMPTS = [
    {
        "title": "Product Listing That Answers Objections",
        "description": "A listing written around the reasons people don't buy",
        "difficulty": "beginner",
        "content": """Write a product listing for {{product}} on {{marketplace}}.

Features: {{product_features}}
Buyer's problem: {{customer_problem}}
Who it is for: {{target_buyer}}
Price: {{price}}

Structure:
1. Title — what it is, who it is for, the one distinguishing spec
2. First three lines: the problem it solves, in the buyer's words
3. Specs as a scannable list, exact numbers and materials
4. "Not right for you if…" — two honest disqualifiers
5. Care, sizing or setup — whatever causes returns

Rules:
- Every claim must map to a stated feature. No "premium quality", no "perfect for any occasion".
- Numbers over adjectives: "250 g" not "lightweight"
- Answer the three questions a buyer would otherwise have to message you about""",
    },
    {
        "title": "Title and Keyword Set",
        "description": "Search terms buyers actually type, worked into a readable title",
        "difficulty": "intermediate",
        "content": """Build the search terms for {{product}} on {{marketplace}}.

What it is: {{product_features}}
Buyer: {{target_buyer}}
Terms I already know: {{keywords}}

Produce:
1. 15 search phrases a buyer would type, grouped: problem-led, product-led, occasion-led
2. Which of those are too broad to compete on, marked
3. Three title variants that read as sentences, not keyword lists
4. The terms that belong in tags but not in the title

Rules:
- Buyer language, not industry language ("shirt that doesn't smell", not "antimicrobial textile")
- No keyword stuffing — a title a human cannot read loses the click even when it ranks
- Mark any term you are guessing at, so it gets checked against real search data""",
    },
    {
        "title": "Photo Shot List",
        "description": "The images that remove doubt, in order",
        "difficulty": "beginner",
        "content": """Plan the photo set for {{product}} on {{marketplace}}.

Features: {{product_features}}
Buyer's doubt: {{customer_problem}}

Produce the shot list in order of importance, each with:
- What is in frame
- Which specific doubt it removes
- Props, scale reference or background needed

Rules:
- First image must be understandable as a 200-px thumbnail
- At least one shot showing true scale next to a known object
- At least one showing the flaw-prone detail honestly (seam, joint, texture)
- Name the shot most sellers skip and lose sales over""",
    },
    {
        "title": "Answer a Product Question",
        "description": "Public Q&A reply that sells to everyone reading it",
        "difficulty": "beginner",
        "content": """Answer this public question about {{product}}.

Question: {{customer_message}}
Truth: {{product_features}}

Rules:
- Direct answer first, then the detail
- If the answer is no, say no and add what the product does instead
- Write it for the 100 people who will read it later, not only the asker
- Never overstate to close one sale — that comes back as a return and a review
- Under 80 words""",
    },
    {
        "title": "Reply to a Bad Review",
        "description": "A public answer that reassures future buyers",
        "difficulty": "advanced",
        "content": """Reply publicly to this review of {{product}}.

Review: {{review_text}}
What actually happened: {{context}}
What I can offer: {{resolution}}

Rules:
- The audience is future buyers, not the reviewer. Write so a stranger reads it and trusts you more.
- Concede everything that is true, immediately and without qualification
- Correct factual errors once, calmly, without "as stated in the listing"
- Offer the fix concretely, then move the rest to private contact
- Never argue, never mention their tone, never ask for the review to be changed
- Under 90 words""",
    },
    {
        "title": "Reduce Returns From a Reason",
        "description": "Turn a return reason into listing and product changes",
        "difficulty": "intermediate",
        "content": """Returns are coming back with this reason: {{return_reason}}

Product: {{product_features}}
Current listing says: {{text}}

Produce:
1. Which expectation the listing sets that the product does not meet
2. Three listing changes that fix it — exact replacement wording
3. One photo or measurement that removes the doubt before purchase
4. The product change worth making if returns continue
5. What this will cost in conversion — be honest, clearer listings sell to fewer but keep more

Rules:
- Do not solve a listing problem with a policy change
- Every change must be verifiable against the actual product""",
    },
    {
        "title": "Bundle and Pricing Options",
        "description": "Structure offers so the middle one is the obvious choice",
        "difficulty": "intermediate",
        "content": """Design offer options for {{product}} at {{price}}.

What buyers pair it with: {{context}}
Buyer: {{target_buyer}}

Produce:
1. Three options with what is in each and what each costs
2. Which one you want most people to pick, and what makes it the obvious pick
3. The wording that presents them without manipulation
4. What NOT to bundle, and why

Rules:
- Each option must be genuinely useful alone. A deliberately bad option to steer choice is a trick, and buyers feel it.
- No fake anchoring, no crossed-out prices that never applied""",
    },
    {
        "title": "Restock or Discontinue Message",
        "description": "Tell waiting customers the truth about availability",
        "difficulty": "beginner",
        "content": """Write the availability message for {{product}}.

Situation: {{context}}
Expected date: {{deadline}}

Rules:
- State the actual status in the first sentence: back on a date, delayed, or gone for good
- Give a date only if you can hold it. "Unknown" is better than a date that slips.
- If discontinued: say why in one line and name the nearest alternative, even a competitor's
- One way to be notified, no account required
- Under 70 words""",
    },
    {
        "title": "Shop Announcement or About Text",
        "description": "The seller story, without the artisan clichés",
        "difficulty": "beginner",
        "content": """Write the about text for a shop selling {{product}} on {{marketplace}}.

Who I am: {{context}}
What is actually different about how I make/source it: {{value_proposition}}

Rules:
- No "passion", no "journey", no "we believe that…", no origin story about a grandmother unless it is true and load-bearing
- Lead with what a buyer gets from you buying here rather than elsewhere
- One concrete detail about production or sourcing that a mass seller could not claim
- First person, plain
- Under 130 words""",
    },
    {
        "title": "Turn Reviews Into Copy",
        "description": "Mine what buyers actually say and put it in the listing",
        "difficulty": "intermediate",
        "content": """Read these reviews of {{product}} and rewrite my copy from them.

Reviews: {{input}}
Current copy: {{text}}

Produce:
1. The words buyers repeatedly use — their vocabulary, not mine
2. The benefit they name that my copy does not mention
3. The doubt that appears before purchase, taken from reviews that mention hesitation
4. A rewritten opening paragraph built from their language
5. What buyers value that I should stop calling a minor detail

Rules:
- Quote them. Do not paraphrase into marketing voice.
- Distinguish what one person said from what many said""",
    },
    {
        "title": "Shipping and Policy Text",
        "description": "Policies that prevent disputes instead of winning them",
        "difficulty": "beginner",
        "content": """Write the shipping and returns text for {{marketplace}}.

Reality: {{context}}
Constraints: {{constraints}}

Structure:
1. Dispatch time and delivery estimate, separately — buyers confuse them
2. What happens if it is late or lost, stated before they have to ask
3. Returns: window, condition, who pays postage
4. The one exception that causes most disputes, spelled out

Rules:
- Plain sentences, no legal register
- Never promise a carrier's delivery time as your own
- Any rule that would feel unfair when quoted back to you gets rewritten""",
    },
    {
        "title": "Launch Post for a New Product",
        "description": "Announce a product to people who already follow you",
        "difficulty": "beginner",
        "content": """Announce {{product}} to existing customers on {{channel}}.

What is new: {{product_features}}
Who it is for: {{target_buyer}}
Price: {{price}}

Rules:
- First line says what it is and who it is for — no teaser, no "something exciting is coming"
- One reason it exists: the problem that made you make it
- Price stated. Hiding it costs more clicks than it saves.
- One link, one action
- No countdown urgency unless the deadline is real
- Under 90 words""",
    },
]
