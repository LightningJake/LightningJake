"""Generates the animated SVGs used in the profile README.

Run:  python scripts/generate_svgs.py
Outputs go to Assets/svg/. Edit the content constants below and re-run.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "Assets" / "svg"
OUT.mkdir(parents=True, exist_ok=True)

# Palette ("lightning" theme)
BG0, BG1 = "#0A0F1F", "#141C3A"
PANEL = "#0F1730"
BORDER = "#26304D"
GRID = "#1A2444"
TEXT = "#E6EDF3"
MUTED = "#8B95A7"
YELLOW = "#FACC15"
CYAN = "#22D3EE"
VIOLET = "#A78BFA"
GREEN = "#4ADE80"

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Code', Consolas, 'DejaVu Sans Mono', monospace"


def bolt(x, y, s=1.0, fill=YELLOW, cls=""):
    """A small lightning-bolt glyph drawn as a path (emoji render inconsistently in SVG)."""
    return (f'<path class="{cls}" transform="translate({x} {y}) scale({s})" fill="{fill}" '
            'd="M9 0 L0 15 H7 L4 28 L15 10 H8 L12 0 Z"/>')


def write(name, svg):
    (OUT / name).write_text(svg, encoding="utf-8")
    print("wrote", OUT / name)


# ---------------------------------------------------------------- banner
def banner():
    W, H = 1200, 320
    nodes = [  # label, x, y, color, glow delay (s)
        ("query", 740, 78, CYAN, 0.0),
        ("retrieve", 895, 78, VIOLET, 0.45),
        ("generate", 1050, 78, YELLOW, 0.9),
        ("evaluate", 1050, 198, GREEN, 1.6),
        ("judge", 895, 198, VIOLET, 2.2),
    ]
    nw, nh = 112, 40
    edges = [
        "M852 98 H895", "M1007 98 H1050", "M1106 118 V198",
        "M1050 218 H1007", "M895 218 H852",
    ]
    css = f"""
    .fade {{ opacity: 0; animation: fadeUp .9s ease-out forwards; }}
    .d1 {{ animation-delay: .1s }} .d2 {{ animation-delay: .3s }} .d3 {{ animation-delay: .5s }}
    .d4 {{ animation-delay: .7s }} .d5 {{ animation-delay: .9s }} .d6 {{ animation-delay: 1.1s }}
    @keyframes fadeUp {{ from {{ opacity: 0; transform: translateY(10px) }} to {{ opacity: 1; transform: none }} }}
    .flow {{ stroke-dasharray: 5 7; animation: flow 1s linear infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset: -12 }} }}
    .halo {{ opacity: 0; animation: halo 3s ease-out infinite; }}
    @keyframes halo {{ 0% {{ opacity: 0 }} 6% {{ opacity: .55 }} 30% {{ opacity: 0 }} 100% {{ opacity: 0 }} }}
    .flicker {{ animation: flicker 3.5s infinite; }}
    @keyframes flicker {{ 0%,100% {{ opacity: 1 }} 46% {{ opacity: 1 }} 48% {{ opacity: .25 }} 50% {{ opacity: 1 }} 52% {{ opacity: .4 }} 54% {{ opacity: 1 }} }}
    .pass {{ animation: pass 6s infinite; }} .review {{ animation: review 6s infinite; }}
    @keyframes pass {{ 0%,45% {{ opacity: 1 }} 50%,95% {{ opacity: 0 }} 100% {{ opacity: 1 }} }}
    @keyframes review {{ 0%,45% {{ opacity: 0 }} 50%,95% {{ opacity: 1 }} 100% {{ opacity: 0 }} }}
    .pulse {{ animation: pulse 2s ease-in-out infinite; }}
    @keyframes pulse {{ 0%,100% {{ opacity: 1 }} 50% {{ opacity: .3 }} }}
    """
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Jaimeet Sarode, AI Engineer">',
             f"<style>{css}</style>",
             f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{GRID}" stroke-width="1"/></pattern>
  <radialGradient id="glow" cx="0.78" cy="0.5" r="0.45"><stop offset="0" stop-color="{CYAN}" stop-opacity="0.16"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
  <radialGradient id="glow2" cx="0.05" cy="0.1" r="0.4"><stop offset="0" stop-color="{YELLOW}" stop-opacity="0.10"/><stop offset="1" stop-color="{YELLOW}" stop-opacity="0"/></radialGradient>
  <linearGradient id="nameg" x1="0" x2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C7D2FE"/></linearGradient>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>""",
             '<g clip-path="url(#clip)">',
             f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
             f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity=".55"/>',
             f'<rect width="{W}" height="{H}" fill="url(#glow)"/>',
             f'<rect width="{W}" height="{H}" fill="url(#glow2)"/>']

    # left text block
    parts.append(f'<g class="fade d1">{bolt(64, 62, 0.85, cls="flicker")}'
                 f'<text x="86" y="83" font-family="{MONO}" font-size="15" letter-spacing="3" fill="{YELLOW}" font-weight="700">LIGHTNINGJAKE</text></g>')
    parts.append(f'<text class="fade d2" x="62" y="148" font-family="{SANS}" font-size="58" font-weight="800" fill="url(#nameg)">Jaimeet Sarode</text>')
    parts.append(f'<text class="fade d3" x="64" y="190" font-family="{SANS}" font-size="20" font-weight="600" fill="{CYAN}">AI Engineer  ·  LLM Evaluation  ·  RAG  ·  Observability</text>')
    parts.append(f'<text class="fade d4" x="64" y="228" font-family="{SANS}" font-size="16" fill="{MUTED}">I build the systems that tell you whether your AI is actually right.</text>')
    pills = [("Mumbai, India", TEXT), ("AI Engineer @ Capgemini", YELLOW), ("Azure AI-102 certified", CYAN)]
    px = 64
    pill_svg = []
    for label, col in pills:
        w = int(len(label) * 7.9 + 28)
        pill_svg.append(f'<rect x="{px}" y="252" width="{w}" height="30" rx="15" fill="{PANEL}" stroke="{BORDER}"/>'
                        f'<circle cx="{px + 14}" cy="267" r="3.5" fill="{col}"/>'
                        f'<text x="{px + 24}" y="272" font-family="{MONO}" font-size="12.5" fill="{TEXT}">{escape(label)}</text>')
        px += w + 10
    parts.append(f'<g class="fade d5">{"".join(pill_svg)}</g>')

    # right: animated RAG + eval pipeline
    g = ['<g class="fade d6">']
    g.append(f'<text x="740" y="58" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">RAG · EVAL PIPELINE</text>')
    for d in edges:
        g.append(f'<path class="flow" d="{d}" stroke="{MUTED}" stroke-width="2" fill="none"/>')
    # travelling packet (drawn under the nodes)
    g.append(f'<circle r="5" fill="{YELLOW}"><animateMotion dur="3s" repeatCount="indefinite" path="M796 98 H1106 V218 H796"/></circle>')
    for label, x, y, col, delay in nodes:
        g.append(f'<rect class="halo" style="animation-delay:{delay}s" x="{x - 4}" y="{y - 4}" width="{nw + 8}" height="{nh + 8}" rx="13" fill="none" stroke="{col}" stroke-width="4"/>')
        g.append(f'<rect x="{x}" y="{y}" width="{nw}" height="{nh}" rx="10" fill="{PANEL}" stroke="{col}" stroke-width="1.5"/>')
        g.append(f'<text x="{x + nw / 2}" y="{y + 25}" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{TEXT}">{label}</text>')
    # verdict pill that alternates PASS / HUMAN REVIEW
    vx, vy = 740, 198
    g.append(f'<rect class="halo" style="animation-delay:2.7s" x="{vx - 4}" y="{vy - 4}" width="{nw + 8}" height="{nh + 8}" rx="13" fill="none" stroke="{GREEN}" stroke-width="4"/>')
    g.append(f'<g class="pass"><rect x="{vx}" y="{vy}" width="{nw}" height="{nh}" rx="20" fill="#0E2A1C" stroke="{GREEN}" stroke-width="1.5"/>'
             f'<text x="{vx + nw / 2}" y="{vy + 25}" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="{GREEN}">✓ PASS</text></g>')
    g.append(f'<g class="review"><rect x="{vx}" y="{vy}" width="{nw}" height="{nh}" rx="20" fill="#2A240B" stroke="{YELLOW}" stroke-width="1.5"/>'
             f'<text x="{vx + nw / 2}" y="{vy + 25}" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="{YELLOW}">⚑ REVIEW</text></g>')
    g.append(f'<circle class="pulse" cx="746" cy="281" r="4" fill="{GREEN}"/>'
             f'<text x="758" y="285" font-family="{MONO}" font-size="12" fill="{MUTED}">every step traced · Langfuse + OpenTelemetry</text>')
    g.append("</g>")
    parts += g
    parts.append("</g>")
    parts.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="{BORDER}"/>')
    parts.append("</svg>")
    write("banner.svg", "\n".join(parts))


