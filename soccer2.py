import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Polygon # 다각형 (유니폼 형태)
from matplotlib.patches import Rectangle, Circle

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
    "Liverpool FC": ["#C8102E", "#00A389", "#FFFFFF"],
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
# 2. 정면 유니폼 생성 함수 (Generative Art Function)
# =========================================================

def draw_uniform(ax, colors, pattern_type):
    """
    정면 시점으로 유니폼 디자인을 생성합니다.
    """
    C1, C2, C3 = colors # 메인, 보조, 패턴/배경색
    
    shirt_width = 12
    shirt_height = 14
    
    # 1. 유니폼 기본 형태 (다각형 사용)
    # 어깨선을 둥글게 표현
    shirt_coords = np.array([
        [-shirt_width/2, -shirt_height/2],  # 왼쪽 아래
        [shirt_width/2, -shirt_height/2],   # 오른쪽 아래
        [shirt_width/2, shirt_height/2 - 2],   # 오른쪽 어깨 아래
        [shirt_width/2 - 2.5, shirt_height/2 + 1], # 오른쪽 어깨 끝
        [2, shirt_height/2 + 2],                # 오른쪽 카라
        [-2, shirt_height/2 + 2],               # 왼쪽 카라
        [-shirt_width/2 + 2.5, shirt_height/2 + 1], # 왼쪽 어깨 끝
        [-shirt_width/2, shirt_height/2 - 2],   # 왼쪽 어깨 아래
    ])
    
    ax.add_patch(Polygon(shirt_coords, closed=True, 
                         facecolor=C1, edgecolor='black', linewidth=1.5))

    # 2. 소매 (팔꿈치 부분만 보이도록)
    sleeve_width = 3
    sleeve_height = 1.5
    sleeve_offset_y = shirt_height/2 - 3 
    
    # 왼쪽 소매
    ax.add_patch(Rectangle((-shirt_width/2 - sleeve_width/2, sleeve_offset_y - sleeve_height/2), 
                           sleeve_width, sleeve_height, facecolor=C1, edgecolor='black', linewidth=1.5))
    ax.add_patch(Rectangle((-shirt_width/2 - sleeve_width/2, sleeve_offset_y - sleeve_height/2), 
                           sleeve_width, sleeve_height, facecolor=C2, edgecolor='none', linewidth=0, alpha=0.3)) # 색상 디테일
    
    # 오른쪽 소매
    ax.add_patch(Rectangle((shirt_width/2 - sleeve_width/2, sleeve_offset_y - sleeve_height/2), 
                           sleeve_width, sleeve_height, facecolor=C1, edgecolor='black', linewidth=1.5))
    ax.add_patch(Rectangle((shirt_width/2 - sleeve_width/2, sleeve_offset_y - sleeve_height/2), 
                           sleeve_width, sleeve_height, facecolor=C2, edgecolor='none', linewidth=0, alpha=0.3)) # 색상 디테일

    # 3. 목 카라 (Collar)
    collar_width = 4.5
    collar_height = 1
    collar_y = shirt_height/2 + 1.5
    ax.add_patch(Rectangle((-collar_width/2, collar_y), collar_width, collar_height,
                           facecolor=C2, edgecolor='black', linewidth=1))

    # 4. 랜덤 패턴 생성 (Pattern Generation)
    
    # 패턴을 그릴 영역 (목 아래 몸통 부분)
    pattern_x_min, pattern_x_max = -shirt_width/2, shirt_width/2
    pattern_y_min, pattern_y_max = -shirt_height/2, shirt_height/2 + 0.5
    
    if pattern_type == "Stripe":
        # 세로 줄무늬
        num_stripes = random.randint(7, 15)
        stripe_width = shirt_width / num_stripes
        for i in range(num_stripes):
            if i % 2 != 0:
                ax.add_patch(Rectangle((pattern_x_min + i * stripe_width, pattern_y_min), stripe_width, pattern_y_max - pattern_y_min,
                                       facecolor=C2, alpha=0.9, edgecolor='none'))
    
    elif pattern_type == "Hoops":
        # 가로 줄무늬
        num_hoops = random.randint(5, 9)
        hoop_height = shirt_height / num_hoops
        for i in range(num_hoops):
            if i % 2 != 0:
                ax.add_patch(Rectangle((pattern_x_min, pattern_y_min + i * hoop_height), shirt_width, hoop_height,
                                       facecolor=C2, alpha=0.9, edgecolor='none'))

    elif pattern_type == "Dots":
        # 도트 패턴
        num_dots = random.randint(50, 100)
        dot_color = random.choice([C2, C3])
        for _ in range(num_dots):
            x = random.uniform(pattern_x_min + 0.5, pattern_x_max - 0.5)
            y = random.uniform(pattern_y_min + 0.5, pattern_y_max - 0.5)
            dot_radius = random.uniform(0.2, 0.5)
            ax.add_patch(Circle((x, y), dot_radius, facecolor=dot_color, alpha=0.7, edgecolor='none'))
            
    elif pattern_type == "Checkers":
        # 체크 패턴
        num_squares = random.randint(6, 12)
        square_size = shirt_width / num_squares
        checker_color = random.choice([C2, C3])
        for i in range(num_squares):
            for j in range(num_squares):
                # Y축 범위 조정: 패턴을 가슴 아래로 제한
                if (i + j) % 2 != 0:
                    x = pattern_x_min + i * square_size
                    y = pattern_y_min + j * square_size
                    ax.add_patch(Rectangle((x, y), square_size, square_size,
                                           facecolor=checker_color, alpha=0.7, edgecolor='none'))
    
    # 5. 로고 및 스폰서 영역 (패턴 위에 겹쳐서 그립니다)
    # 로고
    ax.add_patch(Circle((0, 4.5), 1.2, facecolor=C3, edgecolor=C2, linewidth=0.5, alpha=0.8)) 
    # 스폰서
    ax.add_patch(Rectangle((-3.5, 2.5), 7, 1.2, facecolor=C3, edgecolor=C2, linewidth=0.5, alpha=0.8)) 

