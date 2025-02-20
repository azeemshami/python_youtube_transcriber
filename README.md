
# Python Youtube Transcriber

It's a simple Python FastAPI based youtube transcriber that will convert youtube video into text.

### Setup

python3 -m venv




## Installation

Install youtube transcriber app with pip3.

```bash
  python3 -m venv venv
  
  source venv/bin/activate

  pip install -r requirements

  fastapi dev main.py
```

The app will run on port http://127.0.0.1:8000

Swagger URL: http://127.0.0.1:8000/docs
## API Reference

#### Get Transciption by video link

```http
  GET /api/youtube/transcriber
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `video_url` | `string` | **Required**. Your youtube video link |



## Author

- [@azeemshami](https://www.github.com/azeemshami)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://azeemshami.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-azeem-shami-8384b0114/)