# -------------------------------------------------------------- terminal
def terminal():
    LOOP = 20.0          # seconds per loop
    W = 900
    LH = 27
    TOP = 84
    X = 30
    CW = 9.2             # generous monospace char width, so the typing cover always clears the text

    P = ("❯ ", YELLOW)
    # (kind, start_s, spans) — kind "cmd" is typed, "out" fades in
    lines = [
        ("cmd", 0.6, [("whoami", TEXT)]),
        ("out", 1.5, [("Jaimeet Sarode · AI Engineer @ Capgemini · Mumbai, India", MUTED)]),
        ("cmd", 2.4, [("cat ./focus.txt", TEXT)]),
        ("out", 3.5, [("LLM evaluation · RAG systems · LLM observability · agents", CYAN)]),
        ("cmd", 4.5, [("python -m evals run --suite rag-golden", TEXT)]),
        ("out", 6.6, [("[retrieval ] ", VIOLET), ("context_precision   ....... ", MUTED), ("PASS", GREEN)]),
        ("out", 7.0, [("[retrieval ] ", VIOLET), ("context_recall      ....... ", MUTED), ("PASS", GREEN)]),
        ("out", 7.4, [("[generation] ", VIOLET), ("factual_correctness ....... ", MUTED), ("PASS", GREEN)]),
        ("out", 7.8, [("[generation] ", VIOLET), ("semantic_similarity ....... ", MUTED), ("PASS", GREEN)]),
        ("out", 8.4, [("[judge     ] ", VIOLET), ("llm_as_a_judge      ....... ", MUTED), ("HUMAN REVIEW", YELLOW)]),
        ("out", 9.2, [("✓ ", GREEN), ("report saved · every evaluator traced in Langfuse", TEXT)]),
        ("cmd", 10.0, []),
    ]
    H = TOP + LH * len(lines) + 12

    def pct(t):
        return f"{min(100.0, t / LOOP * 100):.2f}%"

    css = [f"""
    text {{ font-family: {MONO}; font-size: 15px; white-space: pre; }}
    .all {{ animation: all {LOOP}s linear infinite; }}
    @keyframes all {{ 0%, 95% {{ opacity: 1 }} 99%, 100% {{ opacity: 0 }} }}
    .cursor {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0 }} }}
    """]
    body = []
    for i, (kind, t, spans) in enumerate(lines):
        y = TOP + i * LH
        tsp = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in spans)
        n = sum(len(s) for s, _ in spans)
        if kind == "cmd":
            # prompt shows up with the line; command text is revealed by sliding a cover to the right
            css.append(f"@keyframes s{i} {{ 0%, {pct(t - 0.01)} {{ opacity: 0 }} {pct(t)}, 100% {{ opacity: 1 }} }}"
                       f" .s{i} {{ animation: s{i} {LOOP}s linear infinite; }}")
            body.append(f'<g class="s{i}"><text x="{X}" y="{y}"><tspan fill="{P[1]}">{P[0]}</tspan>{tsp}</text>')
            if n:
                dur = max(0.4, n * 0.045)
                width = n * CW + 10
                css.append(f"@keyframes c{i} {{ 0%, {pct(t)} {{ transform: translateX(0) }} {pct(t + dur)}, 100% {{ transform: translateX({width:.0f}px) }} }}"
                           f" .c{i} {{ animation: c{i} {LOOP}s steps(1) infinite; animation-timing-function: steps({n}, end); }}")
                body.append(f'<rect class="c{i}" x="{X + 2 * CW - 2}" y="{y - 18}" width="{W}" height="{LH}" fill="{BG0}"/>')
            else:
                body.append(f'<rect class="cursor" x="{X + 2 * CW}" y="{y - 15}" width="9" height="19" fill="{TEXT}"/>')
            body.append("</g>")
        else:
            css.append(f"@keyframes o{i} {{ 0%, {pct(t)} {{ opacity: 0; transform: translateX(-6px) }} {pct(t + 0.25)}, 100% {{ opacity: 1; transform: none }} }}"
                       f" .o{i} {{ animation: o{i} {LOOP}s ease-out infinite; }}")
            body.append(f'<text class="o{i}" x="{X + 2 * CW}" y="{y}">{tsp}</text>')

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Animated terminal: whoami, focus areas and an LLM evaluation run">',
           f"<style>{''.join(css)}</style>",
           f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{BG0}" stroke="{BORDER}"/>',
           f'<path d="M14 .5 H{W - 14} A13.5 13.5 0 0 1 {W - .5} 14 V42 H.5 V14 A13.5 13.5 0 0 1 14 .5 Z" fill="#111933"/>',
           f'<line x1=".5" y1="42" x2="{W - .5}" y2="42" stroke="{BORDER}"/>',
           '<circle cx="24" cy="21" r="6" fill="#FF5F57"/><circle cx="44" cy="21" r="6" fill="#FEBC2E"/><circle cx="64" cy="21" r="6" fill="#28C840"/>',
           f'<text x="{W / 2}" y="26" text-anchor="middle" style="font-size:13px" fill="{MUTED}">jaimeet@mumbai: ~/evals</text>',
           '<g class="all">', *body, "</g>", "</svg>"]
    write("terminal.svg", "\n".join(svg))


