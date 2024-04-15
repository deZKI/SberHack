from elasticsearch_dsl import Document, Text


class Resume(Document):
    content = Text()

    class Index:
        name = 'resumes'
        settings = {
            "number_of_shards": 2,
        }
