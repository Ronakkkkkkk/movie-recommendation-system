import requests
import streamlit as st

# ==============================================================================
# CONFIG & INITIALIZATION
# ==============================================================================
API_BASE = "https://movie-recommendation-system-2-1b3z.onrender.com"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="THE VAULT // Cinema Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# MODERN OBSIDIAN DESIGN SYSTEM (CSS)
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

/* --- ZERO out Streamlit native Chrome header elements --- */
header, [data-testid="stHeader"] {
    background: transparent !important;
    background-color: transparent !important;
    height: 0px !important;
    display: none !important;
}
/* Force permanent dark background over everything to fix theme blending */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: #06080F !important;
    color: #F3F4F6 !important;
}
.block-container {
    padding: 3.5rem 4rem !important;
    max-width: 1500px !important;
}

/* --- BRANDING HEADER FIX --- */
.brand-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #1E293B;
    margin-bottom: 2rem;
}
.brand-logo {
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: flex;
    align-items: center;
    gap: 10px;
}
.brand-tag {
    font-size: 0.75rem;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* --- SVG ICON INLINES --- */
.svg-icon {
    width: 20px;
    height: 20px;
    fill: none;
    stroke: currentColor;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    display: inline-block;
    vertical-align: middle;
}
.svg-gold { color: #F59E0B; }
.svg-brand { color: #6366F1; }

/* --- NAVBAR CAT PILLS --- */
.nav-pill-box {
    display: flex;
    gap: 12px;
    margin-bottom: 2rem;
    background: #0F172A;
    padding: 8px;
    border-radius: 16px;
    border: 1px solid #1E293B;
    width: fit-content;
}

/* --- INPUTS & TEXT AREAS --- */
div[data-testid="stTextInput"] label {
    display: none !important;
}
div[data-testid="stTextInput"] input {
    color: #F8FAFC !important;
    -webkit-text-fill-color: #F8FAFC !important;
    background-color: #0F172A !important;
    border: 1px solid #1E293B !important;
    border-radius: 14px !important;
    padding: 0.85rem 1.4rem !important;
    font-size: 1rem !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #6366F1 !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
}

div[data-testid="stSelectbox"] > div > div {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
    border: 1px solid #1E293B !important;
    border-radius: 12px !important;
}

/* --- CARD STRUCTURES --- */
.grid-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
}
.movie-card {
    background: #0F172A;
    border: 1px solid #1E293B;
    border-radius: 16px;
    padding: 12px;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    margin-bottom: 0.75rem;
}
.movie-card:hover {
    transform: translateY(-5px);
    border-color: #4F46E5;
    box-shadow: 0 12px 30px rgba(79, 70, 229, 0.15);
}
.movie-poster-wrapper img {
    border-radius: 10px !important;
    object-fit: cover !important;
}
.movie-title {
    font-size: 0.95rem;
    font-weight: 600;
    color: #F1F5F9;
    line-height: 1.4;
    height: 2.8rem;
    overflow: hidden;
    margin: 12px 0 6px 0;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}

/* --- BUTTON EXTENSIONS --- */
.stButton > button {
    background: #1E293B !important;
    color: #E2E8F0 !important;
    border: 1px solid transparent !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
}

/* --- MOVIE DETAILS HERO BLOCKS --- */
.hero-card {
    background: linear-gradient(180deg, #0F172A 0%, #090D16 100%);
    border: 1px solid #1E293B;
    border-radius: 24px;
    padding: 2.5rem;
    margin-bottom: 2rem;
}
.meta-badge {
    background-color: #1E293B;
    color: #94A3B8;
    padding: 4px 12px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 8px;
    border: 1px solid #334155;
}
.section-header {
    font-size: 1.25rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #F8FAFC;
    margin: 2rem 0 1rem 0;
    border-left: 4px solid #4F46E5;
    padding-left: 12px;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# ROUTING & STATES
# ==============================================================================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None
if "home_cat" not in st.session_state:
    st.session_state.home_cat = "trending"

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except ValueError:
        pass

def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()

def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()

# ==============================================================================
# API REQUEST PLUGINS
# ==============================================================================
@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}"
        return r.json(), None
    except Exception as e:
        return None, str(e)

def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()
    raw_items = []

    if isinstance(data, dict) and "results" in data:
        for m in data.get("results") or []:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if title and tmdb_id:
                raw_items.append({
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                })
    elif isinstance(data, list):
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            if title and tmdb_id:
                raw_items.append({
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": m.get("poster_url"),
                    "release_date": m.get("release_date", ""),
                })
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards

def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append({
                "tmdb_id": tmdb["tmdb_id"],
                "title": tmdb.get("title") or x.get("title") or "Untitled",
                "poster_url": tmdb.get("poster_url"),
            })
    return cards

# ==============================================================================
# UNIFORM CORE GRID PLATFORM (Hardcoded 6 Columns)
# ==============================================================================
def safe_poster(poster):
    if isinstance(poster, str) and poster.strip() and poster.startswith("http"):
        return poster
    return "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=300&auto=format&fit=crop"

def poster_grid(cards, key_prefix="grid"):
    if not cards:
        st.info("No films match this configuration. Try adjusting your selection.")
        return

    cols = 6  # Fixed and structured layout column distribution matrix
    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols, gap="medium")
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                st.markdown('<div class="grid-container"><div class="movie-card">', unsafe_allow_html=True)
                st.markdown('<div class="movie-poster-wrapper">', unsafe_allow_html=True)
                if isinstance(poster, str) and poster.strip():
                    st.image(safe_poster(poster), use_container_width=True)
                else:
                    st.image("https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=300&auto=format&fit=crop", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Explore", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}", use_container_width=True):
                    if tmdb_id:
                        goto_details(tmdb_id)
                st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# IMMERSIVE BRAND HEADER (Fixed padding and SVG assets)
# ==============================================================================
film_icon_svg = '<svg class="svg-icon svg-brand" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>'
shield_icon_svg = '<svg class="svg-icon" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'

st.markdown(f"""
<div class="brand-container">
    <div class="brand-logo">{film_icon_svg} THE VAULT</div>
    <div class="brand-tag">{shield_icon_svg} Cinematic Discovery Platform</div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# DISPLAY BLOCK ROUTER: HOME CHANNELS
# ==============================================================================
if st.session_state.view == "home":
    # 1. Inline Premium Top Navbar Category Selector Blocks
    CATS = {"trending": "Trending Now", "popular": "Most Popular", "top_rated": "Top Rated", "now_playing": "In Theaters"}
    
    st.markdown('<div class="nav-pill-box">', unsafe_allow_html=True)
    pill_cols = st.columns(len(CATS))
    for i, (key, label) in enumerate(CATS.items()):
        with pill_cols[i]:
            # Simple active state visual indicator marker prefix text string
            btn_label = f"● {label}" if st.session_state.home_cat == key else label
            if st.button(btn_label, key=f"nav_pill_{key}"):
                st.session_state.home_cat = key
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Immersive Search Entry Form Block
    typed = st.text_input(
        "Search Matrix Input", 
        placeholder="Type a movie title to scan metadata clusters..."
    )

    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Enter 2 or more characters to trigger search analytics pipelines.")
        else:
            with st.spinner("Processing network queries..."):
                data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search engine communication failure: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

                if suggestions:
                    labels = ["-- Choose Indexed Movie Result --"] + [s[0] for s in suggestions]
                    selected = st.selectbox("Direct Match Indexes Found", labels, index=0)

                    if selected != "-- Choose Indexed Movie Result --":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                
                st.markdown("<div class='section-header'>Search Results Map</div>", unsafe_allow_html=True)
                poster_grid(cards, key_prefix="search_results")
        st.stop()

    # 3. Primary Dashboard Feed Matrix Hydration Setup
    current_active_cat = st.session_state.home_cat
    st.markdown(f"<div class='section-header'>Featured Stream Engine Engine // {CATS[current_active_cat]}</div>", unsafe_allow_html=True)

    with st.spinner("Hydrating data arrays..."):
        home_cards, err = api_get_json("/home", params={"category": current_active_cat, "limit": 24})
        
    if err or not home_cards:
        st.error(f"Failed to query category cache frames: {err or 'Unknown Object Specification'}")
        st.stop()

    poster_grid(home_cards, key_prefix="home_feed")

# ==============================================================================
# DISPLAY BLOCK ROUTER: MOVIE ANALYSIS LAYER
# ==============================================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("State pointer missing structural runtime parameters.")
        if st.button("← Back to Hub"):
            goto_home()
        st.stop()

    # Back Navigation Control Bar Row with Inline SVG Chevron
    back_arrow_svg = '<svg class="svg-icon" style="width:14px; height:14px; margin-right:4px;" viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>'
    if st.button(f"Home", key="back_to_hub_btn"):
        goto_home()

    with st.spinner("Reconstructing movie elements..."):
        data, err = api_get_json(f"/movie/id/{tmdb_id}")
        
    if err or not data:
        st.error(f"Fatal metadata asset acquisition error: {err or 'Corrupt Data Node Connection'}")
        st.stop()

    # Profile Sheet UI Blueprint Layout
    st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
    left, right = st.columns([1, 2.5], gap="large")

    with left:
        if data.get("poster_url"):
            st.image(data["poster_url"], use_container_width=True)
        else:
            st.info("Missing Poster Asset Reference")

    with right:
        st.markdown(f"<h1 style='margin-top:0; font-size:2.6rem; font-weight:800; letter-spacing:-0.04em;'>{data.get('title','')}</h1>", unsafe_allow_html=True)
        
        release = data.get("release_date") or "N/A"
        genres = data.get("genres", [])
        
        badge_html = f"<span class='meta-badge'>YEAR: {release[:4] if len(release)>=4 else release}</span>"
        for g in genres[:3]:
            badge_html += f"<span class='meta-badge'>{g['name'].upper()}</span>"
        st.markdown(badge_html, unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size:1.1rem; color:#94A3B8; margin-bottom:0.6rem;'>Story Synopsis</h3>", unsafe_allow_html=True)
        st.write(data.get("overview") or "No semantic abstract overview package exists for this title structure.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Secondary Content Block Recommendations Frame
    star_icon_svg = '<svg class="svg-icon svg-gold" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
    st.markdown(f"<div class='section-header'>{star_icon_svg} Algorithmic Recommendations</div>", unsafe_allow_html=True)

    title_query = (data.get("title") or "").strip()
    if title_query:
        with st.spinner("Computing algorithmic vector projections..."):
            bundle, err2 = api_get_json(
                "/movie/search",
                params={"query": title_query, "tfidf_top_n": 12, "genre_limit": 12},
            )

        if not err2 and bundle:
            st.markdown("<p style='color:#6366F1; font-weight:600; font-size:1rem; margin-top:1.5rem;'>TF-IDF Similarity Map</p>", unsafe_allow_html=True)
            poster_grid(
                to_cards_from_tfidf_items(bundle.get("tfidf_recommendations")),
                key_prefix="details_tfidf",
            )

            st.markdown("<p style='color:#A855F7; font-weight:600; font-size:1rem; margin-top:2rem;'>Genre-Based Matches</p>", unsafe_allow_html=True)
            poster_grid(
                bundle.get("genre_recommendations", []),
                key_prefix="details_genre",
            )
        else:
            st.info("System fallback sequence activated. Compiling target nodes via single descriptor vectors.")
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                poster_grid(genre_only, key_prefix="details_genre_fallback")
            else:
                st.warning("Vector structural calculations yielded an empty neighborhood list array.")
    else:
        st.warning("Insufficient title string payload to verify multi-label feature classifications.")