import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Rectangle

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
    "Lille OSC": ["#004481", ["#E63E3F"], "#FFFFFF"], 
    "Olympique de Marseille": ["#00468C", "#FFFFFF", "#000000"], 
    "Juventus": ["#FFFFFF", "#000000", "#999999"],
    "Inter Milan": ["#004A95", "#FFFFFF", "#000000"],
    "AC Milan": ["#FF0000", "#000000", "#FFFFFF"],
    "AS Roma": ["#86273B", "#F5B41E", "#FFFFFF"],
    "Napoli": ["#007AC9", "#FFFFFF", "#123062"],
    "FC Seoul": ["#86242B", "#FFFFFF", "#000000"],
}

# =========================================================
# 2. 깃발 디자인 생성 함수 (Generative Art Function)
# =========================================================

def draw_flag(ax, colors, pattern_type):
    """
    주어진 색상과 패턴 타입으로 추상적인 깃발 디자인을 생성합니다.
    """
    C1, C2, C3 = colors # 메인, 보조, 패턴/배경색
    
    flag_width = 15
    flag_height = 10
    
    # 1. 깃발 기본 배경 (메인 색상)
    ax.add_patch(Rectangle((0, 0), flag_width, flag_height, 
                           facecolor=C1, edgecolor='black', linewidth=1.5))
    
    # 2. 랜덤 패턴 생성
    
    if pattern_type == "Vertical Stripe":
        # 세로 줄무늬 (Main/Secondary 색상 번갈아 사용)
        num_stripes = random.randint(3, 10)
        stripe_width = flag_width / num_stripes
        stripe_color_set = [C1, C2, C3]
        
        for i in range(num_stripes):
            color_index = (i + random.randint(0, 2)) % 3 # 랜덤하게 시작 색상 선택
            current_color = stripe_color_set[color_index]
            
            # 메인 색상이 아니면 덮어씌움
            if current_color != C1:
                 ax.add_patch(Rectangle((i * stripe_width, 0), stripe_width, flag_height, 
                                       facecolor=current_color, alpha=0.9, edgecolor='none'))

    elif pattern_type == "Horizontal Stripe":
        # 가로 줄무늬
        num_stripes = random.randint(3, 7)
        stripe_height = flag_height / num_stripes
        stripe_color_set = [C1, C2, C3]
        
        for i in range(num_stripes):
            color_index = (i + random.randint(0, 2)) % 3 
            current_color = stripe_color_set[color_index]
            
            if current_color != C1:
                ax.add_patch(Rectangle((0, i * stripe_height), flag_width, stripe_height, 
                                       facecolor=current_color, alpha=0.9, edgecolor='none'))

    elif pattern_type == "Diagonal Cross":
        # 대각선 십자가 패턴 (C2 색상 사용)
        diag_color = C2
        line_thickness = random.uniform(1.0, 1.5)
        
        # X자 형태로 두꺼운 선 그리기 (좌상단 -> 우하단)
        ax.plot([0, flag_width], [flag_height, 0], color=diag_color, 
                linewidth=line_thickness * 10, alpha=0.7)
        # X자 형태로 두꺼운 선 그리기 (좌하단 -> 우상단)
        ax.plot([0, flag_width], [0, flag_height], color=diag_color, 
                linewidth=line_thickness * 10, alpha=0.7)
        
        # 중앙에 패턴 색상(C3)으로 원이나 사각형 추가
        center_shape_size = random.uniform(2, 4)
        ax.add_patch(Rectangle((flag_width/2 - center_shape_size/2, flag_height/2 - center_shape_size/2), 
                               center_shape_size, center_shape_size, 
                               facecolor=C3, edgecolor='black', linewidth=0.5, alpha=0.9))

    elif pattern_type == "Corner Quarter":
        # 4분할 디자인 (Main, Secondary 색상 사용)
        quarter_color = C2
        
        # 좌상단
        ax.add_patch(Rectangle((0, flag_height/2), flag_width/2, flag_height/2, 
                               facecolor=quarter_color, alpha=0.9, edgecolor='none'))
        # 우하단
        ax.add_patch(Rectangle((flag_width/2, 0), flag_width/2, flag_height/2, 
                               facecolor=quarter_color, alpha=0.9, edgecolor='none'))
    
    # 3. 깃대 영역 (메인 깃발 디자인을 덮지 않도록 맨 왼쪽)
    pole_width = 1.0
    ax.add_patch(Rectangle((-pole_width, 0), pole_width, flag_height, 
                           facecolor='grey', edgecolor='black', linewidth=0.5))


# =========================================================
# 3. Streamlit 앱 구성 (이전과 동일)
# =========================================================

def main():
    st.set_page_config(page_title="깃발 생성 예술", layout="wide")
    st.title("🚩 데이터 기반 랜덤 깃발 디자인 생성기")
    st.markdown("축구팀 색상(데이터)을 활용하여 추상적인 깃발 패턴(생성 예술)을 만듭니다.")
    st.markdown("---")
    
    st.sidebar.header("🎨 깃발 설정")
    
    team_list = sorted(TEAM_COLORS.keys())
    selected_team = st.sidebar.selectbox(
        "팀을 선택하세요:",
        team_list
    )
    
    pattern_options = ["Vertical Stripe", "Horizontal Stripe", "Diagonal Cross", "Corner Quarter"]
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

        st.subheader("생성된 랜덤 깃발 디자인 (Generative Art Output)")
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
            
        fig, ax = plt.subplots(figsize=(8, 6)) # 깃발 비율에 맞춰 사이즈 조정
        draw_flag(ax, colors_data, selected_pattern)
        
        ax.set_xlim(-1, 16) # 깃대 포함
        ax.set_ylim(-1, 11)
        ax.axis('off')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        st.markdown("---")
        col_dl, col_blank = st.columns([1, 4])
        
        with col_dl:
            file_name = f"{selected_team.replace(' ', '_')}_flag_{selected_pattern}_{seed}.png"
            buf = fig.get_figure().canvas.buffer_rgba()
            
            st.download_button(
                label="🖼️ 깃발 이미지 다운로드 (PNG)",
                data=buf.tobytes(),
                file_name=file_name,
                mime="image/png"
            )


if __name__ == "__main__":
    main()
