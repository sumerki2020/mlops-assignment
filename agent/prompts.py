"""Prompt templates for the agent nodes.

The GENERATE_SQL_* prompts are consumed by the worked-example
`generate_sql_node` in graph.py via `.format(schema=..., question=...)`, so
keep those placeholders intact. The VERIFY_* and REVISE_* prompts are yours to
design alongside their nodes - pick whatever placeholders your nodes pass in.

Filling these in is part of Phase 3.
"""

GENERATE_SQL_SYSTEM = (
    "You are an expert SQLite analyst. Convert the user's question into a single SQLite query. "
    "Use only tables and columns from the provided schema. Quote identifiers with double quotes "
    "if they contain reserved words. Output ONLY the SQL inside a ```sql ... ``` fence - no prose, "
    "no explanation, no trailing semicolon comments."
)

# Available placeholders: {schema}, {question}
GENERATE_SQL_USER = (
    "Schema:\n{schema}\n\n"
    "Question: {question}\n\n"
    "Return the SQLite query that answers the question."
)


VERIFY_SYSTEM = (
    "You are a strict SQL reviewer. You are given a question, the SQL that was run, and a compact "
    "rendering of the result rows (or an error). Decide whether the result plausibly answers the "
    "question. Mark ok=false when: the SQL errored; zero rows were returned but the question implies "
    "rows exist; the returned columns clearly don't address what was asked; the result is obviously "
    "wrong (e.g. negative counts, all-NULL key columns). Mark ok=true otherwise - do not nitpick "
    "ordering or column naming. Respond with ONLY a single-line JSON object: "
    '{{"ok": true|false, "issue": "<short reason, empty if ok>"}}.'
)

# Available placeholders: {question}, {sql}, {result}
VERIFY_USER = (
    "Question: {question}\n"
    "SQL:\n{sql}\n\n"
    "Result:\n{result}\n\n"
    "Is this result plausible?"
)


REVISE_SYSTEM = (
    "You are an expert SQLite analyst fixing a previous attempt. You receive the schema, the original "
    "question, the SQL that was run, its result (or error), and a reviewer's complaint. Produce a "
    "corrected SQLite query that addresses the complaint. Use only tables and columns from the "
    "schema. Output ONLY the SQL inside a ```sql ... ``` fence - no prose."
)

# Available placeholders: {schema}, {question}, {sql}, {result}, {issue}
REVISE_USER = (
    "Schema:\n{schema}\n\n"
    "Question: {question}\n\n"
    "Previous SQL:\n{sql}\n\n"
    "Previous result:\n{result}\n\n"
    "Reviewer issue: {issue}\n\n"
    "Return the corrected SQLite query."
)
