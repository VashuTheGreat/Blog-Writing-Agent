import logging
import asyncio
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from src.models.State_model import State
from src.graph.nodes.router_node import router_node,route_next
from src.graph.nodes.reducer_node import reducer_node
from src.graph.nodes.search_node import research_node
from src.graph.nodes.orchaster_node import orchestrator_node
from src.graph.nodes.worker_node import worker_node
from src.graph.nodes.fanout_node import fanout
load_dotenv()

g = StateGraph(State)
g.add_node("router", router_node)
g.add_node("research", research_node)
g.add_node("orchestrator", orchestrator_node)
g.add_node("worker", worker_node)
g.add_node("reducer", reducer_node)

g.add_edge(START, "router")
g.add_conditional_edges("router", route_next, {"research": "research", "orchestrator": "orchestrator"})
g.add_edge("research", "orchestrator")

g.add_conditional_edges("orchestrator", fanout, ["worker"])
g.add_edge("worker", "reducer")
g.add_edge("reducer", END)

app = g.compile()


png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)
async def run(topic: str):
    logging.info(f"Starting blog generation for topic: {topic}")
    try:
        out = await app.ainvoke(
            {
                "topic": topic,
                "mode": "",
                "needs_research": False,
                "queries": [],
                "evidence": [],
                "plan": None,
                "sections": [],
                "final": "",
            }
        )
        logging.info("Blog generation completed successfully")
        return out
    except Exception as e:
        logging.error(f"Error during graph execution: {str(e)}")
        raise

if __name__ == "__main__":
    from src.logger import *
    asyncio.run(run("State of Multimodal LLMs in 2026"))