# ---------------------------------------------------------- project cards
PROJECTS = [
    dict(file="card-jfuse.svg", name="jfuse", eyebrow="LLM OBSERVABILITY", accent=YELLOW,
         desc=["Local LLM observability for any Python app:",
               "tracing SDK, prompt management, ingestion",
               "server and web UI on SQLite. OTel-compatible."],
         tags=["Python", "OpenTelemetry", "SQLite"]),
    dict(file="card-amppilot.svg", name="AmpPilot", eyebrow="TOP 33 · INFOSYS GLOBAL HACKATHON", accent=CYAN,
         desc=["AI-powered EV platform: smart routing,",
               "battery health, ML occupancy prediction and",
               "geospatial charging-gap analysis."],
         tags=["FastAPI", "scikit-learn", "Shapely"]),
    dict(file="card-attendie.svg", name="Attendie AI", eyebrow="PATENT PUBLISHED", accent=VIOLET,
         desc=["Real-time multilingual meeting transcription",
               "and summaries with OpenAI Whisper. Cut",
               "minute-taking effort by 50%."],
         tags=["Whisper", "NLP", "Python"]),
    dict(file="card-portipark.svg", name="PortiPark", eyebrow="FULL-STACK", accent=GREEN,
         desc=["Office parking reservations on an interactive",
               "floor grid: book, manage and check in to",
               "parking spots, with JWT auth."],
         tags=["FastAPI", "PostgreSQL", "React + TS"]),
]


