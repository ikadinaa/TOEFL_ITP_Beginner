import streamlit as st

st.set_page_config(
    page_title="TOEFL ITP Beginner 1 Practice",
    page_icon="📘",
    layout="wide"
)

student_name = st.text_input(
    "Enter Your Full Name"
)

menu = st.sidebar.selectbox(
    "Choose Menu",
    [
        "🏠 Home",
        "📖 Introduction to TOEFL ITP",
        "🎧 Listening Comprehension",
        "📝 Structure and Written Expression",
        "📚 Reading Comprehension",
        "🏆 Leaderboard",
        "ℹ️ About"
    ]
) 


# HOME
if menu == "🏠 Home":
    st.title("🎓 TOEFL ITP Beginner 1 Learning App")

    st.markdown("---")

    st.subheader("Welcome!")

    st.write("""
This application is designed for beginner learners who want to understand
the basic concepts of TOEFL ITP. It provides simple learning materials,
practice activities, and quizzes to help users improve their English skills.
""")

    st.subheader("📚 Features")

    st.write("""
✅ Grammar Practice

✅ Vocabulary Builder

✅ Reading Practice

✅ Mini TOEFL Quiz
""")

    st.subheader("🎯 Learning Objectives")

    st.write("""
• Understand basic English grammar

• Learn common TOEFL vocabulary

• Improve reading comprehension skills

• Practice answering TOEFL-style questions

• Build confidence before taking higher-level TOEFL tests
""")

    st.markdown("---")

    st.success("Start your learning journey by selecting a menu from the sidebar.")
    

