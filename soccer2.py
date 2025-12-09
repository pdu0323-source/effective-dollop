import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Circle, Rectangle
import math

# =========================================================
# 1. 데이터 정의 (이전과 동일)
# =========================================================

TEAM_COLORS = {
    # --- 프리미어 리그 (2024/25 시즌 20개 팀) ---
    "Arsenal FC": ["#EF0107", "#00366E", "#FFFFFF"],
    "Aston Villa": ["#4F0024", "#95BFE5", "#67A6CC"],
    "AFC Bournemouth": ["#DA291C", "#000000", "#FFFFFF"],
    "Brentford FC": ["#E30613", "#000000", "#FFFFFF"],
    "Brighton & Hove Albion": ["#0057B8", "#FFFFFF", "#000000"],
    "Chelsea FC": ["#030948", "#FFFFFF", "#DA291C"],
    "Crystal Palace": ["#1B458F", "#A7A5A6", "#DA291C"],
    "Everton FC": ["#003399", "#FFFFFF", "#418A37"],
    "Fulham FC": ["#FFFFFF", "#000000", "#CC0000"],
    "Ipswich Town": ["#003E99", "#FFFFFF", "#CC0000"], 
    "Leicester City": ["#003090", "#FDBE11", "#FFFFFF"],
    "Liverpool FC": ["#C8102E", ["#00A389"], "#FFFFFF"],
    "Manchester City": ["#6CABDD", "#1C2C5B", "#FFFFFF"],
    "Manchester United": ["#DA291C", "#FBE122", "#000000"],
    "Newcastle United": ["#000000", "#FFFFFF", "#5BA8A6"],
    "Nottingham Forest": ["#E5323E", "#FFFFFF", "#000000"],
    "Southampton FC": ["#D71920", "#000000", "#FFFFFF"], 
    "Tottenham Hotspur": ["#FFFFFF", "#132257", "#CE1126"],
    "West Ham United": ["#7A263A", "#F3D45F", "#1BB190"],
    "Wolverhampton Wanderers": ["#FDB913", "#000000", "#101820"],

    # --- 유럽 및 기타 주요 리그 팀 ---
    "Real Madrid": ["#FFFFFF", "#005697", "#000000"],
    "FC Barcelona": ["#A50044", "#004D98", "#FDBE11"],
    "Atletico Madrid": ["#CB3524", "#FFFFFF", "#272D30"],
    "Real Betis": ["#008653", "#FFFFFF", "#964B00"],
    "Bayern Munich": ["#DC052D", "#FFFFFF", "#0066CC"],
    "Borussia Dortmund": ["#FDE100", "#000000", "#FFFFFF"],
    "Bayer Leverkusen": ["#E3221C", "#000000", "#FFFFFF"],
    "RB Leipzig": ["#001C53", "#FFD700", "#FFFFFF"],
    "Borussia Monchengladbach": ["#000000", "#FFFFFF", "#009045"], 
    "Paris Saint-Germain": ["#004A95", "#DA291C", "#FFFFFF"],
    "AS Monaco": ["#C5AA74", "#FFFFFF", "#E30613"],
    "Lille OSC": ["#004481", "#E63E3F", "#FFFFFF"], 
    "Olympique de Marseille": ["#00468C", "#FFFFFF", "#000000"], 
    "Juventus": ["#FFFFFF", "#000000", "#999999"],
    "Inter Milan": ["#004A95", "#FFFFFF", "#000000"],
    "AC Milan": ["#FF0000", "#000000", "#FFFFFF"],
    "AS Roma": ["#86273B", "#F5B41E", "#FFFFFF"],
    "Napoli": ["#007AC9", "#FFFFFF", "#123062"],
    "FC Seoul": ["#86242B", "#FFFFFF", "#000000"],
}

# =========================================================
# 2. 추상화 디자인 생성 함수 (Generative Art Function)
# =========================================================

def generate_complex_abstract_art(ax, colors):
    """
    주어진 색상 배열을 사용하여 복잡한 선과 원형의 추상화 이미지를 생성합니다.
    """
    C1, C2, C3 = colors # 메인, 보조, 배경색
    color_palette = [C1, C2, C3]
    
    # 캔버스 배경색 설정 (대비가 가장 잘 되는 색을 배경으로)
    ax.set_facecolor(C3) 
    
    # --- 1. 배경에 부드러운 사각형 배치 (배경 레이어) ---
    num_bg_rects = 5
    for _ in range(num_bg_rects):
        x = random.uniform(-1, 10)
        y = random.uniform(-1, 10)
        width = random.uniform(3, 8)
        height = random.uniform(3, 8)
        ax.add_patch(Rectangle((x, y), width, height, 
                               facecolor=random.choice(color_palette), 
                               alpha=random.uniform(0.1, 0.3), edgecolor='none'))

    # --- 2. 중심부에 원형 패턴 생성 (중앙 레이어) ---
    num_circles = 50
    center_x, center_y = 5, 5 
    
    for _ in range(num_circles):
        # 중심 주변에 군집하도록 난수 생성
        r = random.uniform(0.1, 4.0)
        theta = random.uniform(0, 2 * math.pi)
        x = center_x + r * math.cos(theta) * random.uniform(0.5, 1.5)
        y = center_y + r * math.sin(theta) * random.uniform(0.5, 1.5)
        
        radius = random.uniform(0.1, 0.8)
        
        ax.add_patch(Circle((x, y), radius, 
                            facecolor=random.choice([C1, C2]), 
                            alpha=random.uniform(0.4, 0.8), 
                            edgecolor=random.choice([C1, C2, C3]), 
                            linewidth=random.uniform(0.5, 2.0)))

    # --- 3. 복잡한 선 패턴 추가 (최상위 레이어) ---
    num_lines = 10
    
    for _ in range(num_lines):
        x_start = random.uniform(0, 10)
        y_start = random.uniform(0, 10)
        x_end = random.uniform(0, 10)
        y_end = random.uniform(0, 10)
        
        ax.plot([x_start, x_end], [y_start, y_end], 
                color=random.choice(color_palette), 
                linewidth=random.uniform(1.0, 4.0), 
                linestyle=random.choice(['-', '--', '-.']), 
                alpha=random.uniform(0.5, 1.0))
        
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off') 
    plt.tight_layout()

