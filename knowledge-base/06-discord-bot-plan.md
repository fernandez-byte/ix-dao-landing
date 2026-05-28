# IX DAO Discord Bot — Plan

**Status:** Planned, not yet set up
**Server:** https://discord.gg/pmMjc6Mnbm

---

## A. Auto Post

| Feature | Example |
|---|---|
| Scheduled announcements | "IX DAO Jobs available this week" every Monday |
| New Job alerts | Auto-post when a new Job goes live |
| Event reminders | Auto-post INFAXIA events 24hrs before |
| LP program updates | Auto-announce when LP program has changes |

---

## B. Auto Reply

| Trigger | Response |
|---|---|
| !jobs | List of available Jobs + links |
| !lp | IX DAO LP info + LP page link |
| !support | Direct to dao@infaxia.io |
| !rewards | How USDT rewards work |
| Keyword: "bug" | Direct to Bug Hunting Job |
| Keyword: "how to join" | Onboarding steps for new members |

---

## C. Member Management

| Feature | Details |
|---|---|
| Welcome message | Auto-greet new members with onboarding guide |
| Role assignment | Auto-assign IX DAO role after verification |
| Join logging | Log new members — name, date, referred from |

---

## D. IX Free Points Commands

| Command | Who | Function |
|---|---|---|
| !mypoints | Any IX DAO member | Shows their own IX FP balance |
| !checkpoints @username | Admins only | Shows IX FP balance of any member |

Data source: Google Sheet, updated every 3 hours

---

## E. Insights & Monitoring

| Insight | How |
|---|---|
| Active hours | Track when most messages are sent |
| Hot topics | Detect frequently mentioned keywords |
| Sentiment | Positive/negative reactions to announcements |
| Job interest | Track which Jobs get most questions |
| Member growth | Daily new member count |

---

## F. Reports (auto-sent to Paul)

| Report | Frequency | Delivery |
|---|---|---|
| Community activity summary | Daily | Telegram |
| New member count | Weekly | Telegram |
| Top questions asked | Weekly | Telegram |
| Sentiment report | Weekly | Email |

---

## Setup Requirements

1. Create Discord bot at Discord Developer Portal → get bot token
2. Invite bot to IX DAO server
3. Deploy bot script on DigitalOcean server (143.198.222.228)
4. Connect bot to Google Sheet via Sheets API for IX FP balance queries
