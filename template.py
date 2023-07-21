from enum import Enum


class EvolutionTemplates(Enum):
    IDEA_GENERATION_PROMPT_TMPL = (
        "Step 1: Begin by identifying the spark of an idea that piques your curiosity. "
        "Consider what makes this idea intriguing and why you believe it holds promise for growth. "
        "This initial idea will form the foundation for our exploration and set the direction for our creative journey.\n"
        "---------------------\n"
        "Idea: {prompt}\n"
        "---------------------\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in generating the initial idea or prompt.\n"
        "- Brainstorm related ideas.\n"
        "- Evaluate the language and clarity of the prompts.\n"
        "- Refine the language and style of the prompts.\n"
        "- Assist in mapping out and structuring the idea or prompt.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Collaborate with the Vocabulary Deconstructor in the ideation phase.\n"
        "- Oversee the refinement process.\n"
        "- Research and gather information.\n"
        "- Structure the idea and refine the language and style of the prompts.\n"
    )

    STEP_1_1_PROMPT_TMPL = (
        "Step 1.1: Drawing inspiration from our initial idea ('{step_1_output}'), "
        "let's brainstorm and expand upon it. What related ideas, themes, or directions can we explore? "
        "This step encourages free thinking and helps us to see the potential extensions of our original idea.\n"
        "---------------------\n"
        "Brainstormed Ideas: \n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in brainstorming and developing related ideas.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Collaborate with the Vocabulary Deconstructor in brainstorming and developing related ideas.\n"
    )

    STEP_1_1_1_PROMPT_TMPL = (
        "Step 1.1.1: After brainstorming, we now have a variety of ideas ('{step_1_1_output}'). "
        "The next step is to identify common threads or themes among them. "
        "Grouping related ideas helps us to see patterns and build a more coherent structure from our initial free thinking.\n"
        "---------------------\n"
        "Group 1: \n"
        "Group 2: \n"
        "Group 3: \n"
        "Vocabulary Deconstructor's Context {vd_context_str} :\n"
        "- Collaborate with the Target Structure in categorizing and grouping related ideas.\n"
        "Target Structure's Context {ts_context_str} :\n"
        "- Collaborate with the Vocabulary Deconstructor in categorizing and grouping related ideas.\n"
    )

    STEP_1_1_2_PROMPT_TMPL = (
        "Step 1.1.2: Considering our grouped ideas ('{step_1_1_1_output}'), "
        "let's determine which of these groups are most relevant or hold the most promise in relation to our original idea. "
        "By ranking these groups, we can prioritize our focus and effort in the next stages.\n"
        "---------------------\n"
        "Rank the groups: \n"
        "Vocabulary Deconstructor's Context {vd_context_str} :\n"
        "- Collaborate with the Target Structure in ranking the groups based on relevance and potential.\n"
        "Target Structure's Context {ts_context_str} :\n"
        "- Collaborate with the Vocabulary Deconstructor in ranking the groups based on relevance and potential.\n"
    )

    STEP_1_1_3_PROMPT_TMPL = (
        "Step 1.1.3: With our ranked groups ('{step_1_1_2_output}'), "
        "it's time to evaluate the potential challenges and benefits of each. "
        "This critical assessment helps us anticipate issues and understand the potential value each group can bring to our overarching idea.\n"
        "---------------------\n"
        "Evaluate the feasibility and impact of each group: \n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Evaluate the feasibility and impact of each group.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Collaborate with the Vocabulary Deconstructor in evaluating the feasibility and impact of each group.\n"
    )

    STEP_1_2_PROMPT_TMPL = (
        "Step 1.2: Now, using the output of the previous steps ('{step_1_1_3_output}'), "
        "let's delve deeper into our initial idea. Are there certain aspects or sub-topics that we could explore more thoroughly? "
        "In this step, we seek to add depth and complexity to our idea by expanding its scope and detail.\n"
        "---------------------\n"
        "Sub-topic 1: \n"
        "Sub-topic 2: \n"
        "Sub-topic 3: \n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in expanding on the sub-topics.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Collaborate with the Vocabulary Deconstructor in expanding on the sub-topics.\n"
    )

    STEP_1_2_1_PROMPT_TMPL = (
        "Step 1.2.1: With our enriched idea and related sub-topics in hand ('{step_1_2_output}'), "
        "let's dissect the idea further into its key components. Understanding these elements can provide a detailed insight into the structure of our idea.\n"
        "---------------------\n"
        "Break down the idea into key components: \n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Break down the idea into key components.\n"
    )

    STEP_1_2_2_PROMPT_TMPL = (
        "Step 1.2.2: Considering our dissected idea ('{step_1_2_1_output}'), "
        "let's shift our perspective and examine the idea from different viewpoints. "
        "This exploration will help us to uncover new aspects and potentials that might have been overlooked.\n"
        "---------------------\n"
        "Explore the idea from different perspectives: \n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in exploring the idea from different perspectives.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Collaborate with the Vocabulary Deconstructor in exploring the idea from different perspectives.\n"
    )

    STEP_1_2_3_PROMPT_TMPL = (
        "Step 1.2.3: After deep introspection of our idea, it's time to seek external influences that could further enrich it. "
        "Considering our idea and its exploration so far ('{step_1_2_2_output}'), "
        "identify inspirations from the world around us and feedback that can refine our idea. In this step, we welcome the outside world to shape our creative process.\n"
        "---------------------\n"
        "External inspiration or feedback to incorporate: \n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in seeking external inspirations and feedback.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Identify relevant external sources of inspiration and feedback.\n"
        "- Evaluate the potential impact of incorporating external influences into the idea.\n"
    )

    STEP_2_PROMPT_TMPL = (
        "Step 2: Refine and Develop Idea or Prompt\n"
        "--------------------------------------------------------\n"
        "Now that we have a solid foundation for our idea, it's time to refine and develop it further. "
        "In this step, we will conduct thorough research, map out the idea, and refine its language and style.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 1.2.3): '{step_1_2_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure to refine and develop the idea.\n"
        "- Assist in researching and gathering relevant information.\n"
        "- Help in structuring and refining the language and style of the idea.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Oversee the refinement and development process.\n"
        "- Conduct comprehensive research and gather necessary information.\n"
        "- Create visual diagrams or outlines to map out the idea's structure.\n"
        "- Refine the language and style of the idea or prompt for clarity and effectiveness.\n"
    )

    STEP_2_1_PROMPT_TMPL = (
        "Step 2.1: Research and Gather Information\n"
        "--------------------------------------------------------\n"
        "In this step, we will conduct thorough research and gather relevant information "
        "to further enhance and support our idea.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 1.2.3): '{step_1_2_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in identifying credible sources and references.\n"
        "- Assist in analyzing and synthesizing the gathered information.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Identify credible sources and references to gather valuable insights.\n"
        "- Analyze and synthesize the collected information to extract relevant details.\n"
    )

    STEP_2_1_1_PROMPT_TMPL = (
        "Step 2.1.1: Identify Credible Sources and References\n"
        "--------------------------------------------------------\n"
        "To ensure the reliability and accuracy of our information, let's identify credible sources and references.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.1): '{step_2_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Aid in pinpointing reliable sources that can provide accurate and trustworthy information.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- From the vast array of potential sources, select those that are reputable, trustworthy, and relevant.\n"
    )

    STEP_2_1_2_PROMPT_TMPL = (
        "Step 2.1.2: Analyze and Synthesize Information\n"
        "--------------------------------------------------------\n"
        "Let's thoroughly analyze and synthesize the gathered information to extract valuable insights and key findings.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.1): '{step_2_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Assist in breaking down complex information and recombining it in a way that enhances understanding.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Digest the collected data, discern patterns, draw conclusions, and reassemble it in a new, enlightening format.\n"
    )

    STEP_2_1_3_PROMPT_TMPL = (
        "Step 2.1.3: Determine Relevance and Applicability of Information\n"
        "--------------------------------------------------------\n"
        "Now, let's evaluate the relevance and applicability of the gathered information to our idea. "
        "This step will help us identify which information is most valuable and useful for our purposes.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.1.2): '{step_2_1_2_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Help in evaluating the relevance of the gathered data to the main idea.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Judge the value of each piece of information, discerning which ones are most applicable to the idea or prompt.\n"
    )

    STEP_2_2_PROMPT_TMPL = (
        "Step 2.2: Map out and Structure Idea or Prompt\n"
        "--------------------------------------------------------\n"
        "In this step, we will create visual diagrams or outlines to map out the structure of our idea or prompt. "
        "This visual representation will provide a clear and organized overview of the idea's components and relationships.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.1.3): '{step_2_1_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in creating visual diagrams or outlines.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Create visual diagrams or outlines to visually represent the structure of the idea or prompt.\n"
        "- Refer to the information analyzed in the previous step for mapping out the structure.\n"
    )

    STEP_2_2_1_PROMPT_TMPL = (
        "Step 2.2.1: Create Visual Diagrams or Outlines\n"
        "--------------------------------------------------------\n"
        "Let's create visual diagrams or outlines to visually represent the structure of our idea or prompt. "
        "This will help us to visualize and organize the various components and sub-topics of our idea.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.2): '{step_2_2_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Assist in transforming abstract ideas into clear, visual representations, making them easier to understand and refine.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Transform the complex idea or prompt into visual diagrams or outlines, enhancing comprehension and future development.\n"
    )

    STEP_2_2_2_PROMPT_TMPL = (
        "Step 2.2.2: Group and Organize Components or Sub-Topics\n"
        "--------------------------------------------------------\n"
        "Now, let's group and organize the components or sub-topics of our idea based on their similarities or relationships. "
        "This will provide a logical structure and make it easier to navigate through different aspects of the idea.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.2.1): '{step_2_2_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Identify related components or sub-topics.\n"
        "- Arrange them logically to streamline the flow of the idea.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Organize the components to enhance understanding and comprehension.\n"
        "- Use the relationships between components to guide the organization process.\n"
    )

    STEP_2_2_3_PROMPT_TMPL = (
        "Step 2.2.3: Determine Logical Flow and Transitions\n"
        "--------------------------------------------------------\n"
        "In this step, we will determine the logical flow and transitions between different components or sub-topics of our idea. "
        "This ensures a smooth and coherent progression of thoughts and ideas throughout the development process.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.2.2): '{step_2_2_2_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Evaluate the transitions between components or sub-topics.\n"
        "- Ensure a clear and logical progression from one point to the next.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Consider the reader's perspective to ensure the flow is intuitive and smooth.\n"
        "- Incorporate appropriate transitions to guide the reader through the idea or prompt.\n"
    )

    STEP_2_3_PROMPT_TMPL = (
        "Step 2.3: Refine Language and Style of Idea or Prompt\n"
        "--------------------------------------------------------\n"
        "To effectively communicate our idea, it is crucial to refine the language and style of the idea or prompt. "
        "This step involves making the language clear, concise, and engaging while establishing a consistent tone and voice.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.2.3): '{step_2_2_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Identify and eliminate unnecessary or redundant language.\n"
        "- Clarify and simplify language for ease of understanding.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Establish a consistent tone and voice throughout the idea or prompt.\n"
        "- Refer to the visual diagrams or outlines created in the previous step for refining language and style.\n"
    )

    STEP_2_3_1_PROMPT_TMPL = (
        "Step 2.3.1: Identify and Eliminate Unnecessary or Redundant Language\n"
        "--------------------------------------------------------\n"
        "Let's review the language used in our idea or prompt and identify any unnecessary or redundant phrases. "
        "By removing such language, we can ensure that our idea is concise and to the point.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.3): '{step_2_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Scan the idea or prompt for redundant or unnecessary language.\n"
        "- Simplify language to maintain clarity and conciseness.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Focus on retaining the essential details and information.\n"
        "- Reframe sentences if needed to remove redundancy while keeping the main idea intact.\n"
    )

    STEP_2_3_2_PROMPT_TMPL = (
        "Step 2.3.2: Clarify and Simplify Language for Ease of Understanding\n"
        "--------------------------------------------------------\n"
        "To enhance understanding, let's clarify and simplify the language used in our idea or prompt. "
        "This involves rephrasing complex sentences, avoiding jargon, and ensuring the language is accessible to the target audience.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.3.1): '{step_2_3_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Help in rephrasing complex sentences and avoiding jargon.\n"
        "- Ensure that the language used is easy to understand and accessible to the target audience.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Rephrase complex sentences and clarify ambiguous phrases.\n"
        "- Avoid technical jargon unless necessary and use simpler alternatives when possible.\n"
        "- Ensure that the language is clear, concise, and easily understandable by the target audience.\n"
    )

    STEP_2_3_3_PROMPT_TMPL = (
        "Step 2.3.3: Establish Consistent Tone and Voice\n"
        "--------------------------------------------------------\n"
        "In order to create a cohesive and engaging idea or prompt, it is important to establish a consistent tone and voice. "
        "This step involves defining the desired tone, whether it's formal, informal, professional, or creative, and ensuring that it remains consistent throughout the content.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 2.3.2): '{step_2_3_2_output}'\n"
        "Establish consistent tone and voice (refer to previous step):\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in establishing the desired tone and voice.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Define the desired tone and voice for the idea or prompt.\n"
        "- Ensure that the tone and voice remain consistent throughout the content.\n"
        "Step 2.3.2): '{step_2_3_2_output}'\n"
        "Establish consistent tone and voice (refer to previous step):\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure in establishing the desired tone and voice.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Define the desired tone and voice for the idea or prompt.\n"
        "- Ensure that the tone and voice remain consistent throughout the content.\n"
    )

    STEP_3_PROMPT_TMPL = (
        "Step 3: Breathe Life Into Your Idea\n"
        "--------------------------------------------------------\n"
        "We've brainstormed and refined our idea, now let's transform it into reality. "
        "Our Target Structure (TS) will spearhead this transformative process.\n"
        "--------------------------------------------------------\n"
        "Insights from Step 2.3.3: '{step_2_3_3_output}'\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Design a detailed implementation plan with a timeline.\n"
        "- Dissect the implementation process into manageable tasks.\n"
        "- Ascertain necessary resources and budget for successful execution.\n"
        "- Set a clear timeline and deadlines to guide our journey.\n"
    )

    STEP_3_1_PROMPT_TMPL = (
        "Step 3.1: Sketching the Roadmap\n"
        "--------------------------------------------------------\n"
        "In this phase, the Target Structure (TS) will craft a roadmap for our idea's journey. "
        "This includes decomposing the implementation into tasks, determining required resources and budget, and setting a timeline with clear milestones.\n"
        "--------------------------------------------------------\n"
        "Inspired by Step 3: '{step_3_output}'\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Task Decomposition:\n"
        "   - Step 3.1.1: {step_3_1_1_desc}\n"
        "   - Step 3.1.2: {step_3_1_2_desc}\n"
        "   - Step 3.1.3: {step_3_1_3_desc}\n"
    )

    STEP_3_1_1_PROMPT_TMPL = (
        "Step 3.1.1: The Task-Breaker\n"
        "--------------------------------------------------------\n"
        "Let's turn our grand plan into small, achievable tasks. "
        "This will make our journey manageable and efficient.\n"
        "--------------------------------------------------------\n"
        "Guided by Step 3.1: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure to segment the implementation into tasks.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Work with the Vocabulary Deconstructor to convert the plan into tasks.\n"
    )

    STEP_3_1_2_PROMPT_TMPL = (
        "Step 3.1.2: Resource Scout\n"
        "--------------------------------------------------------\n"
        "Now, let's identify the resources and budget required for our journey. "
        "This will ensure we are well-equipped for our adventure.\n"
        "--------------------------------------------------------\n"
        "Informed by Step 3.1: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure to pinpoint necessary resources and budget.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Collaborate with the Vocabulary Deconstructor to earmark necessary resources and budget.\n"
    )

    STEP_3_1_3_PROMPT_TMPL = (
        "Step 3.1.3: The Timekeeper\n"
        "--------------------------------------------------------\n"
        "It's time to set our clocks. A clear timeline and deadlines will keep us focused and accountable. "
        "--------------------------------------------------------\n"
        "Drawing from Step 3.1: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure to outline a timeline and deadlines.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Collaborate with the Vocabulary Deconstructor to establish a clear timeline and deadlines.\n"
    )

    STEP_3_2_PROMPT_TMPL = (
        "Step 3.2: Set the Wheels in Motion\n"
        "--------------------------------------------------------\n"
        "Now, it's showtime! We'll execute our plan and keep an eye on our progress. "
        "This involves delegating tasks, monitoring progress, adapting on the fly, and evaluating the fruits of our labor.\n"
        "--------------------------------------------------------\n"
        "Informed by Step 3.1.3: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure in task delegation.\n"
        "- Keep an eagle eye on the progress, and adjust the course as required.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Delegate tasks for the implementation.\n"
        "- Monitor the progress and course-correct as needed.\n"
        "- Assess the success of the implementation.\n"
    )

    STEP_3_2_1_PROMPT_TMPL = (
        "Step 3.2.1: Taskmaster At Work\n"
        "--------------------------------------------------------\n"
        "To ensure a smooth execution, let's assign tasks and roles to our team members. "
        "This will make everyone's responsibility clear and foster accountability.\n"
        "--------------------------------------------------------\n"
        "Drawing from Step 3.2: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure to allocate tasks and roles.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Assign tasks and roles, considering the expertise and responsibilities of team members.\n"
    )

    STEP_3_2_2_PROMPT_TMPL = (
        "Step 3.2.2: The Progress Tracker\n"
        "--------------------------------------------------------\n"
        "Our journey will require constant vigilance. By closely monitoring our progress, we can adapt to any hitches and stay on track.\n"
        "--------------------------------------------------------\n"
        "Guided by Step 3.2: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure to track progress and suggest necessary adjustments.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Monitor the journey, making necessary adjustments to ensure successful execution.\n"
    )

    STEP_3_2_3_PROMPT_TMPL = (
        "Step 3.2.3: Measure of Success\n"
        "--------------------------------------------------------\n"
        "With our journey complete, it's time to assess our progress. "
        "This will allow us to gauge our success, learn from the process, and celebrate our achievements.\n"
        "--------------------------------------------------------\n"
        "Informed by Step 3.2.2: {previous_step_output}\n"
        "Vocabulary Deconstructor's Context ({vd_context_str}):\n"
        "- Collaborate with the Target Structure in evaluating the success of the implementation.\n"
        "Target Structure's Context ({ts_context_str}):\n"
        "- Assess and measure the success of the implementation using predefined goals and criteria.\n"
    )

    STEP_4_PROMPT_TMPL = (
        "Step 4: Reflect and Iterate on Idea or Prompt\n"
        "--------------------------------------------------------\n"
        "After the implementation, it's important to reflect on the success of the idea or prompt and identify areas for improvement. "
        "In this step, both the Target Structure (TS) and Vocabulary Deconstructor (VD) will play crucial roles in evaluating and analyzing the implementation.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 3.2.3): '{step_3_2_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure to evaluate the success of the implementation.\n"
        "- Provide insights and analysis based on the gathered data and feedback.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Evaluate the effectiveness of the implementation and its alignment with the initial goals.\n"
        "- Analyze the feedback received and make necessary adjustments to improve the idea or prompt.\n"
    )

    STEP_4_1_PROMPT_TMPL = (
        "Step 4.1: Evaluate and Analyze Success of Implementation\n"
        "--------------------------------------------------------\n"
        "In this step, the Target Structure (TS) and Vocabulary Deconstructor (VD) will collaborate to evaluate and analyze the success of the implementation. "
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4): '{step_4_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure to determine the effectiveness of the implementation.\n"
        "- Analyze the feedback received and provide insights for potential improvements.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Evaluate the success of the implementation in achieving its intended goals.\n"
        "- Analyze the feedback and make necessary adjustments to enhance the idea or prompt.\n"
    )

    STEP_4_1_1_PROMPT_TMPL = (
        "Step 4.1.1: Gauge the Echoes of Implementation\n"
        "--------------------------------------------------------\n"
        "Time to determine the ripple effects of our implemented idea or prompt. Let's measure its impact and results.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.1): '{step_4_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Assess the impact and results of the implemented idea or prompt.\n"
        "- Determine the effectiveness of the implementation.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Reflect on the implementation process.\n"
        "- Identify key success factors and areas for improvement.\n"
    )

    STEP_4_1_2_PROMPT_TMPL = (
        "Step 4.1.2: Navigating the Sea of Feedback\n"
        "--------------------------------------------------------\n"
        "Now we dive into the sea of feedback, seeking pearls of wisdom to refine our idea or prompt.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.1): '{step_4_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Analyze the feedback received.\n"
        "- Identify necessary adjustments to improve the idea or prompt.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Understand feedback and identify how it can be used for improvement.\n"
        "- Prioritize feedback and create an action plan for adjustments.\n"
    )

    STEP_4_1_3_PROMPT_TMPL = (
        "Step 4.1.3: Reflecting on the Learned Lessons and Possible Improvements\n"
        "--------------------------------------------------------\n"
        "This step involves taking a moment to ponder on what we've learned from the implementation and identifying possible areas for improvement.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.1.2): '{step_4_1_2_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Reflect on the lessons learned from the implementation.\n"
        "- Identify potential areas for improvement.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Review the feedback and adjustments made.\n"
        "- Understand how these adjustments have influenced the effectiveness of the idea or prompt.\n"
    )

    STEP_4_2_PROMPT_TMPL = (
        "Step 4.2: Identify and Incorporate Feedback\n"
        "--------------------------------------------------------\n"
        "In this step, the Target Structure (TS) will focus on identifying valuable feedback and incorporating it into the next iteration of the idea or prompt.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.1.3): '{step_4_1_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Collaborate with the Target Structure to identify feedback for potential improvements.\n"
        "- Provide insights and suggestions for incorporating feedback into the next iteration.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Identify areas for improvement based on the feedback received.\n"
        "- Determine potential solutions and evaluate their effectiveness.\n"
        "- Implement the selected solution and measure its success.\n"
        "- Reflect on the lessons learned and potential improvements for future iterations.\n"
    )

    STEP_4_2_1_PROMPT_TMPL = (
        "Step 4.2.1: Identify Areas for Improvement\n"
        "--------------------------------------------------------\n"
        "Let's carefully review the feedback received and identify specific areas of the idea or prompt that can be improved.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2): '{step_4_2_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Review feedback received.\n"
        "- Identify specific areas for improvement.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Analyze feedback carefully.\n"
        "- Pinpoint aspects of the idea or prompt that require refinement.\n"
    )

    STEP_4_2_2_PROMPT_TMPL = (
        "Step 4.2.2: Determine Potential Solutions\n"
        "--------------------------------------------------------\n"
        "Now, let's brainstorm potential solutions to address the identified areas for improvement.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.1): '{step_4_2_1_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Brainstorm potential solutions.\n"
        "- Address identified areas for improvement.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Generate a range of possible solutions.\n"
        "- Choose the solutions that most effectively address the areas for improvement.\n"
    )

    STEP_4_2_3_PROMPT_TMPL = (
        "Step 4.2.3: Evaluate and Select Best Solution\n"
        "--------------------------------------------------------\n"
        "In this step, let's evaluate the potential solutions and select the one that is most effective and feasible.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.2): '{step_4_2_2_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Evaluate potential solutions.\n"
        "- Select the most effective and feasible solution.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Assess the benefits and drawbacks of each solution.\n"
        "- Choose the best solution based on this assessment.\n"
    )
    STEP_4_2_4_PROMPT_TMPL = (
        "Step 4.2.4: Implement and Execute Solution\n"
        "--------------------------------------------------------\n"
        "Now, let's implement and execute the selected solution to address the areas for improvement.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.3): '{step_4_2_3_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Implement the selected solution.\n"
        "- Execute the plan and address the identified areas for improvement.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Execute the selected solution.\n"
        "- Monitor the process and ensure that the solution is implemented as planned.\n"
    )

    STEP_4_2_5_PROMPT_TMPL = (
        "Step 4.2.5: Evaluate and Measure Success of Solution\n"
        "--------------------------------------------------------\n"
        "In order to assess the effectiveness of the implemented solution, let's evaluate and measure its success.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.4): '{step_4_2_4_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Evaluate the implemented solution.\n"
        "- Measure its success against the set goals and objectives.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Assess the success of the solution.\n"
        "- Determine if it has effectively addressed the areas for improvement.\n"
    )

    STEP_4_2_6_PROMPT_TMPL = (
        "Step 4.2.6: Reflect on Lessons Learned and Potential Improvements\n"
        "--------------------------------------------------------\n"
        "This step involves reflecting on the lessons learned from the implemented solution and identifying potential areas for further improvement.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.5): '{step_4_2_5_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Reflect on the lessons learned from the solution implementation.\n"
        "- Identify potential areas for further improvement.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Review the entire process and identify what worked and what didn't.\n"
        "- Determine areas for future improvement.\n"
    )

    STEP_4_2_7_PROMPT_TMPL = (
        "Step 4.2.7: Incorporate Feedback into Next Iteration\n"
        "--------------------------------------------------------\n"
        "Let's incorporate the valuable feedback received into the next iteration of the idea or prompt.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.6): '{step_4_2_6_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Understand the feedback received.\n"
        "- Incorporate this feedback into the next iteration of the idea or prompt.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Plan for the next iteration of the idea or prompt.\n"
        "- Incorporate lessons learned and feedback into this plan.\n"
    )

    STEP_4_2_8_PROMPT_TMPL = (
        "Step 4.2.8: Repeat Steps 4.2.1-4.2.7 as Needed\n"
        "--------------------------------------------------------\n"
        "If necessary, we can repeat Steps 4.2.1-4.2.7 to continue the iterative process of incorporating feedback and making improvements.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.7): '{step_4_2_7_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Review the process and determine if repeating Steps 4.2.1-4.2.7 is necessary.\n"
        "- Continue the iterative process of incorporating feedback and making improvements as needed.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Assess if there's a need to repeat the steps for further refinement.\n"
        "- If necessary, start again from Step 4.2.1 to further refine the idea or prompt.\n"
    )

    FINALIZE_PROMPT_TMPL = (
        "Step 4.2.9: Evaluate and Analyze Success of Implementation\n"
        "--------------------------------------------------------\n"
        "In this final step of Step 4, let's evaluate and analyze the success of the overall implementation and its impact on the idea or prompt.\n"
        "--------------------------------------------------------\n"
        "Previous Step Output (Step 4.2.8): '{step_4_2_8_output}'\n"
        "Vocabulary Deconstructor's Context {vd_context_str}:\n"
        "- Evaluate the overall success of the implementation.\n"
        "- Analyze its impact on the idea or prompt.\n"
        "Target Structure's Context {ts_context_str}:\n"
        "- Assess the effectiveness of the entire process.\n"
        "- Determine if the desired impact has been achieved.\n"
    )

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"EvolutionTemplates.{self.name}"
