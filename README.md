# ScrapperWopelis
Scraper simple de links de wopelis, para alamacenarlos en local o lo que se necesite.

IMPORTANTE: Python 2.7
Dependencias: mechanize, cookielib, bs4, re, time

# Funcionamiento

```
import scrapperwopelis
#cookies path
cookie = 'cookies.txt'
sc = scrapperwopelis.ScrapperWopelis(cookie)
```

# Funciones

```
sc = scrapperwopelis.ScrapperWopelis(cookie)
sc.getAllLinks(html)
```

Devuelve todos los enlaces correspondientes a esa pagina, junto con el titulo del capitulo (xej: Castle 5x02 - El maravilloso Scrapper)


```
sc = scrapperwopelis.ScrapperWopelis(cookie)
sc.getHtml(url)
```

Devuelve el HTML de la url

```
sc = scrapperwopelis.ScrapperWopelis(cookie)
sc.showLinks(url)
```

Genera un HTML (nombre_de_capitulo.html) con los enlaces de la url


```
sc = scrapperwopelis.ScrapperWopelis(cookie)
sc.getFullSerie(url)
```

Genera un HTML por cada capitulo de la serie y lo almacena (index en proceso)
