from supabase import create_client
import plotly.graph_objects as go

# Your Supabase Credentials (from your supabase-config.js)
url = "YOUR_SUPABASE_URL"
key = "YOUR_SUPABASE_ANON_KEY"
supabase = create_client(url, key)

def run_and_save_analysis(user_id, bill_amount):
    # 1. Run the math
    units = round(bill_amount / 6.5, 2)
    community_data = [120, 450, 310, 680]
    better_than = sum(1 for val in community_data if val > units)
    
    # 2. Build the chart (The instructions)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Neighbor A", "Neighbor B", "Neighbor C", "Neighbor D", "YOU"],
        y=community_data + [units],
        marker_color=['#d0dce0', '#d0dce0', '#d0dce0', '#d0dce0', '#133b2c']
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300)

    # 3. Pack the box
    analysis_results = {
        "units": units,
        "rank": f"Leading {better_than} neighbors in efficiency.",
        "chart_json": fig.to_json()
    }

    # 4. Save to Supabase
    supabase.table("profiles").update({"latest_analysis": analysis_results}).eq("id", user_id).execute()
    return "Analysis saved successfully!"