def card(p):
    W, H = 420, 200
    a = p["accent"]
    css = f"""
    .sweep {{ animation: sweep 5s ease-in-out infinite; }}
    @keyframes sweep {{ 0% {{ transform: translateX(-160px) }} 60%, 100% {{ transform: translateX({W + 160}px) }} }}
    """
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(p["name"])}">',
             f"<style>{css}</style>",
             f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
  <linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="16"/></clipPath>
</defs>""",
             '<g clip-path="url(#clip)">',
             f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
             f'<rect width="{W}" height="4" fill="{a}"/>',
             f'<rect class="sweep" x="0" y="0" width="140" height="{H}" fill="url(#shine)" transform="skewX(-20)"/>',
             "</g>",
             f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="{BORDER}"/>',
             f'<text x="24" y="38" font-family="{MONO}" font-size="11.5" letter-spacing="1.5" fill="{a}" font-weight="700">{escape(p["eyebrow"])}</text>',
             f'<text x="24" y="70" font-family="{SANS}" font-size="25" font-weight="800" fill="{TEXT}">{escape(p["name"])}</text>',
             f'<text x="{W - 24}" y="70" text-anchor="end" font-family="{SANS}" font-size="20" fill="{MUTED}">↗</text>']
    for i, line in enumerate(p["desc"]):
        parts.append(f'<text x="24" y="{100 + i * 21}" font-family="{SANS}" font-size="14.5" fill="{MUTED}">{escape(line)}</text>')
    tx = 24
    for t in p["tags"]:
        w = int(len(t) * 7.4 + 22)
        parts.append(f'<rect x="{tx}" y="160" width="{w}" height="24" rx="12" fill="{PANEL}" stroke="{BORDER}"/>'
                     f'<text x="{tx + w / 2}" y="176" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{TEXT}">{escape(t)}</text>')
        tx += w + 8
    parts.append("</svg>")
    write(p["file"], "\n".join(parts))


# ------------------------------------------------------------------ footer
def footer():
    W, H = 1200, 140
    css = """
    .w1 { animation: w 8s ease-in-out infinite alternate; }
    .w2 { animation: w 6s ease-in-out infinite alternate-reverse; }
    @keyframes w { from { transform: translateX(0) } to { transform: translateX(-120px) } }
    .flicker { animation: flicker 3.5s infinite; }
    @keyframes flicker { 0%,100%,46% { opacity: 1 } 48% { opacity: .25 } 50% { opacity: 1 } 52% { opacity: .4 } 54% { opacity: 1 } }
    """

    def wave(y, amp, period=240):
        d = f"M0 {y}"
        x = 0
        while x < W + 240:
            d += f" q{period / 4} {-amp} {period / 2} 0 t{period / 2} 0"
            x += period
        return d + f" V{H} H0 Z"

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Thanks for stopping by">',
             f"<style>{css}</style>",
             f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG0}"/></linearGradient>'
             f'<clipPath id="fc"><rect width="{W}" height="{H}" rx="20"/></clipPath></defs>',
             '<g clip-path="url(#fc)">',
             f'<path class="w1" d="{wave(70, 18)}" fill="{CYAN}" opacity=".12"/>',
             f'<path class="w2" d="{wave(82, 14, 300)}" fill="{YELLOW}" opacity=".10"/>',
             f'<path class="w1" d="{wave(92, 10, 200)}" fill="url(#g)"/>',
             "</g>",
             bolt(352, 105, 0.7, cls="flicker"),
             f'<text x="{W / 2 + 10}" y="124" text-anchor="middle" font-family="{SANS}" font-size="17" font-weight="600" fill="{TEXT}">Thanks for stopping by. Let\'s build AI you can trust.</text>',
             "</svg>"]
    write("footer.svg", "\n".join(parts))


if __name__ == "__main__":
    banner()
    terminal()
    for p in PROJECTS:
        card(p)
    footer()
