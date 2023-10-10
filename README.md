# Content
V tomto repositáři je moje řešení testovací úkolu pro Luxonis
Řešení se skládá z dvou částí:
* scraper
* server

### Zadání
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

### Stav 
Nenastavoval jsem vlastní PostgreSQL databázi, v souboru scraper/sreality/pipelines.py je třeba vyplnit všechny údaje pro připojení se na místní databázi.
