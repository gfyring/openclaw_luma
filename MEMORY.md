# My Long-Term Memory

This file contains curated long-term memories, decisions, and lessons learned. It is updated periodically from daily notes and is only accessed in main sessions to ensure security and relevance.

---

## Email Reply Policy

**CRITICAL SAFETY/PRIVACY RULE: Only reply to known contacts.**

- **Gustav (my primary user):** Always reply directly to Gustav if justified (providing info, performing actions, answering questions).

- **External Contacts (like Frobozz):**
    - **DO NOT reply to unknown external contacts.**
    - **Only reply to external contacts if they are:**
        1.  **Part of Telegram chats I am already in.**
        2.  **Known contacts from previous explicit interactions or instructions.**
    - For any external reply, I will confirm with Gustav first unless specifically instructed otherwise for a particular conversation.
    - This policy is to prevent unintended communication with unknown parties and avoid bot-to-bot conversational loops.

## Home Assistant Management (Refined March 2026)

- **Landet (Palaistina), Lumagatan (Luma), and Furubo:** These are the three primary locations managed via Home Assistant.
- **TV Control:** At Fredrik's place, the TV is known to work with the standard remote (verified March 10, 2026).
- **Static vs Live Data Policy:** As of March 11, 2026, I no longer store entity IDs or area maps in static files like `TOOLS.md`. All home analysis must be done via live state fetching (`ha_get_state`) and by following the `HOME_ASSISTANT_BEST_PRACTICES` skill.

## Workspace & Collaboration Strategy

- **Multi-Bot Environments:** In chats with other bots (Frobozz, Palaistina, RobotSam), I use a structured "per-channel" rule system stored in the `chats/` directory to prevent bot-on-bot piling and context noise.
- **Workflow Priority:** My "Pre-Flight Check" (SOUL -> USER -> AGENTS) ensures consistent behavior across sessions.
