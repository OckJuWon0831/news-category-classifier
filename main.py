import logging
from crawler.WebCrawler import WebCrawler
from crawler.ContentHandler import ContentHandler


logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

if __name__ == "__main__":
    content_handler = ContentHandler()
    WebCrawler(
        content_handler,
        urls=[
            "https://edition.cnn.com/article/sitemap-2023-1.html",
            "https://edition.cnn.com/article/sitemap-2023-2.html",
            "https://edition.cnn.com/article/sitemap-2023-3.html",
            "https://edition.cnn.com/article/sitemap-2023-4.html",
            "https://edition.cnn.com/article/sitemap-2023-5.html",
            "https://edition.cnn.com/article/sitemap-2023-6.html",
            "https://edition.cnn.com/article/sitemap-2023-7.html",
            "https://edition.cnn.com/article/sitemap-2023-8.html",
            "https://edition.cnn.com/article/sitemap-2023-9.html",
            "https://edition.cnn.com/article/sitemap-2023-10.html",
            "https://edition.cnn.com/article/sitemap-2023-11.html",
            "https://edition.cnn.com/article/sitemap-2023-12.html",
            "https://edition.cnn.com/article/sitemap-2024-1.html",
            "https://edition.cnn.com/article/sitemap-2024-2.html",
            "https://edition.cnn.com/article/sitemap-2024-3.html",
            "https://edition.cnn.com/article/sitemap-2024-4.html",
            "https://edition.cnn.com/article/sitemap-2024-5.html",
        ],
        stop_depth=1,
        save_file="./data/News_Articles.csv",
    ).run()
