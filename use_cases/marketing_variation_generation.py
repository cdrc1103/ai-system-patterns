from patterns.workflows.orchestrator_workers import FlexibleOrchestrator
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

ORCHESTRATOR_PROMPT = """
Analyze this task and break it down into 2-3 distinct approaches:

Task: {task}

Return your response in this format:

<analysis>
Explain your understanding of the task and which variations would be valuable.
Focus on how each approach serves different aspects of the task.
</analysis>

<tasks>
    <task>
    <type></type>
    <description></description>
    </task>
    <task>
    <type></type>
    <description></description>
    </task>
</tasks>
"""

WORKER_PROMPT = """
Generate content based on:
Task: {original_task}
Style: {task_type}
Guidelines: {task_description}

Return your response in this format:

<response>
Your content here, maintaining the specified style and fully addressing requirements.
</response>
"""


orchestrator = FlexibleOrchestrator(
    orchestrator_prompt=ORCHESTRATOR_PROMPT,
    worker_prompt=WORKER_PROMPT,
)

results = orchestrator.process(
    client=client,
    task="Write a product description for a new eco-friendly water bottle",
    context={
        "target_audience": "environmentally conscious millennials",
        "key_features": ["plastic-free", "insulated", "lifetime warranty"]
    }
)