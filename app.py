import streamlit as st
import random

st.set_page_config(page_title="Kindness Quest", page_icon="🌟", layout="centered")

QUESTIONS = [
    {
        "scenario": "Your friend drops all their books on the floor. What should you do?",
        "options": [
            "Laugh because it looks funny",
            "Help pick up the books and ask if they are okay",
            "Walk away quickly"
        ],
        "answer": "Help pick up the books and ask if they are okay",
        "explanation": "Helping shows empathy because you notice someone needs support."
    },
    {
        "scenario": "Someone gives you a gift you do not really like. What should you say?",
        "options": [
            "Thank you for thinking of me",
            "I do not want this",
            "This is boring"
        ],
        "answer": "Thank you for thinking of me",
        "explanation": "Gratitude means appreciating the person's kindness, even if the gift is not perfect."
    },
    {
        "scenario": "A classmate answers wrongly in class. What is respectful?",
        "options": [
            "Giggle softly",
            "Say, 'That was easy!'",
            "Stay kind and let them try again"
        ],
        "answer": "Stay kind and let them try again",
        "explanation": "Respect means not embarrassing others when they make mistakes."
    },
    {
        "scenario": "Your parent cooked dinner after a tiring day. What can you do?",
        "options": [
            "Complain about the food",
            "Say thank you and help clear the table",
            "Leave the plates for someone else"
        ],
        "answer": "Say thank you and help clear the table",
        "explanation": "Showing gratitude can be through words and helpful actions."
    },
    {
        "scenario": "A new student is sitting alone during recess. What should you do?",
        "options": [
            "Invite them to join you",
            "Ignore them",
            "Tell others they have no friends"
        ],
        "answer": "Invite them to join you",
        "explanation": "Empathy means thinking about how someone else may feel."
    },
    {
        "scenario": "Your friend is talking, but you want to say something. What is respectful?",
        "options": [
            "Interrupt loudly",
            "Wait, listen, then speak",
            "Walk away"
        ],
        "answer": "Wait, listen, then speak",
        "explanation": "Respect means giving others a chance to speak."
    }
]

def reset_game():
    st.session_state.score = 0
    st.session_state.question_number = 0
    st.session_state.used_questions = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.selected = None

if "score" not in st.session_state:
    reset_game()

st.title("🌟 Kindness Quest")
st.subheader("Learn empathy, gratitude and respect through a mini game!")

total_questions = len(QUESTIONS)

st.progress(st.session_state.question_number / total_questions)
st.write(f"**Score:** {st.session_state.score} / {total_questions}")

if st.session_state.question_number >= total_questions:
    st.success("Game completed!")

    if st.session_state.score == total_questions:
        st.balloons()
        st.write("🏆 Amazing! You are a Kindness Champion!")
    elif st.session_state.score >= total_questions * 0.7:
        st.write("👏 Great job! You showed good understanding of empathy and respect.")
    else:
        st.write("💪 Good try! Play again to practise kind and respectful choices.")

    if st.button("Play Again"):
        reset_game()
        st.rerun()

else:
    current = st.session_state.used_questions[st.session_state.question_number]

    st.markdown("### Scenario")
    st.info(current["scenario"])

    choice = st.radio(
        "What is the best choice?",
        current["options"],
        index=None,
        key=f"question_{st.session_state.question_number}"
    )

    if st.button("Submit Answer", disabled=st.session_state.answered or choice is None):
        st.session_state.answered = True
        st.session_state.selected = choice

        if choice == current["answer"]:
            st.session_state.score += 1
            st.session_state.feedback = "✅ Correct! " + current["explanation"]
        else:
            st.session_state.feedback = (
                "❌ Not quite. The better answer is: "
                + current["answer"]
                + ". "
                + current["explanation"]
            )
        st.rerun()

    if st.session_state.answered:
        if st.session_state.selected == current["answer"]:
            st.success(st.session_state.feedback)
        else:
            st.warning(st.session_state.feedback)

        if st.button("Next Question"):
            st.session_state.question_number += 1
            st.session_state.answered = False
            st.session_state.feedback = ""
            st.session_state.selected = None
            st.rerun()

st.divider()
st.caption("Kindness tip: Respect is shown through words, actions and listening.")
