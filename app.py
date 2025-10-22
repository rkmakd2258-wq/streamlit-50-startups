import streamlit as st

from app_ml import run_ml 


def main():
    st.title('스타트업 수익 예측 앱')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0] :
        pass
    elif choice == menu[1] :
        pass
    elif choice == menu[2] :
        run_ml()
    

if __name__ == '__main__' :
    main()