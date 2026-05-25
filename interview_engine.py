import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm():
    from dotenv import load_dotenv
    load_dotenv(override=True)
    api_key = os.getenv("GROQ_API_KEY")
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=api_key,
        temperature=0.7
    )
def generate_questions(role, num_questions=5):
    """Generate interview questions for a given role."""
    llm = get_llm()
    prompt = f"""Generate exactly {num_questions} interview questions for a {role} position.
Mix of technical and behavioral questions.
Format: Return ONLY a numbered list. No explanations.
Example:
1. Question here
2. Question here"""

    response = llm.invoke(prompt)
    lines = response.content.strip().split('\n')
    questions = []
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit():
            question = line.split('.', 1)[-1].strip()
            if question:
                questions.append(question)
    return questions[:num_questions]

def get_feedback(role, question, answer):
    """Get detailed feedback on an interview answer."""
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert interviewer giving feedback on interview answers.
Be specific, constructive, and encouraging.
Always structure your feedback exactly like this:

**Score: X/10**

**What you did well:**
- Point 1
- Point 2

**What to improve:**
- Point 1
- Point 2

**Ideal answer would include:**
- Key point 1
- Key point 2"""),
        ("human", f"""Role: {role}
Question: {question}
Candidate's Answer: {answer}

Give detailed feedback on this answer.""")
    ])
    chain = prompt | llm
    response = chain.invoke({})
    return response.content

def get_final_summary(role, qa_pairs):
    """Generate overall interview performance summary."""
    llm = get_llm()
    qa_text = ""
    for i, (q, a) in enumerate(qa_pairs, 1):
        qa_text += f"Q{i}: {q}\nA{i}: {a}\n\n"

    prompt = f"""You interviewed a candidate for {role} role.
Here are all their answers:
{qa_text}

Give a final interview summary with:
1. Overall Score (X/10)
2. Top 3 Strengths
3. Top 3 Areas to Improve
4. Would you recommend them? Why?
5. One key tip for their next interview

Be honest but encouraging."""

    response = llm.invoke(prompt)
    return response.content