# =========================================================
# 3. Streamlit 앱 구성 (이전과 동일)
# =========================================================

def main():
    st.set_page_config(page_title="유니폼 생성 예술", layout="wide")
    st.title("👕 데이터 기반 랜덤 유니폼 생성기")
    st.markdown("축구팀 색상을 활용하여 유니폼 패턴을 생성합니다. (생성 예술)")
    st.markdown("---")
    
    st.sidebar.header("🎨 유니폼 설정")
    
    team_list = sorted(TEAM_COLORS.keys())
    selected_team = st.sidebar.selectbox(
        "팀을 선택하세요:",
        team_list
    )
    
    pattern_options = ["Stripe", "Hoops", "Dots", "Checkers"]
    selected_pattern = st.sidebar.selectbox(
        "패턴 유형을 선택하세요:",
        pattern_options,
        index=random.randint(0, 3)
    )
    
    seed = st.sidebar.number_input(
        "Seed 입력 (숫자를 바꾸면 패턴의 디테일이 변경됩니다)",
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
            st.markdown(f"**패턴/배경 색상:** `{colors_data[2]}`")
            st.markdown(f"<div style='background-color:{colors_data[2]}; height:30px; border-radius: 5px; border: 1px solid #ccc;'></div>", unsafe_allow_html=True)

        st.markdown("---")

        st.subheader("생성된 랜덤 유니폼 (Generative Art Output)")
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
            
        fig, ax = plt.subplots(figsize=(7, 7))
        draw_uniform(ax, colors_data, selected_pattern)
        
        ax.set_xlim(-10, 10)
        ax.set_ylim(-8, 8)
        ax.axis('off')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        st.markdown("---")
        col_dl, col_blank = st.columns([1, 4])
        
        with col_dl:
            file_name = f"{selected_team.replace(' ', '_')}_uniform_{selected_pattern}_{seed}.png"
            buf = fig.get_figure().canvas.buffer_rgba()
            
            st.download_button(
                label="🖼️ 유니폼 이미지 다운로드 (PNG)",
                data=buf.tobytes(),
                file_name=file_name,
                mime="image/png"
            )


if __name__ == "__main__":
    main()