# =========================================================
# 3. Streamlit 앱 구성 (이전과 동일)
# =========================================================

def main():
    st.set_page_config(page_title="추상화 생성 예술", layout="wide")
    st.title("🎨 축구팀 색상을 활용한 추상화 생성 예술")
    st.markdown("팀 색상(데이터)을 기반으로 복잡하고 아름다운 패턴(생성 예술)을 만듭니다.")
    st.markdown("---")
    
    st.sidebar.header("🎨 생성 설정")
    
    team_list = sorted(TEAM_COLORS.keys())
    selected_team = st.sidebar.selectbox(
        "팀을 선택하세요:",
        team_list
    )
    
    # 패턴 유형 대신, 그림 스타일의 세밀함을 조정하는 옵션으로 대체 가능 (생략)
    st.sidebar.markdown("##### 현재는 단일 추상 스타일로 고정됩니다.")
    
    seed = st.sidebar.number_input(
        "Seed 입력 (숫자를 바꾸면 다른 작품이 생성됩니다)",
        min_value=1,
        max_value=10000,
        value=random.randint(1, 10000)
    )
    
    def get_league(team):
        pl_teams = ["Arsenal FC", "Aston Villa", "AFC Bournemouth", "Brentford FC", "Brighton & Hove Albion", "Chelsea FC", "Crystal Palace", "Everton FC", "Fulham FC", "Ipswich Town", "Leicester City", "Liverpool FC", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Southampton FC", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"]
        liga_teams = ["Real Madrid", "FC Barcelona", "Atletico Madrid", "Real Betis"]
        bundes_teams = ["Bayern Munich", "Borussia Dortmund", "Bayer Leverkusen", "RB Leipzig", "Borussia Monchengladbach"]
        ligue1_teams = ["Paris Saint-Germain", "AS Monaco", "Lille OSC", "Olympique de Marseille"]
        seriea_teams = ["Juventus", "Inter Milan", "AC Milan", "AS Roma", "Napoli"]
        
        if team in pl_teams: return "🏴󠁧󠁢󠁥󠁮󠁧󠁿 프리미어 리그"
        elif team in liga_teams: return "🇪🇸 라 리가"
        elif team in bundes_teams: return "🇩🇪 분데스리가"
        elif team in ligue1_teams: return "🇫🇷 리그 1"
        elif team in seriea_teams: return "🇮🇹 세리에 A"
        elif team == "FC Seoul": return "🇰🇷 K리그 1"
        else: return "기타 리그"

    if selected_team:
        league = get_league(selected_team)
        st.subheader(f"선택 팀: {selected_team} ({league})")
        
        colors_data = TEAM_COLORS[selected_team]
        
        st.subheader("사용된 팀 대표 색상 (HEX 코드)")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"**메인 색상:** `{colors_data[0]}`")
            st.markdown(f"<div style='background-color:{colors_data[0]}; height:30px; border-radius: 5px; border: 1px solid #ccc;'></div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"**보조 색상:** `{colors_data[1]}`")
            st.markdown(f"<div style='background-color:{colors_data[1]}; height:30px; border-radius: 5px; border: 1px solid #ccc;'></div>", unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"**배경/패턴 색상:** `{colors_data[2]}`")
            st.markdown(f"<div style='background-color:{colors_data[2]}; height:30px; border-radius: 5px; border: 1px solid #ccc;'></div>", unsafe_allow_html=True)

        st.markdown("---")

        st.subheader("생성된 추상화 작품 (Generative Art Output)")
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
            
        fig, ax = plt.subplots(figsize=(8, 8))
        generate_complex_abstract_art(ax, colors_data)
        
        st.pyplot(fig)
        
        st.markdown("---")
        col_dl, col_blank = st.columns([1, 4])
        
        with col_dl:
            file_name = f"{selected_team.replace(' ', '_')}_AbstractArt_{seed}.png"
            buf = fig.get_figure().canvas.buffer_rgba()
            
            st.download_button(
                label="🖼️ 작품 이미지 다운로드 (PNG)",
                data=buf.tobytes(),
                file_name=file_name,
                mime="image/png"
            )
        st.info("이 작품은 팀 색상을 기반으로 무작위로 위치, 크기, 투명도를 조정하여 생성된 복잡한 추상 디자인입니다. 'Seed'를 바꿔보세요.")


if __name__ == "__main__":
    main()
