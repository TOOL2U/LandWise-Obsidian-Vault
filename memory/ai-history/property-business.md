# Property Management Business Knowledge

> Source: Claude AI conversation history export (April 2025 – April 2026)
> Last updated: 2026-04-07

## Business Model — Sia Moon Property Management

Shaun is building an island-wide property management services business for rental properties on a Thai island (Koh Phangan / Koh Samui area).

### Core Services

- Cleaning services (turnover and deep clean)
- Emergency check-ins for guests
- Pool cleaning and maintenance
- General maintenance
- Repair works: electrical, plumbing, and other trades

### Why This Model Works

- Islands create natural barriers to competition — defined, contained market
- Tourist-heavy location with consistent demand for vacation rental services
- Bundled service approach is smart — property owners prefer a single provider
- Premium positioning for luxury villas (not budget)

### Brand — Sia Moon Property Management

- Company: Sia Moon Co., Ltd. (registered Thai company)
- Brand goals: professional, trustworthy, modern, memorable
- Staff uniforms designed for tropical Southeast Asia environment
- Logo: minimalist, Thai wooden house on paradise island theme
- Has explored sustainability and wellness branding elements

### Property Details

- Manages Thai wooden houses and luxury villas
- Properties located on paradise Thai island
- One property involved in a construction/rebuild project (original house design seen in Chiang Mai, rebuilt on site)
- Construction considerations: termite prevention critical — all wooden formwork around pillars must be removed, no wood debris under house

### Booking System Architecture

- Bookings come through Booking.com
- Booking.com sends confirmation email to Gmail
- Gmail Watch (via Make.com) monitors for new booking emails
- Webhook triggers automated processing in the webapp
- System includes: check email → parse booking details → update database → send confirmation → assign tasks
- Sign-up and onboarding flows also automated via Make.com webhooks

### Lease Situation

- 10-year commercial lease agreement in Koh Phangan, Surat Thani
- Lessor: Mrs. Soljit Abe (via attorney Miss Pongsupa Chomin)
- Lessee: Sia Moon Co., Ltd.
- Key terms negotiated: no security deposit, free water from deep well, subletting allowed under company licences
- Contract reviewed by top Thai law firm
- Important: contract must be fair for Thai Land Office and Thai courts, not just protective of lessee

### Pipeline (as of early 2026)

- Phase: Pre-launch
- Goal: onboard first 3 paying clients
- Known leads: Denis, Philémon, Bob (mostly unqualified at the time)
- Workflow: intake → qualification → quoting → approval → send
