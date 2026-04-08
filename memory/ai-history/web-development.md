# Web Development History & Projects

> Source: Claude AI conversation history export (April 2025 – April 2026)
> Last updated: 2026-04-07

## Tech Stack

- **Frontend:** React, Vite, TypeScript, Tailwind CSS, Remix
- **Backend:** Node.js, Supabase
- **Hosting:** GitHub (org: TOOL2U)
- **Automation:** Make.com (webhooks)
- **IDE:** VS Code / Cursor
- **Browser:** Chrome Canary (for dev), used DevTools Workspaces for live editing
- **OS:** Mac Studio, macOS 15.3.2

## GitHub Repositories

### TOOL2U/Marketplace

- Service marketplace web app called "MAN2U"
- Built with React + Remix, TypeScript, Tailwind CSS, React Icons
- Had a developer page added for testing bookings and navigation
- Developer page includes booking tests, site navigation tools, in same style as rest of app

### TOOL2U/SIA-MOON-WEBSITE

- Website for Sia Moon Property Management
- Reviewed for errors, structure, organization

### TOOL2U/Property-Management---Claude

- Comprehensive villa property management web application
- Uses Supabase for backend integration
- Checked for correct Supabase connection and integration

## Key Technical Topics Explored

### Combining React Apps

- Explored merging two React/Vite/Node repos onto a single domain
- Options discussed: monorepo approach, micro-frontends, reverse proxy routing

### Chrome DevTools Workspaces

- Wanted live editing from Chrome DevTools to save directly to VS Code
- Set up workspace mapping for localhost:5173 (Vite dev server)
- On Mac, the option may be labelled differently — uses Sources panel → Filesystem

### Bank Account Integration

- Built a bookkeeping webapp and wanted bank account linking
- Explored Thai bank APIs (Bangkok Bank, Krungsri, Krungthai)
- Thai banks are slower on open banking vs Western markets
- Limited API access for personal accounts at these banks

### Booking Automation

- Integrated Booking.com → Gmail Watch → Make.com webhooks → webapp
- Automated sign-up confirmation and onboarding form flows
- Created flowcharts documenting the entire automation pipeline

### AI Business Automation

- Designed an AI automation system for full business control
- Back-office toggle button to enable/disable AI control
- AI can approve bookings, manage operations, handle communications
- Staged implementation approach planned
