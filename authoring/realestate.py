PACK = {
    "id": "real-estate",
    "name": "Real Estate",
    "description": "Listings, viewings, offers and owner communication — written to attract the right buyer rather than every buyer.",
    "category": "business",
    "created": "2026-08-12",
    "tags": ["real-estate", "property", "sales", "listings"],
}

PROMPTS = [
    {
        "title": "Property Listing",
        "description": "A listing that sells the life in the flat, with the facts intact",
        "difficulty": "beginner",
        "content": """Write a listing for a {{property_type}} in {{location}}.

Features and condition: {{property_features}}
Who it suits: {{target_buyer}}
Price: {{asking_price}}

Structure:
1. Headline — type, size, area, the one distinguishing feature
2. Opening: what living here is actually like on a normal Tuesday
3. The rooms, in the order someone walks through them
4. Condition and what needs doing, stated plainly
5. Area: transport, schools, shops — with real distances
6. Price and what is included

Rules:
- Every superlative must be replaced by the fact behind it: not "bright", but "south-facing, windows on two sides"
- Name the obvious drawback and frame it honestly. Buyers find it at the viewing anyway; finding it themselves costs you trust.
- No "must be seen to be appreciated", no "rare opportunity\"""",
    },
    {
        "title": "Listing Headline Variants",
        "description": "Five headlines for the same property, aimed at different buyers",
        "difficulty": "beginner",
        "content": """Write headlines for a {{property_type}} in {{location}} at {{asking_price}}.

Features: {{property_features}}

Give 5 variants, each aimed at a different buyer: first-timers, families, downsizers, investors, renovators.

For each: who it targets, and which feature it leads with.

Then: which variant fits {{target_buyer}} best, and why the others would attract viewings that waste everyone's time.

Rules:
- Under 80 characters each
- Type, size and area must appear in every variant
- No exclamation marks""",
    },
    {
        "title": "Viewing Preparation Brief",
        "description": "What to say, show and prepare before people arrive",
        "difficulty": "intermediate",
        "content": """Prepare a viewing for a {{property_type}} in {{location}}.

Condition: {{property_features}}
Buyer type: {{target_buyer}}

Produce:
1. The route through the property, in order, and why that order
2. The three questions this buyer type always asks, with the honest answer to each
3. The weak point they will notice, and the truthful framing prepared in advance
4. What to have ready on paper: costs, floor plan, energy certificate, building minutes
5. The one question to ask them that reveals whether they are serious

Rules:
- Never open with the worst room, never end on it either
- Prepare answers you can defend if checked in the documents""",
    },
    {
        "title": "Follow-Up After a Viewing",
        "description": "Short message that moves a real buyer forward",
        "difficulty": "beginner",
        "content": """Write a follow-up to someone who viewed the {{property_type}} in {{location}}.

What they reacted to: {{context}}
Next step I want: {{goal}}

Rules:
- Reference one specific thing from the viewing, so it is clearly not a template
- Answer any question left open at the viewing, or say when you will
- One clear next step with a date
- No pressure about other interested parties unless it is true and verifiable
- Under 90 words""",
    },
    {
        "title": "Handle a Price Objection",
        "description": "Defend an asking price with evidence, or concede",
        "difficulty": "advanced",
        "content": """A buyer says the price is too high for the {{property_type}} in {{location}}.

Their argument: {{objection}}
What supports the price: {{context}}
Asking: {{asking_price}}

Produce:
1. Which part of their argument is correct — say it first
2. The evidence supporting the price: comparables, condition, what is included
3. Where the price is genuinely negotiable and where it is not
4. The counter-offer worth making, and the number below which walking away is right
5. What to concede instead of price: timing, fixtures, repairs

Rules:
- No comparable figures invented. If you do not have market data, say which data would settle it.
- Never defend a price with "the owner needs this much\"""",
    },
    {
        "title": "Owner Update During a Slow Sale",
        "description": "Tell the seller the truth about why it isn't moving",
        "difficulty": "advanced",
        "content": """Update the owner of a {{property_type}} in {{location}} that has not sold.

Activity so far: {{context}}
My assessment: {{issue}}

Structure:
1. The numbers: enquiries, viewings, offers — plain figures
2. What buyers actually say, quoted
3. The cause as I see it: price, presentation, or market — pick one and justify it
4. The two options with what each costs and what each is likely to achieve
5. My recommendation and the decision I need from them

Rules:
- Do not blame "the market" without the figures showing it
- If the price is the problem, say the number
- No optimism that the evidence does not support""",
    },
    {
        "title": "Offer Presentation to the Seller",
        "description": "Present an offer with everything that matters, not just the number",
        "difficulty": "intermediate",
        "content": """Present this offer on the {{property_type}} in {{location}}.

Offer: {{context}}
Asking: {{asking_price}}

Structure:
1. The number and how it compares to asking
2. The buyer: financing status, chain, proof of funds
3. Timing and conditions attached
4. Strength assessment — how likely this completes, and what could break it
5. The three responses available: accept, counter at X, or wait, each with its risk

Rules:
- A lower offer that completes beats a higher one that collapses. Say so with the evidence.
- Never present a number without its conditions
- No recommendation without naming what it costs the seller if you are wrong""",
    },
    {
        "title": "Valuation Explanation",
        "description": "Explain a number to an owner who expected more",
        "difficulty": "advanced",
        "content": """Explain the valuation of a {{property_type}} in {{location}} to its owner.

Features: {{property_features}}
My figure: {{asking_price}}
What they expected: {{context}}

Structure:
1. The figure and the range around it
2. What drives it up, itemised
3. What drives it down, itemised — including what they have paid for that the market does not reward
4. The comparables and how they differ from this property
5. What a higher asking price would actually cost them in time on market

Rules:
- Separate what the market pays from what the property is worth to them personally, explicitly and kindly
- Every adjustment gets a reason and a rough figure
- Never quote a number you would revise after the first two weeks""",
    },
    {
        "title": "Rental Ad and Tenant Criteria",
        "description": "Advertise a rental and state the criteria openly",
        "difficulty": "beginner",
        "content": """Write a rental listing for a {{property_type}} in {{location}}.

Features: {{property_features}}
Rent and costs: {{price}}
Requirements: {{must_haves}}

Structure:
1. The flat: size, rooms, floor, condition
2. Total monthly cost broken down — rent, service charges, heating, deposit
3. Available from, minimum term
4. What applicants need to provide, listed
5. How viewings work

Rules:
- Every cost stated. Hidden charges produce cancellations, not tenants.
- Requirements must be lawful and applied to everyone; no criteria that single out protected characteristics
- No "no DSS"-style exclusions or anything equivalent in your jurisdiction
- Plain, factual, no lifestyle prose""",
    },
    {
        "title": "Neighbourhood Description",
        "description": "Describe the area truthfully, with distances",
        "difficulty": "beginner",
        "content": """Describe {{location}} for a listing aimed at {{target_buyer}}.

What I know: {{context}}

Structure:
1. What the street itself is like — noise, traffic, parking
2. Daily infrastructure with walking times: shops, doctor, school, transport
3. What the area is good at
4. What it is not good at — one honest sentence
5. What is changing: construction, new lines, development

Rules:
- Times and distances, not adjectives. "7 minutes to the S-Bahn", not "excellent connections".
- Mark anything you have not verified so it gets checked
- No claims about future value""",
    },
    {
        "title": "Exposé Checklist",
        "description": "Everything the documentation must contain before going live",
        "difficulty": "intermediate",
        "content": """Build the pre-listing checklist for a {{property_type}} in {{location}}.

What I have: {{context}}

Produce:
1. Documents required before publication, each with who provides it and typical lead time
2. Measurements and figures that must be verified, not estimated
3. Photos required, in shooting order
4. What must be corrected before photos are taken
5. The three items most often missing that delay a sale by weeks

Rules:
- Mark anything with legal disclosure consequences in the relevant jurisdiction as blocking
- Do not state a legal requirement as fact for a country you were not told about — flag it as "verify locally\"""",
    },
    {
        "title": "Reply to a Lowball Enquiry",
        "description": "Answer an unrealistic offer without ending the conversation",
        "difficulty": "intermediate",
        "content": """Someone offered far below asking on the {{property_type}} in {{location}}.

Their offer and reasoning: {{objection}}
Asking: {{asking_price}}

Rules:
- Thank them once, briefly, then be concrete
- Ask what led them to that figure — sometimes they know something you do not
- State plainly whether it is in a range worth discussing
- If it is not, say so and leave a specific door open ("at X we would talk")
- No offence, no lecture about the market
- Under 100 words""",
    },
]