# INTRODUCTION
elif menu == "📖 Introduction to TOEFL ITP":
    st.header("📖 Introduction to TOEFL ITP")

    st.write("""
TOEFL ITP (Test of English as a Foreign Language Institutional Testing Program)
is an English proficiency test used by schools, universities, and institutions
to measure academic English skills.

The test evaluates a learner's ability to understand and use English in an
academic environment. TOEFL ITP is commonly used for placement tests,
graduation requirements, scholarship applications, and academic preparation.

This beginner application is designed for students who are new to TOEFL ITP.
The materials focus on basic grammar, vocabulary, reading comprehension, and
simple TOEFL-style questions to help learners build confidence before studying
more advanced TOEFL content.
""")

    st.subheader("📌 Main Sections of TOEFL ITP")

    st.write("""
1. Listening Comprehension
   - Understanding short conversations and talks.

2. Structure and Written Expression
   - Understanding English grammar and sentence structure.

3. Reading Comprehension
   - Understanding written passages and answering questions.
""")

    st.subheader("🎯 Learning Goals")

    st.write("""
After using this application, learners should be able to:

• Recognize basic TOEFL question types.

• Improve fundamental grammar skills.

• Learn common English vocabulary.

• Develop basic reading comprehension skills.

• Prepare for higher-level TOEFL ITP practice.
""")
# LISTENING
elif menu == "🎧 Listening Comprehension":

    st.title("🎧 Listening Comprehension")

    package = st.selectbox(
        "Select Package",
        [
            "Package 1",
            "Package 2",
            "Package 3",
            "Package 4",
            "Package 5"
        ]
    )

    # ==========================
    # PACKAGE 1
    # ==========================
    if package == "Package 1":
        st.subheader("Audio Package 1")

        audio_file = open("audio/PACKAGE 1.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.markdown("---")

        answers = {}

        answers[1] = st.radio(
            "1. What is the main topic of the audio?",
            [
                "A family vacation",
                "The first snowfall of the season",
                "A trip to school",
                "Building a house"
            ],
            key="l1_1"
        )

        answers[2] = st.radio(
            "2. On what date did it snow?",
            [
                "November 16th",
                "November 20th",
                "November 26th",
                "December 26th"
            ],
            key="l1_2"
        )

        answers[3] = st.radio(
            "3. How long did it snow?",
            [
                "All day",
                "One hour",
                "Two days",
                "One week"
            ],
            key="l1_3"
        )

        answers[4] = st.radio(
            "4. Who is excited about the snow?",
            [
                "The mother",
                "The father",
                "The narrator and the sister",
                "The neighbors"
            ],
            key="l1_4"
        )

        answers[5] = st.radio(
            "5. Why does the mother not like the snow?",
            [
                "She is sick",
                "She must shovel the driveway",
                "She is busy working",
                "She is afraid of snow"
            ],
            key="l1_5"
        )

        answers[6] = st.radio(
            "6. What does the narrator put on before going outside?",
            [
                "Boots and scarf",
                "Hat and mittens",
                "Jacket and shoes",
                "Sweater and hat"
            ],
            key="l1_6"
        )

        answers[7] = st.radio(
            "7. Who puts on the narrator's scarf?",
            [
                "The narrator",
                "The sister",
                "The father",
                "The mother"
            ],
            key="l1_7"
        )

        answers[8] = st.radio(
            "8. What do the children make first?",
            [
                "A snow fort",
                "A snow angel",
                "A snowman",
                "A snow house"
            ],
            key="l1_8"
        )

        answers[9] = st.radio(
            "9. What does the mother do outside?",
            [
                "Makes a snowman",
                "Throws snowballs",
                "Shovels snow",
                "Drinks hot chocolate"
            ],
            key="l1_9"
        )

        answers[10] = st.radio(
            "10. What activity do the children do after making a snowman?",
            [
                "Go skating",
                "Make snow angels",
                "Build a tent",
                "Go home"
            ],
            key="l1_10"
        )

        answers[11] = st.radio(
            "11. What do the children throw?",
            [
                "Leaves",
                "Rocks",
                "Snowballs",
                "Sticks"
            ],
            key="l1_11"
        )

        answers[12] = st.radio(
            "12. What happens again later?",
            [
                "The wind starts",
                "The rain starts",
                "The snow starts",
                "The sun shines"
            ],
            key="l1_12"
        )

        answers[13] = st.radio(
            "13. Why do they go inside?",
            [
                "To eat dinner",
                "To watch television",
                "To drink hot chocolate",
                "To study"
            ],
            key="l1_13"
        )

        answers[14] = st.radio(
            "14. The word 'beautiful' is closest in meaning to:",
            [
                "Ugly",
                "Pretty",
                "Dirty",
                "Cold"
            ],
            key="l1_14"
        )

        answers[15] = st.radio(
            "15. What can we conclude about the children?",
            [
                "They enjoy playing in the snow.",
                "They dislike winter.",
                "They are afraid of snow.",
                "They want to stay indoors."
            ],
            key="l1_15"
        )

        answer_key = {
            1: "The first snowfall of the season",
            2: "November 26th",
            3: "All day",
            4: "The narrator and the sister",
            5: "She must shovel the driveway",
            6: "Hat and mittens",
            7: "The mother",
            8: "A snowman",
            9: "Shovels snow",
            10: "Make snow angels",
            11: "Snowballs",
            12: "The snow starts",
            13: "To drink hot chocolate",
            14: "Pretty",
            15: "They enjoy playing in the snow."
        }

        if st.button(
            "Submit Listening Package 1",
            key="submit_listening_package_1"
        ):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"🎉 Your Score: {score}/15")
            st.session_state["listening_p1"] = score
            st.write(f"📊 Percentage: {percentage:.0f}%")

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")

            st.subheader("Answer Explanation")

            explanations = {
                1: "The audio is about the first snowfall of the season.",
                2: "The snowfall happened on November 26th.",
                3: "The narrator says it snowed all day.",
                4: "The narrator and the sister are excited about the snow.",
                5: "The mother dislikes snow because she must shovel the driveway.",
                6: "The narrator wears a hat and mittens before going outside.",
                7: "The mother helps put on the narrator's scarf.",
                8: "The children make a snowman first.",
                9: "The mother shovels snow outside.",
                10: "After making a snowman, they make snow angels.",
                11: "The children throw snowballs.",
                12: "Later, the snow starts again.",
                13: "They go inside to drink hot chocolate.",
                14: "'Beautiful' means pretty.",
                15: "The children clearly enjoy playing in the snow."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")

    # ==========================
    # PACKAGE 2
    # ==========================
   
    elif package == "Package 2":

        st.subheader("Audio Package 2")

        audio_file = open("audio/PACKAGE 2.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.markdown("---")

        answers = {}

        answers[1] = st.radio(
            "1. What is the main topic of the audio?",
            [
                "Jessica's birthday",
                "Jessica's first day of kindergarten",
                "Jessica's family vacation",
                "Jessica's new house"
            ],
            key="l2_1"
        )

        answers[2] = st.radio(
            "2. Who walks Jessica to school?",
            [
                "Her teacher",
                "Her friends",
                "Her parents",
                "Her neighbors"
            ],
            key="l2_2"
        )

        answers[3] = st.radio(
            "3. Who walks Jessica to her classroom?",
            [
                "Her father",
                "Her teacher",
                "Her sister",
                "Her mother"
            ],
            key="l2_3"
        )

        answers[4] = st.radio(
            "4. What is Jessica's teacher's name?",
            [
                "Mr. Brown",
                "Mr. Parker",
                "Mr. Smith",
                "Mr. Jones"
            ],
            key="l2_4"
        )

        answers[5] = st.radio(
            "5. What time does the school bell ring?",
            [
                "8:15 a.m.",
                "8:30 a.m.",
                "8:45 a.m.",
                "9:00 a.m."
            ],
            key="l2_5"
        )

        answers[6] = st.radio(
            "6. What does Jessica do before her mother leaves?",
            [
                "Waves goodbye",
                "Hugs and kisses her mom",
                "Cries",
                "Eats breakfast"
            ],
            key="l2_6"
        )

        answers[7] = st.radio(
            "7. What happens at 9:00 a.m.?",
            [
                "Lunch begins",
                "Recess starts",
                "Jessica stands for the national anthem",
                "School ends"
            ],
            key="l2_7"
        )

        answers[8] = st.radio(
            "8. What do children say when Mr. Parker calls their names?",
            [
                "Hello",
                "Present",
                "Yes",
                "Here"
            ],
            key="l2_8"
        )

        answers[9] = st.radio(
            "9. What does Mr. Parker teach first?",
            [
                "Science and art",
                "Letters and numbers",
                "Music and sports",
                "Reading and writing"
            ],
            key="l2_9"
        )

        answers[10] = st.radio(
            "10. What time do students have recess?",
            [
                "10:00 a.m.",
                "10:15 a.m.",
                "10:30 a.m.",
                "11:15 a.m."
            ],
            key="l2_10"
        )

        answers[11] = st.radio(
            "11. What can students do during recess?",
            [
                "Study and read",
                "Play and eat",
                "Sleep and rest",
                "Draw and sing"
            ],
            key="l2_11"
        )

        answers[12] = st.radio(
            "12. Where do students go at 10:30 a.m.?",
            [
                "Library",
                "Music room",
                "Gym class",
                "Cafeteria"
            ],
            key="l2_12"
        )

        answers[13] = st.radio(
            "13. What does Mr. Parker tell students to do at 11:15 a.m.?",
            [
                "Stand up",
                "Go home",
                "Sit on the carpet",
                "Eat lunch"
            ],
            key="l2_13"
        )

        answers[14] = st.radio(
            "14. What two activities does Mr. Parker do before lunch?",
            [
                "Reads a story and teaches a song",
                "Gives a test and homework",
                "Plays games and exercises",
                "Shows a movie and sings"
            ],
            key="l2_14"
        )

        answers[15] = st.radio(
            "15. What happens when the lunch bell rings?",
            [
                "Recess begins",
                "Gym class starts",
                "Jessica's first day ends",
                "Students take a test"
            ],
            key="l2_15"
        )

        answer_key = {
            1: "Jessica's first day of kindergarten",
            2: "Her parents",
            3: "Her mother",
            4: "Mr. Parker",
            5: "8:45 a.m.",
            6: "Hugs and kisses her mom",
            7: "Jessica stands for the national anthem",
            8: "Here",
            9: "Letters and numbers",
            10: "10:15 a.m.",
            11: "Play and eat",
            12: "Gym class",
            13: "Sit on the carpet",
            14: "Reads a story and teaches a song",
            15: "Jessica's first day ends"
        }

        if st.button(
            "Submit Listening Package 2",
            key="submit_listening_package_2"
        ):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"🎉 Your Score: {score}/15")
            st.session_state["listening_p2"] = score
            st.write(f"📊 Percentage: {percentage:.0f}%")

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")

            st.subheader("Answer Explanation")

            explanations = {
                1: "The audio discusses Jessica's first day of kindergarten.",
                2: "Jessica is accompanied by her parents.",
                3: "Her mother walks her to the classroom.",
                4: "Her teacher's name is Mr. Parker.",
                5: "The school bell rings at 8:45 a.m.",
                6: "Jessica hugs and kisses her mother before she leaves.",
                7: "Students stand for the national anthem at 9:00 a.m.",
                8: "Students answer 'Here' during attendance.",
                9: "Mr. Parker teaches letters and numbers first.",
                10: "Recess starts at 10:15 a.m.",
                11: "Students can play and eat during recess.",
                12: "Students go to gym class at 10:30 a.m.",
                13: "Mr. Parker tells students to sit on the carpet.",
                14: "He reads a story and teaches a song.",
                15: "The lunch bell marks the end of Jessica's first morning."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")

    # ==========================
    # PACKAGE 3
    # ==========================
    elif package == "Package 3":

        st.subheader("Audio Package 3")

        audio_file = open("audio/PACKAGE 3.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.markdown("---")

        answers = {}

        answers[1] = st.radio(
            "1. What is the main topic of the audio?",
            [
                "A vegetable garden",
                "Anne's flower garden",
                "A public park",
                "A flower shop"
            ],
            key="l3_1"
        )

        answers[2] = st.radio(
            "2. What is the narrator's name?",
            [
                "Jessica",
                "Anna",
                "Anne",
                "Amanda"
            ],
            key="l3_2"
        )

        answers[3] = st.radio(
            "3. What does Anne love?",
            [
                "Trees",
                "Flowers",
                "Vegetables",
                "Birds"
            ],
            key="l3_3"
        )

        answers[4] = st.radio(
            "4. Where is her garden?",
            [
                "Behind her house",
                "Beside her house",
                "In front of her house",
                "Near a school"
            ],
            key="l3_4"
        )

        answers[5] = st.radio(
            "5. Who also has a garden?",
            [
                "Her sister",
                "Her friend",
                "Her teacher",
                "Her neighbor"
            ],
            key="l3_5"
        )

        answers[6] = st.radio(
            "6. What type of flower is mentioned first?",
            [
                "Tulips",
                "Petunias",
                "Roses",
                "Lilies"
            ],
            key="l3_6"
        )

        answers[7] = st.radio(
            "7. Which flower is NOT mentioned?",
            [
                "Roses",
                "Tulips",
                "Petunias",
                "Sunflowers"
            ],
            key="l3_7"
        )

        answers[8] = st.radio(
            "8. What color flowers does Anne plant?",
            [
                "Red",
                "Orange",
                "Blue",
                "All of the above"
            ],
            key="l3_8"
        )

        answers[9] = st.radio(
            "9. Which color is mentioned last?",
            [
                "Red",
                "Orange",
                "Blue",
                "Purple"
            ],
            key="l3_9"
        )

        answers[10] = st.radio(
            "10. What does Anne do to care for her garden?",
            [
                "Waters it every day",
                "Paints the flowers",
                "Builds fences",
                "Cuts trees"
            ],
            key="l3_10"
        )

        answers[11] = st.radio(
            "11. How often does she water the garden?",
            [
                "Once a week",
                "Twice a week",
                "Every day",
                "Every month"
            ],
            key="l3_11"
        )

        answers[12] = st.radio(
            "12. What does she remove from the garden?",
            [
                "Leaves",
                "Weeds",
                "Trees",
                "Stones"
            ],
            key="l3_12"
        )

        answers[13] = st.radio(
            "13. What insects does she kill?",
            [
                "Insects that eat her flowers",
                "All insects",
                "Mosquitoes only",
                "Ants only"
            ],
            key="l3_13"
        )

        answers[14] = st.radio(
            '14. The word "different" is closest in meaning to:',
            [
                "Same",
                "Various",
                "Small",
                "Beautiful"
            ],
            key="l3_14"
        )

        answers[15] = st.radio(
            "15. How does Anne feel about her garden?",
            [
                "She dislikes it.",
                "She ignores it.",
                "She loves it.",
                "She wants to sell it."
            ],
            key="l3_15"
        )

        answer_key = {
            1: "Anne's flower garden",
            2: "Anne",
            3: "Flowers",
            4: "In front of her house",
            5: "Her neighbor",
            6: "Roses",
            7: "Sunflowers",
            8: "All of the above",
            9: "Purple",
            10: "Waters it every day",
            11: "Every day",
            12: "Weeds",
            13: "Insects that eat her flowers",
            14: "Various",
            15: "She loves it."
        }

        if st.button(
            "Submit Listening Package 3",
            key="submit_listening_package_3"
        ):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"🎉 Your Score: {score}/15")
            st.session_state["listening_p3"] = score
            st.write(f"📊 Percentage: {percentage:.0f}%")

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")

            st.subheader("Answer Explanation")

            explanations = {
                1: "The audio is about Anne's flower garden.",
                2: "The narrator's name is Anne.",
                3: "Anne loves flowers.",
                4: "Her garden is in front of her house.",
                5: "Her neighbor also has a garden.",
                6: "Roses are mentioned first.",
                7: "Sunflowers are not mentioned.",
                8: "She plants red, orange, and blue flowers.",
                9: "Purple is mentioned last.",
                10: "She waters the garden every day.",
                11: "She waters it daily.",
                12: "She removes weeds.",
                13: "She kills insects that eat her flowers.",
                14: "Different means various.",
                15: "Anne loves her garden."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    # ==========================
    # PACKAGE 4
    # ==========================
    elif package == "Package 4":

        st.subheader("Audio Package 4")

        audio_file = open("audio/PACKAGE 4.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.markdown("---")

        answers = {}

        answers[1] = st.radio(
            "1. What is the main topic of the audio?",
            [
                "A camping trip",
                "A school day",
                "A family reunion",
                "A fishing contest"
            ],
            key="l4_1"
        )

        answers[2] = st.radio(
            "2. What family went camping?",
            [
                "Brown family",
                "Smith family",
                "Bright family",
                "Green family"
            ],
            key="l4_2"
        )

        answers[3] = st.radio(
            "3. Where did they go?",
            [
                "Blue River",
                "Silent Lake",
                "Green Forest",
                "Sunny Beach"
            ],
            key="l4_3"
        )

        answers[4] = st.radio(
            "4. What day did they leave?",
            [
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ],
            key="l4_4"
        )

        answers[5] = st.radio(
            "5. How many days did they camp?",
            [
                "One day",
                "Two days",
                "Three days",
                "Four days"
            ],
            key="l4_5"
        )

        answers[6] = st.radio(
            "6. What did they bring?",
            [
                "A big tent",
                "Food",
                "Insect repellent",
                "All of the above"
            ],
            key="l4_6"
        )

        answers[7] = st.radio(
            "7. What did they do on Friday night?",
            [
                "Went hiking",
                "Had a campfire",
                "Went swimming",
                "Went fishing"
            ],
            key="l4_7"
        )

        answers[8] = st.radio(
            "8. What food did they roast?",
            [
                "Corn",
                "Potatoes",
                "Marshmallows",
                "Fish"
            ],
            key="l4_8"
        )

        answers[9] = st.radio(
            "9. What did they sing?",
            [
                "School songs",
                "Campfire songs",
                "National songs",
                "Children's songs"
            ],
            key="l4_9"
        )

        answers[10] = st.radio(
            "10. Which activity did they do on Saturday?",
            [
                "Canoeing",
                "Fishing",
                "Swimming",
                "All of the above"
            ],
            key="l4_10"
        )

        answers[11] = st.radio(
            "11. What did they do on Sunday?",
            [
                "Hiking",
                "Swimming",
                "Canoeing",
                "Fishing"
            ],
            key="l4_11"
        )

        answers[12] = st.radio(
            "12. Which bird is mentioned?",
            [
                "Eagle",
                "Owl",
                "Blue jay",
                "Crow"
            ],
            key="l4_12"
        )

        answers[13] = st.radio(
            "13. Which animal did they see?",
            [
                "Bear",
                "Tiger",
                "Raccoon",
                "Deer"
            ],
            key="l4_13"
        )

        answers[14] = st.radio(
            "14. Which animal did they NOT see?",
            [
                "Raccoon",
                "Squirrel",
                "Blue jay",
                "Bear"
            ],
            key="l4_14"
        )

        answers[15] = st.radio(
            "15. What can we conclude about the trip?",
            [
                "It was boring.",
                "It was fun.",
                "It was difficult.",
                "It was short."
            ],
            key="l4_15"
        )

        answer_key = {
            1: "A camping trip",
            2: "Bright family",
            3: "Silent Lake",
            4: "Friday",
            5: "Three days",
            6: "All of the above",
            7: "Had a campfire",
            8: "Marshmallows",
            9: "Campfire songs",
            10: "All of the above",
            11: "Hiking",
            12: "Blue jay",
            13: "Raccoon",
            14: "Bear",
            15: "It was fun."
        }

        if st.button(
            "Submit Listening Package 4",
            key="submit_listening_package_4"
        ):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"🎉 Your Score: {score}/15")
            st.session_state["listening_p4"] = score
            st.write(f"📊 Percentage: {percentage:.0f}%")

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")

            st.subheader("Answer Explanation")

            explanations = {
                1: "The audio is about a camping trip.",
                2: "The Bright family went camping.",
                3: "They camped at Silent Lake.",
                4: "They left on Friday.",
                5: "They camped for three days.",
                6: "They brought a tent, food, and insect repellent.",
                7: "They had a campfire on Friday night.",
                8: "They roasted marshmallows.",
                9: "They sang campfire songs.",
                10: "They went canoeing, fishing, and swimming.",
                11: "They went hiking on Sunday.",
                12: "A blue jay is mentioned in the audio.",
                13: "They saw a raccoon.",
                14: "They did not see a bear.",
                15: "The trip was enjoyable and fun."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    # ==========================
    # PACKAGE 5
    # ==========================
  
    elif package == "Package 5":

        st.subheader("Audio Package 5")

        audio_file = open("audio/PACKAGE 5.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.markdown("---")

        answers = {}

        answers[1] = st.radio(
            "1. What is the main topic of the audio?",
            [
                "A school",
                "A house",
                "A garden",
                "A neighborhood"
            ],
            key="l5_1"
        )

        answers[2] = st.radio(
            "2. How many bedrooms does the house have?",
            [
                "One",
                "Two",
                "Three",
                "Four"
            ],
            key="l5_2"
        )

        answers[3] = st.radio(
            "3. Who sleeps in one bedroom?",
            [
                "The narrator and sister",
                "The grandparents",
                "The parents",
                "The guests"
            ],
            key="l5_3"
        )

        answers[4] = st.radio(
            "4. Who shares the other bedroom?",
            [
                "The parents",
                "The narrator and sister",
                "The cousins",
                "The grandparents"
            ],
            key="l5_4"
        )

        answers[5] = st.radio(
            "5. What room is used for cooking?",
            [
                "Living room",
                "Bathroom",
                "Basement",
                "Kitchen"
            ],
            key="l5_5"
        )

        answers[6] = st.radio(
            "6. What does the family do in the living room?",
            [
                "Eat dinner",
                "Watch television",
                "Study",
                "Sleep"
            ],
            key="l5_6"
        )

        answers[7] = st.radio(
            "7. How is the bathroom described?",
            [
                "Small",
                "Modern",
                "Big",
                "Old"
            ],
            key="l5_7"
        )

        answers[8] = st.radio(
            "8. What does the house have a lot of?",
            [
                "Windows",
                "Doors",
                "Closets",
                "Chairs"
            ],
            key="l5_8"
        )

        answers[9] = st.radio(
            "9. What is in the basement?",
            [
                "A bedroom",
                "A workshop",
                "A kitchen",
                "A garage"
            ],
            key="l5_9"
        )

        answers[10] = st.radio(
            "10. What does the father make?",
            [
                "Toys",
                "Metal tools",
                "Wood furniture",
                "Clothes"
            ],
            key="l5_10"
        )

        answers[11] = st.radio(
            "11. Does the house have a second floor?",
            [
                "Yes",
                "No",
                "Sometimes",
                "Not mentioned"
            ],
            key="l5_11"
        )

        answers[12] = st.radio(
            "12. What does the house have besides the basement?",
            [
                "Garage",
                "Barn",
                "Office",
                "Balcony"
            ],
            key="l5_12"
        )

        answers[13] = st.radio(
            "13. What kind of tree is in the backyard?",
            [
                "Apple tree",
                "Oak tree",
                "Maple tree",
                "Pine tree"
            ],
            key="l5_13"
        )

        answers[14] = st.radio(
            "14. What else is in the backyard?",
            [
                "Basketball court",
                "Swimming pool and vegetable garden",
                "Playground",
                "Flower shop"
            ],
            key="l5_14"
        )

        answers[15] = st.radio(
            "15. How does the family feel about their house?",
            [
                "They dislike it.",
                "They want to move.",
                "They like it.",
                "They are unsure."
            ],
            key="l5_15"
        )

        answer_key = {
            1: "A house",
            2: "Two",
            3: "The parents",
            4: "The narrator and sister",
            5: "Kitchen",
            6: "Watch television",
            7: "Big",
            8: "Closets",
            9: "A workshop",
            10: "Wood furniture",
            11: "No",
            12: "Garage",
            13: "Maple tree",
            14: "Swimming pool and vegetable garden",
            15: "They like it."
        }

        if st.button(
            "Submit Listening Package 5",
            key="submit_listening_package_5"
        ):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"🎉 Your Score: {score}/15")
            st.session_state["listening_p5"] = score
            st.write(f"📊 Percentage: {percentage:.0f}%")

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")

            st.subheader("Answer Explanation")

            explanations = {
                1: "The audio describes a house.",
                2: "The house has two bedrooms.",
                3: "The parents sleep in one bedroom.",
                4: "The narrator shares the other bedroom with a sister.",
                5: "The kitchen is used for cooking.",
                6: "The family watches television in the living room.",
                7: "The bathroom is described as big.",
                8: "The house has many closets.",
                9: "There is a workshop in the basement.",
                10: "The father makes wood furniture.",
                11: "The house does not have a second floor.",
                12: "The house also has a garage.",
                13: "There is a maple tree in the backyard.",
                14: "The backyard has a swimming pool and vegetable garden.",
                15: "The family likes their house."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    st.markdown("---")

    if st.button("Calculate Listening Final Score"):

        p1 = st.session_state.get("listening_p1", 0)
        p2 = st.session_state.get("listening_p2", 0)
        p3 = st.session_state.get("listening_p3", 0)
        p4 = st.session_state.get("listening_p4", 0)
        p5 = st.session_state.get("listening_p5", 0)

        total = p1 + p2 + p3 + p4 + p5

        percentage = (total / 75) * 100

        st.subheader("🎧 Listening Final Score")

        st.write(f"Package 1: {p1}/15")
        st.write(f"Package 2: {p2}/15")
        st.write(f"Package 3: {p3}/15")
        st.write(f"Package 4: {p4}/15")
        st.write(f"Package 5: {p5}/15")

        st.success(f"Total Score: {total}/75")
        st.session_state["listening_total"] = listening_score
        st.success(f"Percentage: {percentage:.0f}%")

        st.session_state["listening_total"] = total
# STRUCTURE AND WRITTEN EXPRESSION
elif menu == "📝 Structure and Written Expression":

    st.title("📝 Structure and Written Expression")

    package = st.selectbox(
        "Select Package",
        [
            "Package 1",
            "Package 2",
            "Package 3",
            "Package 4",
            "Package 5"
        ]
    )

    st.write("Selected:", package)

    st.progress(100)
    st.caption("Grammar Practice: 20 Questions")

    score = 0
    if package == "Package 1":

        answers = {}

        answers[1] = st.radio(
            "1. My brother _____ a student at the university.",
            ["am", "is", "are", "be"],
            key="s1"
        )

        answers[2] = st.radio(
            "2. Sarah _____ English every day.",
            ["study", "studies", "studying", "studied"],
            key="s2"
        )

        answers[3] = st.radio(
            "3. The students _____ in the classroom now.",
            ["is", "am", "are", "be"],
            key="s3"
        )

        answers[4] = st.radio(
            "4. _____ book is on the table.",
            ["A", "An", "The", "Some"],
            key="s4"
        )

        answers[5] = st.radio(
            "5. My father _____ to work by car.",
            ["go", "goes", "going", "gone"],
            key="s5"
        )

        answers[6] = st.radio(
            "6. We _____ football yesterday.",
            ["play", "plays", "played", "playing"],
            key="s6"
        )

        answers[7] = st.radio(
            "7. There _____ many books in the library.",
            ["is", "are", "was", "be"],
            key="s7"
        )

        answers[8] = st.radio(
            "8. She is _____ than her sister.",
            ["tall", "taller", "tallest", "more tall"],
            key="s8"
        )

        answers[9] = st.radio(
            "9. I need _____ umbrella because it is raining.",
            ["a", "an", "the", "some"],
            key="s9"
        )

        answers[10] = st.radio(
            "10. They _____ dinner at 7 p.m. every day.",
            ["eat", "eats", "eating", "ate"],
            key="s10"
        )

        answers[11] = st.radio(
            "11. The teacher _____ very kind.",
            ["am", "are", "is", "be"],
            key="s11"
        )

        answers[12] = st.radio(
            "12. We _____ in Palangka Raya last week.",
            ["are", "were", "is", "be"],
            key="s12"
        )

        answers[13] = st.radio(
            "13. John and Mike _____ best friends.",
            ["am", "is", "are", "was"],
            key="s13"
        )

        answers[14] = st.radio(
            "14. The cat is sleeping _____ the chair.",
            ["on", "in", "at", "from"],
            key="s14"
        )

        answers[15] = st.radio(
            "15. She _____ coffee every morning.",
            ["drink", "drinks", "drank", "drinking"],
            key="s15"
        )
        answer_key = {
            1:"is",
            2:"studies",
            3:"are",
            4:"The",
            5:"goes",
            6:"played",
            7:"are",
            8:"taller",
            9:"an",
            10:"eat",
            11:"is",
            12:"were",
            13:"are",
            14:"on",
            15:"drinks"
        }
        if st.button("Submit Package 1"):

            score = 0

            for num in answer_key:

                if answers[num] == answer_key[num]:
                    score += 1

            st.success(
                f"Your Score: {score}/15"
            )
            st.session_state["structure_p1"] = score
            st.subheader("Answer Explanation")

            explanations = {
                1:"'My brother' is singular, so use 'is'.",
                2:"Sarah is singular, so the verb becomes 'studies'.",
                3:"'Students' is plural, so use 'are'.",
                4:"The sentence refers to a specific book, so use 'The'.",
                5:"Father is singular, so use 'goes'.",
                6:"Yesterday indicates past tense, so use 'played'.",
                7:"Books is plural, so use 'are'.",
                8:"Comparative adjective of tall is taller.",
                9:"Umbrella begins with a vowel sound, so use 'an'.",
                10:"They is plural, so use base verb 'eat'.",
                11:"Teacher is singular, so use 'is'.",
                12:"Last week indicates past tense, so use 'were'.",
                13:"John and Mike are plural, so use 'are'.",
                14:"The correct preposition is 'on the chair'.",
                15:"She is singular, so use 'drinks'."
            }

            for num in explanations:
                st.write(
                    f"{num}. {explanations[num]}"
                )
    elif package == "Package 2":

        answers = {}
        answers[1] = st.radio(
            "1. My mother _____ breakfast every morning.",
            ["cook", "cooks", "cooked", "cooking"],
            key="p2s1"
        )

        answers[2] = st.radio(
            "2. The children _____ happy today.",
            ["is", "am", "are", "be"],
            key="p2s2"
        )

        answers[3] = st.radio(
            "3. I _____ a new bag yesterday.",
            ["buy", "bought", "buys", "buying"],
            key="p2s3"
        )

        answers[4] = st.radio(
            "4. There _____ a cat under the table.",
            ["is", "are", "were", "be"],
            key="p2s4"
        )

        answers[5] = st.radio(
            "5. She has _____ orange.",
            ["a", "an", "the", "some"],
            key="p2s5"
        )

        answers[6] = st.radio(
            "6. They _____ English in class now.",
            ["study", "studies", "are studying", "studied"],
            key="p2s6"
        )

        answers[7] = st.radio(
            "7. My house is _____ the school.",
            ["near", "from", "under", "between"],
            key="p2s7"
        )

        answers[8] = st.radio(
            "8. The movie was very _____.",
            ["interest", "interested", "interesting", "interests"],
            key="p2s8"
        )

        answers[9] = st.radio(
            "9. We _____ to Jakarta last month.",
            ["go", "goes", "went", "going"],
            key="p2s9"
        )

        answers[10] = st.radio(
            "10. The students _____ their homework every day.",
            ["do", "does", "did", "doing"],
            key="p2s10"
        )

        answers[11] = st.radio(
            "11. _____ is my best friend.",
            ["He", "Him", "His", "Himself"],
            key="p2s11"
        )

        answers[12] = st.radio(
            "12. The books _____ on the desk.",
            ["is", "are", "was", "be"],
            key="p2s12"
        )

        answers[13] = st.radio(
            "13. My sister is _____ than me.",
            ["young", "younger", "youngest", "more young"],
            key="p2s13"
        )

        answers[14] = st.radio(
            "14. We have _____ water in the bottle.",
            ["many", "much", "few", "little of"],
            key="p2s14"
        )

        answers[15] = st.radio(
            "15. The teacher _____ the lesson clearly.",
            ["explain", "explains", "explaineds", "explaining"],
            key="p2s15"
        )
        answer_key = {
            1:"cooks",
            2:"are",
            3:"bought",
            4:"is",
            5:"an",
            6:"are studying",
            7:"near",
            8:"interesting",
            9:"went",
            10:"do",
            11:"He",
            12:"are",
            13:"younger",
            14:"much",
            15:"explains"
        }
        if st.button("Submit Package 2"):

            score = 0

            for num in answer_key:

                if answers[num] == answer_key[num]:
                    score += 1

            st.success(
                f"Your Score: {score}/15"
            )
            st.session_state["structure_p2"] = score
            st.subheader("Answer Explanation")

            explanations = {
                1:"My mother is singular, so use 'cooks'.",
                2:"Children is plural, so use 'are'.",
                3:"Yesterday indicates past tense, so use 'bought'.",
                4:"A cat is singular, so use 'is'.",
                5:"Orange begins with a vowel sound, so use 'an'.",
                6:"Now indicates present continuous, so use 'are studying'.",
                7:"The correct preposition is 'near'.",
                8:"Movies can be 'interesting'.",
                9:"Last month indicates past tense, so use 'went'.",
                10:"Students is plural, so use 'do'.",
                11:"Subject pronoun is needed, so use 'He'.",
                12:"Books is plural, so use 'are'.",
                13:"Comparative adjective is 'younger'.",
                14:"Water is uncountable, so use 'much'.",
                15:"Teacher is singular, so use 'explains'."
            }

            for num in explanations:
                st.write(
                    f"{num}. {explanations[num]}"
                )
    elif package == "Package 3":

        answers = {}
        answers[1] = st.radio(
            "1. My brother and I _____ to school together every day.",
            ["goes", "go", "going", "went"],
            key="p3s1"
        )

        answers[2] = st.radio(
            "2. There _____ some milk in the refrigerator.",
            ["are", "were", "is", "be"],
            key="p3s2"
        )

        answers[3] = st.radio(
            "3. She _____ her homework last night.",
            ["finished", "finish", "finishes", "finishing"],
            key="p3s3"
        )

        answers[4] = st.radio(
            "4. We need _____ new computer for our class.",
            ["an", "a", "the", "some"],
            key="p3s4"
        )

        answers[5] = st.radio(
            "5. The students are sitting _____ the classroom.",
            ["on", "at", "in", "from"],
            key="p3s5"
        )

        answers[6] = st.radio(
            "6. My mother _____ delicious cakes.",
            ["makes", "make", "making", "made"],
            key="p3s6"
        )

        answers[7] = st.radio(
            "7. They _____ watching television now.",
            ["is", "are", "am", "be"],
            key="p3s7"
        )

        answers[8] = st.radio(
            "8. This book is _____ than that one.",
            ["interesting", "interest", "more interesting", "most interesting"],
            key="p3s8"
        )

        answers[9] = st.radio(
            "9. _____ teacher is explaining the lesson.",
            ["The", "An", "A", "Some"],
            key="p3s9"
        )

        answers[10] = st.radio(
            "10. We _____ to Bali last holiday.",
            ["go", "went", "goes", "going"],
            key="p3s10"
        )

        answers[11] = st.radio(
            "11. My friend _____ very friendly.",
            ["are", "am", "is", "were"],
            key="p3s11"
        )

        answers[12] = st.radio(
            "12. There _____ many students in the library yesterday.",
            ["were", "is", "am", "be"],
            key="p3s12"
        )

        answers[13] = st.radio(
            "13. She speaks English _____.",
            ["good", "well", "best", "better"],
            key="p3s13"
        )

        answers[14] = st.radio(
            "14. I have _____ apples in my bag.",
            ["much", "little", "many", "any of"],
            key="p3s14"
        )

        answers[15] = st.radio(
            "15. The baby _____ peacefully now.",
            ["sleep", "slept", "is sleeping", "sleeps"],
            key="p3s15"
        )
        answer_key = {
            1:"go",
            2:"is",
            3:"finished",
            4:"a",
            5:"in",
            6:"makes",
            7:"are",
            8:"more interesting",
            9:"The",
            10:"went",
            11:"is",
            12:"were",
            13:"well",
            14:"many",
            15:"is sleeping"
        }
        if st.button("Submit Package 3"):

            score = 0

            for num in answer_key:

                if answers[num] == answer_key[num]:
                    score += 1

            st.success(
                f"Your Score: {score}/15"
            )
            st.session_state["structure_p3"] = score
            st.subheader("Answer Explanation")

            explanations = {
                1:"My brother and I = plural subject, use 'go'.",
                2:"Milk is uncountable singular, so use 'is'.",
                3:"Last night indicates past tense, so use 'finished'.",
                4:"Computer is singular countable, so use 'a'.",
                5:"The correct preposition is 'in the classroom'.",
                6:"Mother is singular, so use 'makes'.",
                7:"They + watching = are watching.",
                8:"Comparative form is 'more interesting'.",
                9:"Specific teacher, so use 'The'.",
                10:"Last holiday indicates past tense, so use 'went'.",
                11:"Friend is singular, so use 'is'.",
                12:"Yesterday indicates past tense plural, so use 'were'.",
                13:"Speak is a verb, so use adverb 'well'.",
                14:"Apples are countable plural, so use 'many'.",
                15:"Now indicates present continuous, so use 'is sleeping'."
            }

            for num in explanations:
                st.write(
                    f"{num}. {explanations[num]}"
                )
    elif package == "Package 4":

        answers = {}
        st.info(
            "Choose the underlined word or phrase that must be changed to make the sentence correct."
        )
        answers[1] = st.radio(
            "1. She (A) go to school every day (B) by bus (C) with her sister (D).",
            ["A", "B", "C", "D"],
            key="p4s1"
        )

        answers[2] = st.radio(
            "2. They (A) is playing football (B) in the field (C) now (D).",
            ["A", "B", "C", "D"],
            key="p4s2"
        )

        answers[3] = st.radio(
            "3. My father (A) work in a bank (B) near our house (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s3"
        )

        answers[4] = st.radio(
            "4. We (A) was very happy (B) yesterday (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s4"
        )

        answers[5] = st.radio(
            "5. I bought (A) a orange (B) from the market (C) yesterday (D).",
            ["A", "B", "C", "D"],
            key="p4s5"
        )

        answers[6] = st.radio(
            "6. The students (A) studies English (B) every day (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s6"
        )

        answers[7] = st.radio(
            "7. She is (A) more tall than her sister (B) in the family (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s7"
        )

        answers[8] = st.radio(
            "8. There (A) are a book (B) on the table (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s8"
        )

        answers[9] = st.radio(
            "9. My mother (A) cook dinner (B) every evening (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s9"
        )

        answers[10] = st.radio(
            "10. The dogs (A) is sleeping (B) under the tree (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s10"
        )

        answers[11] = st.radio(
            "11. He (A) have a new bicycle (B). (C) (D)",
            ["A", "B", "C", "D"],
            key="p4s11"
        )

        answers[12] = st.radio(
            "12. We (A) goes to campus (B) every Monday (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s12"
        )

        answers[13] = st.radio(
            "13. She (A) were at home yesterday (B). (C) (D)",
            ["A", "B", "C", "D"],
            key="p4s13"
        )

        answers[14] = st.radio(
            "14. They (A) enjoys reading books (B) after class (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s14"
        )

        answers[15] = st.radio(
            "15. I am (A) interesting in English (B) lessons (C). (D)",
            ["A", "B", "C", "D"],
            key="p4s15"
        )
        answer_key = {
            1:"A",
            2:"A",
            3:"A",
            4:"A",
            5:"A",
            6:"A",
            7:"A",
            8:"A",
            9:"A",
            10:"A",
            11:"A",
            12:"A",
            13:"A",
            14:"A",
            15:"A"
        }
        if st.button("Submit Package 4"):

            score = 0

            for num in answer_key:

                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.session_state["structure_p4"] = score
            st.write(f"Percentage: {percentage:.0f}%")
            st.subheader("Answer Explanation")

            explanations = {
                1:"go → should be goes",
                2:"is → should be are",
                3:"work → should be works",
                4:"was → should be were",
                5:"a orange → should be an orange",
                6:"studies → should be study",
                7:"more tall → should be taller",
                8:"are → should be is",
                9:"cook → should be cooks",
                10:"is → should be are",
                11:"have → should be has",
                12:"goes → should be go",
                13:"were → should be was",
                14:"enjoys → should be enjoy",
                15:"interesting → should be interested"
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    elif package == "Package 5":

        answers = {}

        st.subheader("Part B: Written Expression")

        st.write(
            "Directions: In each sentence below, four words or phrases are underlined. "
            "Choose the one word or phrase that must be changed in order for the sentence to be correct."
        )
        answers[1] = st.radio(
            "1. My sister (A) study English (B) every day (C) at university (D).",
            ["A", "B", "C", "D"],
            key="p5s1"
        )

        answers[2] = st.radio(
            "2. They (A) was very tired (B) after the exam (C) yesterday (D).",
            ["A", "B", "C", "D"],
            key="p5s2"
        )

        answers[3] = st.radio(
            "3. I bought (A) an new laptop (B) for my study (C) last week (D).",
            ["A", "B", "C", "D"],
            key="p5s3"
        )

        answers[4] = st.radio(
            "4. The students (A) is discussing the assignment (B) in the classroom (C) now (D).",
            ["A", "B", "C", "D"],
            key="p5s4"
        )

        answers[5] = st.radio(
            "5. She can (A) sings very well (B) in front of the audience (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s5"
        )

        answers[6] = st.radio(
            "6. We (A) goes to the library (B) every Saturday (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s6"
        )

        answers[7] = st.radio(
            "7. There (A) are a book (B) on the desk (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s7"
        )

        answers[8] = st.radio(
            "8. My father (A) drive to work (B) every morning (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s8"
        )

        answers[9] = st.radio(
            "9. He is (A) more taller than his brother (B) in the family (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s9"
        )

        answers[10] = st.radio(
            "10. The information (A) are very useful (B) for the students (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s10"
        )

        answers[11] = st.radio(
            "11. She enjoys (A) to read novels (B) in her free time (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s11"
        )

        answers[12] = st.radio(
            "12. I am interested (A) on learning English (B) because it is useful (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s12"
        )

        answers[13] = st.radio(
            "13. The children (A) were playing football (B) when it (C) start to rain (D).",
            ["A", "B", "C", "D"],
            key="p5s13"
        )

        answers[14] = st.radio(
            "14. We need (A) much books (B) for the new semester (C). (D)",
            ["A", "B", "C", "D"],
            key="p5s14"
        )

        answers[15] = st.radio(
            "15. My mother bought (A) a umbrella because (B) it was (C) rain yesterday (D).",
            ["A", "B", "C", "D"],
            key="p5s15"
        )
        answer_key = {
            1:"A",
            2:"A",
            3:"A",
            4:"A",
            5:"A",
            6:"A",
            7:"A",
            8:"A",
            9:"A",
            10:"A",
            11:"A",
            12:"A",
            13:"C",
            14:"A",
            15:"C"
        }
        if st.button("Submit Package 5"):

            score = 0

            for num in answer_key:

                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.session_state["structure_p5"] = score
            st.write(f"Percentage: {percentage:.0f}%")
            st.subheader("Answer Explanation")

            explanations = {
                1:"study → studies",
                2:"was → were",
                3:"an → a",
                4:"is → are",
                5:"sings → sing",
                6:"goes → go",
                7:"are → is",
                8:"drive → drives",
                9:"more taller → taller",
                10:"are → is",
                11:"to read → reading",
                12:"on → in",
                13:"start → started",
                14:"much → many",
                15:"rain → raining"
            }

            for num in explanations:
                st.write(
                    f"{num}. {explanations[num]}"
                )
    st.markdown("---")

    if st.button(
        "Calculate Structure Final Score",
        key="calculate_structure_final"
    ):

        p1 = st.session_state.get("structure_p1", 0)
        p2 = st.session_state.get("structure_p2", 0)
        p3 = st.session_state.get("structure_p3", 0)
        p4 = st.session_state.get("structure_p4", 0)
        p5 = st.session_state.get("structure_p5", 0)

        total = p1 + p2 + p3 + p4 + p5

        percentage = (total / 75) * 100

        st.subheader("📝 Structure Final Score")

        st.write(f"Package 1: {p1}/15")
        st.write(f"Package 2: {p2}/15")
        st.write(f"Package 3: {p3}/15")
        st.write(f"Package 4: {p4}/15")
        st.write(f"Package 5: {p5}/15")

        st.success(f"Total Score: {total}/75")
        st.session_state["structure_total"] = structure_score
        st.success(f"Percentage: {percentage:.0f}%")

        st.session_state["structure_total"] = total
   # READING COMPREHENSION
elif menu == "📚 Reading Comprehension":

    st.title("📚 Reading Comprehension")

    package = st.selectbox(
        "Select Package",
        [
            "Package 1",
            "Package 2",
            "Package 3",
            "Package 4",
            "Package 5"
        ]
    )

    st.write("Selected:", package)

    score = 0
    if package == "Package 1":

        st.subheader("Reading Passage")

        st.write("""
Maria is a university student. She studies English Education at a university in Indonesia.
Every weekday, she wakes up at 5:00 a.m. and prepares for her classes.
She usually eats breakfast with her family before leaving home.

Maria goes to campus by motorcycle. Her classes begin at 7:30 a.m.
She enjoys learning English because she wants to become an English teacher
in the future. Her favorite subject is Speaking because she likes practicing
conversations with her classmates.

After class, Maria often studies in the library. Sometimes she works on
group projects with her friends. In the evening, she reviews her lessons
and prepares for the next day. She believes that studying regularly helps
her improve her English skills.
""")

        answers = {}
        answers[1] = st.radio(
            "1. What is the passage mainly about?",
            [
                "A university library",
                "Maria's daily activities",
                "An English test",
                "A motorcycle trip"
            ],
            key="r1"
        )

        answers[2] = st.radio(
            "2. Where does Maria study?",
            [
                "At a hospital",
                "At a high school",
                "At a university",
                "At a language course"
            ],
            key="r2"
        )

        answers[3] = st.radio(
            "3. What does Maria study?",
            [
                "Mathematics",
                "English Education",
                "Biology",
                "Economics"
            ],
            key="r3"
        )

        answers[4] = st.radio(
            "4. What time does Maria wake up?",
            [
                "4:00 a.m.",
                "5:00 a.m.",
                "6:00 a.m.",
                "7:00 a.m."
            ],
            key="r4"
        )

        answers[5] = st.radio(
            "5. Who does Maria eat breakfast with?",
            [
                "Her friends",
                "Her classmates",
                "Her teachers",
                "Her family"
            ],
            key="r5"
        )

        answers[6] = st.radio(
            "6. How does Maria go to campus?",
            [
                "By bus",
                "By bicycle",
                "By motorcycle",
                "By car"
            ],
            key="r6"
        )

        answers[7] = st.radio(
            "7. What time do her classes begin?",
            [
                "6:30 a.m.",
                "7:00 a.m.",
                "7:30 a.m.",
                "8:00 a.m."
            ],
            key="r7"
        )

        answers[8] = st.radio(
            "8. Why does Maria enjoy learning English?",
            [
                "She wants to travel abroad",
                "She wants to become an English teacher",
                "She wants to open a business",
                "She wants to learn science"
            ],
            key="r8"
        )

        answers[9] = st.radio(
            "9. What is her favorite subject?",
            [
                "Writing",
                "Reading",
                "Grammar",
                "Speaking"
            ],
            key="r9"
        )

        answers[10] = st.radio(
            "10. Why does she like Speaking?",
            [
                "She likes practicing conversations",
                "She likes reading books",
                "She likes taking tests",
                "She likes writing essays"
            ],
            key="r10"
        )

        answers[11] = st.radio(
            "11. Where does Maria often study after class?",
            [
                "At home",
                "In the cafeteria",
                "In the library",
                "In the laboratory"
            ],
            key="r11"
        )

        answers[12] = st.radio(
            "12. What does Maria sometimes do with her friends?",
            [
                "Play football",
                "Watch movies",
                "Work on group projects",
                "Travel together"
            ],
            key="r12"
        )

        answers[13] = st.radio(
            "13. What does Maria do in the evening?",
            [
                "Plays games",
                "Reviews her lessons",
                "Sleeps early",
                "Watches television"
            ],
            key="r13"
        )

        answers[14] = st.radio(
            "14. According to the passage, what helps Maria improve her English skills?",
            [
                "Traveling",
                "Watching movies",
                "Studying regularly",
                "Playing sports"
            ],
            key="r14"
        )

        answers[15] = st.radio(
            "15. The word 'improve' is closest in meaning to:",
            [
                "Increase",
                "Forget",
                "Stop",
                "Change"
            ],
            key="r15"
        )
        answer_key = {
            1:"Maria's daily activities",
            2:"At a university",
            3:"English Education",
            4:"5:00 a.m.",
            5:"Her family",
            6:"By motorcycle",
            7:"7:30 a.m.",
            8:"She wants to become an English teacher",
            9:"Speaking",
            10:"She likes practicing conversations",
            11:"In the library",
            12:"Work on group projects",
            13:"Reviews her lessons",
            14:"Studying regularly",
            15:"Increase"
        }
        if st.button("Submit Reading Package 1"):

            score = 0

            for num in answer_key:

                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.write(f"Percentage: {percentage:.0f}%")
            st.session_state["reading_p1"] = score

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")
    elif package == "Package 2":

        st.subheader("Reading Passage")

        st.write("""
Rina is a first-year university student. She studies English Education.
Every morning, she attends classes with her classmates. Her favorite place
on campus is the library because it is quiet and comfortable.

Rina usually spends two hours in the library after class. She reads books,
completes assignments, and prepares for exams. Sometimes, she meets her
friends there to discuss group projects.

On weekends, Rina joins activities organized by the student association.
She believes these activities help her develop communication and leadership skills.
""")

        answers = {}
        answers[1] = st.radio(
            "1. What is the passage mainly about?",
            [
                "A student's university life",
                "A school library",
                "A weekend trip",
                "A classroom"
            ],
            key="rp2_1"
        )

        answers[2] = st.radio(
            "2. What does Rina study?",
            [
                "Mathematics",
                "English Education",
                "Biology",
                "Economics"
            ],
            key="rp2_2"
        )

        answers[3] = st.radio(
            "3. What year is Rina in?",
            [
                "First year",
                "Second year",
                "Third year",
                "Fourth year"
            ],
            key="rp2_3"
        )

        answers[4] = st.radio(
            "4. What is her favorite place?",
            [
                "Cafeteria",
                "Classroom",
                "Library",
                "Laboratory"
            ],
            key="rp2_4"
        )

        answers[5] = st.radio(
            "5. Why does she like the library?",
            [
                "It is large",
                "It is quiet and comfortable",
                "It is new",
                "It is crowded"
            ],
            key="rp2_5"
        )

        answers[6] = st.radio(
            "6. How long does she usually spend in the library?",
            [
                "One hour",
                "Two hours",
                "Three hours",
                "Four hours"
            ],
            key="rp2_6"
        )

        answers[7] = st.radio(
            "7. What does she do in the library?",
            [
                "Sleeps",
                "Plays games",
                "Reads books",
                "Watches movies"
            ],
            key="rp2_7"
        )

        answers[8] = st.radio(
            "8. She also completes _____ there.",
            [
                "sports",
                "assignments",
                "meetings",
                "interviews"
            ],
            key="rp2_8"
        )

        answers[9] = st.radio(
            "9. Why does she prepare for exams?",
            [
                "To improve her learning",
                "To travel",
                "To work",
                "To exercise"
            ],
            key="rp2_9"
        )

        answers[10] = st.radio(
            "10. Who does she sometimes meet?",
            [
                "Teachers",
                "Parents",
                "Friends",
                "Neighbors"
            ],
            key="rp2_10"
        )

        answers[11] = st.radio(
            "11. What do they discuss?",
            [
                "Sports",
                "Movies",
                "Group projects",
                "Holidays"
            ],
            key="rp2_11"
        )

        answers[12] = st.radio(
            "12. When does Rina join student activities?",
            [
                "Every day",
                "On weekends",
                "At night",
                "During exams"
            ],
            key="rp2_12"
        )

        answers[13] = st.radio(
            "13. Who organizes the activities?",
            [
                "Teachers",
                "Parents",
                "Student association",
                "Librarians"
            ],
            key="rp2_13"
        )

        answers[14] = st.radio(
            "14. What skills does she develop?",
            [
                "Cooking and driving",
                "Communication and leadership",
                "Singing and dancing",
                "Reading and writing"
            ],
            key="rp2_14"
        )

        answers[15] = st.radio(
            "15. The word 'develop' is closest in meaning to:",
            [
                "Improve",
                "Forget",
                "Stop",
                "Leave"
            ],
            key="rp2_15"
        )
        answer_key = {
            1:"A student's university life",
            2:"English Education",
            3:"First year",
            4:"Library",
            5:"It is quiet and comfortable",
            6:"Two hours",
            7:"Reads books",
            8:"assignments",
            9:"To improve her learning",
            10:"Friends",
            11:"Group projects",
            12:"On weekends",
            13:"Student association",
            14:"Communication and leadership",
            15:"Improve"
        }
        if st.button("Submit Reading Package 2"):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.write(f"Percentage: {percentage:.0f}%")
            st.session_state["reading_p2"] = score

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")
            st.subheader("Answer Explanation")

            explanations = {
                1:"The passage discusses Rina's university life.",
                2:"Rina studies English Education.",
                3:"She is a first-year student.",
                4:"Her favorite place is the library.",
                5:"She likes it because it is quiet and comfortable.",
                6:"She spends two hours there after class.",
                7:"She reads books in the library.",
                8:"She completes assignments there.",
                9:"Preparing for exams helps improve learning.",
                10:"She sometimes meets her friends.",
                11:"They discuss group projects.",
                12:"She joins activities on weekends.",
                13:"The student association organizes them.",
                14:"The activities develop communication and leadership skills.",
                15:"Develop means improve."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    elif package == "Package 3":

        st.subheader("Reading Passage")

        st.write("""
Andi likes learning English. He studies English every day for one hour.
He learns new vocabulary, practices grammar, and listens to English songs.

Sometimes, Andi watches English movies with subtitles. This activity helps
him understand pronunciation and improve his listening skills. He also
speaks English with his friends whenever possible.

Andi believes that regular practice is the key to learning a language successfully.
""")

        answers = {}
        answers[1] = st.radio(
            "1. What is the passage mainly about?",
            [
                "Learning English",
                "Watching television",
                "Listening to music",
                "Playing games"
            ],
            key="rp3_1"
        )

        answers[2] = st.radio(
            "2. Who likes learning English?",
            [
                "Rina",
                "Maria",
                "Andi",
                "Budi"
            ],
            key="rp3_2"
        )

        answers[3] = st.radio(
            "3. How often does Andi study English?",
            [
                "Once a week",
                "Every day",
                "Twice a month",
                "Never"
            ],
            key="rp3_3"
        )

        answers[4] = st.radio(
            "4. How long does he study?",
            [
                "30 minutes",
                "One hour",
                "Two hours",
                "Three hours"
            ],
            key="rp3_4"
        )

        answers[5] = st.radio(
            "5. What does he learn?",
            [
                "Vocabulary",
                "Grammar",
                "Both A and B",
                "Science"
            ],
            key="rp3_5"
        )

        answers[6] = st.radio(
            "6. What does he listen to?",
            [
                "News",
                "English songs",
                "Podcasts",
                "Radio shows"
            ],
            key="rp3_6"
        )

        answers[7] = st.radio(
            "7. What does he sometimes watch?",
            [
                "Sports",
                "Cartoons",
                "English movies",
                "Documentaries"
            ],
            key="rp3_7"
        )

        answers[8] = st.radio(
            "8. What do the movies have?",
            [
                "Pictures",
                "Music",
                "Subtitles",
                "Advertisements"
            ],
            key="rp3_8"
        )

        answers[9] = st.radio(
            "9. What does this activity help him understand?",
            [
                "Writing",
                "Pronunciation",
                "Grammar",
                "Reading"
            ],
            key="rp3_9"
        )

        answers[10] = st.radio(
            "10. What skill does it improve?",
            [
                "Listening",
                "Speaking",
                "Writing",
                "Typing"
            ],
            key="rp3_10"
        )

        answers[11] = st.radio(
            "11. With whom does he speak English?",
            [
                "Teachers only",
                "Parents only",
                "Friends",
                "Nobody"
            ],
            key="rp3_11"
        )

        answers[12] = st.radio(
            "12. When does he speak English?",
            [
                "Whenever possible",
                "Never",
                "During holidays only",
                "Once a month"
            ],
            key="rp3_12"
        )

        answers[13] = st.radio(
            "13. What is the key to learning a language?",
            [
                "Talent",
                "Money",
                "Practice",
                "Travel"
            ],
            key="rp3_13"
        )

        answers[14] = st.radio(
            "14. The word 'regular' means:",
            [
                "Consistent",
                "Rare",
                "Difficult",
                "Fast"
            ],
            key="rp3_14"
        )

        answers[15] = st.radio(
            "15. The passage suggests that Andi is:",
            [
                "Lazy",
                "Hardworking",
                "Unhappy",
                "Busy"
            ],
            key="rp3_15"
        )
        answer_key = {
            1:"Learning English",
            2:"Andi",
            3:"Every day",
            4:"One hour",
            5:"Both A and B",
            6:"English songs",
            7:"English movies",
            8:"Subtitles",
            9:"Pronunciation",
            10:"Listening",
            11:"Friends",
            12:"Whenever possible",
            13:"Practice",
            14:"Consistent",
            15:"Hardworking"
        }
        if st.button("Submit Reading Package 3"):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.write(f"Percentage: {percentage:.0f}%")
            st.session_state["reading_p3"] = score

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")
            st.subheader("Answer Explanation")

            explanations = {
                1:"The passage discusses Andi's English learning activities.",
                2:"The person mentioned is Andi.",
                3:"He studies English every day.",
                4:"He studies for one hour.",
                5:"He learns vocabulary and grammar.",
                6:"He listens to English songs.",
                7:"He sometimes watches English movies.",
                8:"The movies have subtitles.",
                9:"The activity helps him understand pronunciation.",
                10:"It improves listening skills.",
                11:"He speaks English with friends.",
                12:"He speaks English whenever possible.",
                13:"Practice is the key to learning a language.",
                14:"Regular means consistent.",
                15:"The passage shows that Andi is hardworking."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    elif package == "Package 4":

        st.subheader("Reading Passage")

        st.write("""
Technology plays an important role in education today.
Many students use laptops, tablets, and smartphones to support their learning activities.

Teachers often use presentation software and online platforms to share materials with students.
Students can also access information quickly through the internet.

Although technology provides many benefits, students should use it wisely.
Spending too much time on social media may reduce study time.
""")

        answers = {}
        answers[1] = st.radio(
            "1. What is the passage mainly about?",
            [
                "Education and technology",
                "Sports activities",
                "Library services",
                "Student clubs"
            ],
            key="rp4_1"
        )

        answers[2] = st.radio(
            "2. What plays an important role in education?",
            [
                "Sports",
                "Technology",
                "Music",
                "Travel"
            ],
            key="rp4_2"
        )

        answers[3] = st.radio(
            "3. What do many students use?",
            [
                "Laptops",
                "Tablets",
                "Smartphones",
                "All of the above"
            ],
            key="rp4_3"
        )

        answers[4] = st.radio(
            "4. Why do students use these devices?",
            [
                "For learning activities",
                "For sleeping",
                "For cooking",
                "For driving"
            ],
            key="rp4_4"
        )

        answers[5] = st.radio(
            "5. Who often uses presentation software?",
            [
                "Parents",
                "Teachers",
                "Doctors",
                "Police officers"
            ],
            key="rp4_5"
        )

        answers[6] = st.radio(
            "6. What do teachers share?",
            [
                "Food",
                "Materials",
                "Clothes",
                "Tickets"
            ],
            key="rp4_6"
        )

        answers[7] = st.radio(
            "7. How can students access information?",
            [
                "Through the internet",
                "Through television",
                "Through newspapers only",
                "Through radio only"
            ],
            key="rp4_7"
        )

        answers[8] = st.radio(
            "8. Information can be accessed:",
            [
                "Slowly",
                "Quickly",
                "Rarely",
                "Never"
            ],
            key="rp4_8"
        )

        answers[9] = st.radio(
            "9. Does technology provide benefits?",
            [
                "Yes",
                "No",
                "Sometimes",
                "Not mentioned"
            ],
            key="rp4_9"
        )

        answers[10] = st.radio(
            "10. How should students use technology?",
            [
                "Wisely",
                "Carelessly",
                "Rarely",
                "Secretly"
            ],
            key="rp4_10"
        )

        answers[11] = st.radio(
            "11. What may reduce study time?",
            [
                "Reading books",
                "Doing homework",
                "Social media",
                "Attending class"
            ],
            key="rp4_11"
        )

        answers[12] = st.radio(
            "12. The word 'benefits' means:",
            [
                "Problems",
                "Advantages",
                "Mistakes",
                "Costs"
            ],
            key="rp4_12"
        )

        answers[13] = st.radio(
            "13. Which device is NOT mentioned?",
            [
                "Laptop",
                "Tablet",
                "Smartphone",
                "Printer"
            ],
            key="rp4_13"
        )

        answers[14] = st.radio(
            "14. Online platforms help teachers:",
            [
                "Share materials",
                "Play games",
                "Travel abroad",
                "Exercise"
            ],
            key="rp4_14"
        )

        answers[15] = st.radio(
            "15. The passage encourages students to:",
            [
                "Avoid technology",
                "Use technology wisely",
                "Stop studying",
                "Buy more devices"
            ],
            key="rp4_15"
        )
        answer_key = {
            1:"Education and technology",
            2:"Technology",
            3:"All of the above",
            4:"For learning activities",
            5:"Teachers",
            6:"Materials",
            7:"Through the internet",
            8:"Quickly",
            9:"Yes",
            10:"Wisely",
            11:"Social media",
            12:"Advantages",
            13:"Printer",
            14:"Share materials",
            15:"Use technology wisely"
        }
        if st.button("Submit Reading Package 4"):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.write(f"Percentage: {percentage:.0f}%")
            st.session_state["reading_p4"] = score

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")
            st.subheader("Answer Explanation")
            explanations = {
                1:"The passage discusses technology in education.",

                2:"Technology plays an important role in education.",

                3:"Laptops, tablets, and smartphones are all mentioned.",

                4:"Students use them for learning activities.",

                5:"Teachers often use presentation software.",

                6:"Teachers share learning materials.",

                7:"Students access information through the internet.",

                8:"The passage says information can be accessed quickly.",

                9:"Technology provides many benefits.",

                10:"Students should use technology wisely.",

                11:"Too much social media may reduce study time.",

                12:"Benefits means advantages.",

                13:"Printer is not mentioned.",

                14:"Online platforms help teachers share materials.",

                15:"The passage encourages wise use of technology."

            }



            for num in explanations:

                st.write(f"{num}. {explanations[num]}")
    elif package == "Package 5":

        st.subheader("Reading Passage")

        st.write("""
A healthy lifestyle is important for students. Good health helps students focus
better in class and perform well in their studies.

Students should eat nutritious food, drink enough water, and exercise regularly.
They should also get enough sleep every night. Most experts recommend seven to
eight hours of sleep for young adults.

In addition, students should manage their stress and balance their academic and
personal lives. Healthy habits can improve both physical and mental well-being.
""")

        answers = {}
        answers[1] = st.radio(
            "1. What is the passage mainly about?",
            [
                "Healthy lifestyle",
                "University clubs",
                "Technology",
                "Transportation"
            ],
            key="rp5_1"
        )

        answers[2] = st.radio(
            "2. Why is good health important?",
            [
                "It helps students focus better",
                "It helps students travel",
                "It helps students drive",
                "It helps students shop"
            ],
            key="rp5_2"
        )

        answers[3] = st.radio(
            "3. What should students eat?",
            [
                "Fast food only",
                "Nutritious food",
                "Candy only",
                "Snacks only"
            ],
            key="rp5_3"
        )

        answers[4] = st.radio(
            "4. What should students drink?",
            [
                "Enough water",
                "Soda only",
                "Coffee only",
                "Juice only"
            ],
            key="rp5_4"
        )

        answers[5] = st.radio(
            "5. Students should exercise:",
            [
                "Rarely",
                "Regularly",
                "Never",
                "Monthly"
            ],
            key="rp5_5"
        )

        answers[6] = st.radio(
            "6. What else should students get?",
            [
                "More homework",
                "More money",
                "Enough sleep",
                "More classes"
            ],
            key="rp5_6"
        )

        answers[7] = st.radio(
            "7. How many hours of sleep are recommended?",
            [
                "3–4 hours",
                "5–6 hours",
                "7–8 hours",
                "10–12 hours"
            ],
            key="rp5_7"
        )

        answers[8] = st.radio(
            "8. Who recommends this amount of sleep?",
            [
                "Teachers",
                "Experts",
                "Friends",
                "Parents"
            ],
            key="rp5_8"
        )

        answers[9] = st.radio(
            "9. Students should manage their:",
            [
                "Time only",
                "Money only",
                "Stress",
                "Travel plans"
            ],
            key="rp5_9"
        )

        answers[10] = st.radio(
            "10. Students should balance:",
            [
                "Academic and personal lives",
                "Work and travel",
                "Sports and games",
                "Family and hobbies"
            ],
            key="rp5_10"
        )

        answers[11] = st.radio(
            "11. Healthy habits can improve:",
            [
                "Physical well-being",
                "Mental well-being",
                "Both A and B",
                "Neither"
            ],
            key="rp5_11"
        )

        answers[12] = st.radio(
            "12. The word 'focus' is closest in meaning to:",
            [
                "Concentrate",
                "Sleep",
                "Walk",
                "Relax"
            ],
            key="rp5_12"
        )

        answers[13] = st.radio(
            "13. The word 'regularly' means:",
            [
                "Consistently",
                "Rarely",
                "Never",
                "Slowly"
            ],
            key="rp5_13"
        )

        answers[14] = st.radio(
            "14. What does the passage suggest?",
            [
                "Healthy habits are beneficial",
                "Sleep is unnecessary",
                "Exercise is harmful",
                "Water is unhealthy"
            ],
            key="rp5_14"
        )

        answers[15] = st.radio(
            "15. Which title is best for this passage?",
            [
                "Healthy Lifestyle for Students",
                "Learning Technology",
                "University Library",
                "English Class"
            ],
            key="rp5_15"
        )
        answer_key = {
            1:"Healthy lifestyle",
            2:"It helps students focus better",
            3:"Nutritious food",
            4:"Enough water",
            5:"Regularly",
            6:"Enough sleep",
            7:"7–8 hours",
            8:"Experts",
            9:"Stress",
            10:"Academic and personal lives",
            11:"Both A and B",
            12:"Concentrate",
            13:"Consistently",
            14:"Healthy habits are beneficial",
            15:"Healthy Lifestyle for Students"
        }
        if st.button("Submit Reading Package 5", key="submit_reading_p5"):

            score = 0

            for num in answer_key:
                if answers[num] == answer_key[num]:
                    score += 1

            percentage = (score / 15) * 100

            st.success(f"Your Score: {score}/15")
            st.write(f"Percentage: {percentage:.0f}%")
            st.session_state["reading_p5"] = score

            if percentage >= 80:
                st.success("Excellent!")
            elif percentage >= 60:
                st.info("Good Job!")
            else:
                st.warning("Keep Practicing!")
            st.subheader("Answer Explanation")

            explanations = {
                1:"The passage discusses a healthy lifestyle for students.",
                2:"Good health helps students focus better in class.",
                3:"Students should eat nutritious food.",
                4:"Students should drink enough water.",
                5:"Exercise should be done regularly.",
                6:"Students should get enough sleep.",
                7:"Experts recommend 7–8 hours of sleep.",
                8:"The recommendation comes from experts.",
                9:"Students should manage their stress.",
                10:"Students should balance academic and personal lives.",
                11:"Healthy habits improve physical and mental well-being.",
                12:"Focus means concentrate.",
                13:"Regularly means consistently.",
                14:"The passage suggests healthy habits are beneficial.",
                15:"The best title is Healthy Lifestyle for Students."
            }

            for num in explanations:
                st.write(f"{num}. {explanations[num]}")
    st.markdown("---")
    st.subheader("📖 Reading Final Score")

    reading_score = (
        st.session_state.get("reading_p1", 0) +
        st.session_state.get("reading_p2", 0) +
        st.session_state.get("reading_p3", 0) +
        st.session_state.get("reading_p4", 0) +
        st.session_state.get("reading_p5", 0)
    )

    st.write(f"Reading Score: {reading_score}/75")
    st.session_state["reading_total"] = reading_score
    st.markdown("---")
    st.subheader("🎓 Overall TOEFL Score")

    listening_score = st.session_state.get("listening_total", 0)
    structure_score = st.session_state.get("structure_total", 0)
    reading_score = st.session_state.get("reading_total", 0)

    total_score = (
        listening_score +
        structure_score +
        reading_score
    )

    st.success(f"Total TOEFL Raw Score: {total_score}/225")
    if st.button("Save Result"):

        if "leaderboard" not in st.session_state:
            st.session_state["leaderboard"] = []

        st.session_state["leaderboard"].append(
            {
                "Name": student_name,
                "Listening": listening_score,
                "Structure": structure_score,
                "Reading": reading_score,
                "Total": total_score
            }
        )

        st.success("Result Saved Successfully!")

    st.markdown("---")
    st.subheader("Participant Information")

    st.write(f"Name: {student_name}")
   
# LEADERBOARD
elif menu == "🏆 Leaderboard":

    st.title("🏆 Leaderboard")

    if "leaderboard" in st.session_state:

        leaderboard = sorted(
            st.session_state["leaderboard"],
            key=lambda x: x["Total"],
            reverse=True
        )

        rank = 1

        for student in leaderboard:

            st.write(
                f"{rank}. {student['Name']} - {student['Total']}/225"
            )

            rank += 1

    else:
        st.info("No results saved yet.")

# ABOUT
elif menu == "ℹ️ About":
    st.title("ℹ️ About This Application")

    st.markdown("---")

    st.subheader("Application Name")

    st.write("TOEFL ITP Beginner 1 Learning App")

    st.subheader("Purpose")

    st.write("""
This application is designed to help beginner learners understand the
basic concepts of TOEFL ITP through interactive learning activities,
practice exercises, and quizzes.
""")

    st.subheader("Features")

    st.write("""
✅ Introduction to TOEFL ITP

✅ Grammar Practice

✅ Vocabulary Builder

✅ Reading Practice

✅ Mini TOEFL Quiz
""")

    st.subheader("Target Users")

    st.write("""
This application is intended for beginner English learners who want to
prepare for TOEFL ITP and improve their basic English skills.
""")

    st.subheader("Version")

    st.write("Version 1.0")

    st.markdown("---")

    st.success("Thank you for using TOEFL ITP Beginner 1 Learning App!")