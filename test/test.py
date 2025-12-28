from langchain_community.document_loaders.sitemap import SitemapLoader

loader = SitemapLoader("https://www.sunbeaminfo.in/sitemap.xml")

docs = loader.load()
for i in docs:
    print(docs)