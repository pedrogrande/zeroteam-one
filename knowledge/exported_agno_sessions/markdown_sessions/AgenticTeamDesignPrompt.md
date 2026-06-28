<!-- @format -->

I have had a productive week developing a prototype of the Future's Edge platform using a team of AI agents in VSCode and have had a lot of learnings.

1. The 6-dimension ontology framework has lived up to its promise
2. Agents can improve themselves by conducting retrospectives and learning from successes and failures.
3. Having a meta agent that reviews retros and upgrades agents (tools, instructions etc) increases performance
4. The low cost and speed of agents compared to humans means it is trivial to have extra agents in the workflow to maintain quality and performance that wouldn't be feasible in human teams or workflows.
5. The agents are great at documenting their work and objectively critiquing their own work as well as other agents' works.
6. Agents don't always operate within the set rules or roles assigned to them
7. The amount of documentation produced quickly becomes a context overhead that could be better managed with a dedicated documentation agent that summarises, organizes and creates 'cheat sheets' for faster access by the relevant agents.
8. The free models available in VSCode were not good at any of the agentic work I tried. Claude Sonnet 4.5 was very good. However I ran out of credits. I will try some other premium models like Gemini to see if they can perform as well as Claude.
9. The advisor, meta and doc agents were good at recognising and defining 'gold standard' output and creating patterns or other knowledge sharing docs. There is no easy way to see which documents have been read or found useful by the agents.
10. Giving a developer agent a full story to build as a vertical slice was effective - but this is where I want to experiment with decomposition into tasks, and agents with less tools or context to care about to see if this can be more efficient with token usage and shorten development time at equal or higher quality.

Let's take these learnings and the valuable information in the thread to design a new team and workflow.

I would like us to design this to be a starter template that can be used on any software project - all the user needs to do is add the project context and an agent can update the team and workflow to suit.

For now, start with what context the user should provide for the agent team.
