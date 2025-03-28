import streamlit as st
import datetime

threads = []
posts = {}

def create_thread(title):
    thread_id = str(int(datetime.datetime.now().timestamp()))
    threads.append({"id": thread_id, "title": title})
    posts[thread_id] = []
    return thread_id

def create_post(thread_id, name, content):
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    posts[thread_id].append({"name": name, "content": content, "created_at": created_at})

def main():
    st.title("スレッド一覧")
    for thread in threads:
        st.write(f'[{thread["title"]}](/thread?id={thread["id"]})')

    st.header("スレッド作成")
    title = st.text_input("タイトル")
    if st.button("作成"):
        create_thread(title)
        st.success("スレッドを作成しました。")

    thread_id = st.experimental_get_query_params().get("id", [None])[0]
    if thread_id:
        st.header("投稿一覧")
        if thread_id in posts:
            for post in posts[thread_id]:
                st.write(f'**{post["name"]}**: {post["content"]} ({post["created_at"]})')
        else:
            st.write("スレッドが存在しません。")

        st.header("投稿")
        name = st.text_input("名前")
        content = st.text_area("本文")
        if st.button("投稿"):
            create_post(thread_id, name, content)
            st.success("投稿しました。")

if __name__ == "__main__":
    main()
