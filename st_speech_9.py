import streamlit as st
import speech_recognition as sr
import keyboard
# 音声入力（認識）関数
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="ja-JP")
        except:
            return "" 
already_displayed = False               
while True:
    if not already_displayed:
        print("話しかけてください...")
        st.write("🤗話しかけてください...")
        already_displayed = True
    st.session_state.user_input = ""
    st.session_state.user_input = speech_to_text()
    if keyboard.is_pressed('1') :st.session_state.user_input ="こんばんは"
    if keyboard.is_pressed('2') :st.session_state.user_input ="画像の内容を説明して"
    if keyboard.is_pressed('3') :st.session_state.user_input ="石川県小松市の観光地は？"
    if keyboard.is_pressed('4') :st.session_state.user_input ="有名な道の駅は？"
    if keyboard.is_pressed('5') :st.session_state.user_input ="CIDPとは？"
    if keyboard.is_pressed('6') :st.session_state.user_input ="きょうの料理はなにがいいかな"
    if keyboard.is_pressed('7') :st.session_state.user_input ="宇宙人はいますか？"
    if keyboard.is_pressed('8') :st.session_state.user_input ="私の名前は誠です。"
    if keyboard.is_pressed('9') :st.session_state.user_input ="私の名前は？"
    if keyboard.is_pressed('0') :st.session_state.user_input ="善悪は何で決まりますか？"
    if keyboard.is_pressed('esc') :
        print("音声での問い合わせを終了しました。")
        with st.chat_message('assistant'):   
            st.write("音声での問い合わせを終了しました。") 
        #break   
    # 対話ループ 
    # 画像と問い合わせ入力があったときの処理
    #if webrtc_ctx.video_transformer: #VideoProcessor
        #frame = webrtc_ctx.video_transformer.frame  #VideoProcessor.frame 

        
    #if frame is not None and st.session_state.user_input !="":
    if st.session_state.user_input !="":    
        #サイドバーに画像を表示
        #image_placeholder.image(frame, channels="BGR")
        #ユーザーの音声入力を表示
        with st.chat_message('user'):   
            st.write(st.session_state.user_input) 
            st.session_state.user_input=""
        already_displayed = False

