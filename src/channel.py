# my API YouTube
# AIzaSyBCSEZ1rHqCLTaVfxrLAGXhKyxCpCSBrcY
import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',

                                                          id=channel_id).execute()

        self.title: str = video_response['items'][0]['snippet']['title']
        self.description: str = video_response['items'][0]['snippet']['description']
        self.url: str = video_response['items'][0]['snippet']['thumbnails']['default']['url']
        self.count_podpishchikov: str = video_response['items'][0]['statistics']['subscriberCount']
        self.video_count: str = video_response['items'][0]['statistics']['videoCount']
        self.count_views: str = video_response['items'][0]['statistics']['viewCount']



    def print_info(self) -> None:
        """API_KEY скопирован из гугла и вставлен в переменные окружения"""
        api_key: str = os.getenv('API_KEY')
        """создаем специальный объект для работы с API"""
        youtube = build('youtube', 'v3', developerKey=api_key)

        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel_id)
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('API_KEY'))

    def to_json(self, filename):
        """метод, сохраняющий в файл значения атрибутов экземпляра"""
        channel_info = {"title": self.title,
                        "channel_id": self.channel_id,
                        "description": self.description,
                        "url": self.url,
                        "count_podpishchikov": self.count_podpishchikov,
                        "video_count": self.video_count,
                        "count_views": self.count_views}

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_info, file, indent=4, ensure_ascii=False)







