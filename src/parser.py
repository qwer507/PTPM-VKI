import requests
from bs4 import BeautifulSoup
from src.database import Database

class ForumParser:
    def parse_page(self,path,from_file=False):
        if from_file:
            try:
                with open(path, 'rb') as f:
                    raw = f.read()
                html_content = raw.decode('windows-1251', errors='ignore')
            except OSError as e:
                print(f"[file] Не удалось прочитать {path}: {e}")
                return None
        else:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            try:
                response = requests.get(path, headers=headers, timeout=30)
                response.raise_for_status()

                html_content = response.content.decode('windows-1251', errors='ignore')

            except requests.RequestException as e:
                print(f"Ошибка загрузки: {e}")
                return []

        soup = BeautifulSoup(html_content, 'html.parser')
        post_nodes = soup.select('div[data-post]')

        if not post_nodes:
            return []

        result = []
        for node in post_nodes:
            data_post = node.get('data-post', '')
            try:
                post_id = int(data_post)
            except ValueError:
                continue
            author_node = node.select_one('span.post_nick a')
            if author_node:
                author = author_node.get_text(strip=True)
            else:
                author = ""

            msg_node = node.select_one('div.post_body')
            if msg_node:
                message_html = msg_node.decode_contents()
            else:
                message_html = ""

            result.append([post_id, author, message_html])
        return result

    def save_to_db(self,data,repo: Database):
        for message_data in data:
            repo.add(message_data[0],message_data[1],message_data[2])


if __name__ == "__main__":
    parser = ForumParser()
    db = Database()
    test_url = "https://4pda.to/forum/index.php?showtopic=1069995"
    posts = parser.parse_page(test_url)
    parser.save_to_db(posts,db)

    for post in posts:
        print(f"ID: {post[0]}, Автор: {post[1]}, Сообщение: {post[2]}")